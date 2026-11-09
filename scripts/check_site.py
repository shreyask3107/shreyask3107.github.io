#!/usr/bin/env python3
"""Check the rendered profile and its local links without extra dependencies."""

import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.references = []
        self.headings = []
        self.sections = []
        self.logo_sources = []
        self.refresh_target = ""
        self.h1_count = 0
        self.publication_count = 0
        self.publication_orders = []
        self.publication_urls = []
        self.publication_venues = []
        self.scripts = 0
        self.missing_alt = 0
        self.lang = ""
        self.viewport = ""
        self.title = ""
        self._heading = None
        self._publication_heading = False
        self._venue = None
        self._text = []
        self._in_title = False
        self.html = path.read_text(encoding="utf-8")
        self.feed(self.html)
        self.text = " ".join("".join(self._text).split())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "section":
            self.sections.append(attrs.get("id"))
        for attr in ("href", "src"):
            if attr in attrs:
                self.references.append(attrs[attr] or "")
        if tag in ("h1", "h2", "h3", "h4"):
            self._heading = [tag, ""]
            self._publication_heading = "publication-title" in classes
        if tag == "a" and self._publication_heading:
            self.publication_urls.append(attrs.get("href", ""))
        if tag == "p" and "publication-venue" in classes:
            self._venue = ""
        if tag == "h1":
            self.h1_count += 1
        if "publication-row" in classes:
            self.publication_count += 1
            self.publication_orders.append(attrs.get("value", ""))
        if tag == "img" and "organization-logo" in classes:
            self.logo_sources.append(attrs.get("src", ""))
        if tag == "script":
            self.scripts += 1
        if tag == "img" and not attrs.get("alt", "").strip():
            self.missing_alt += 1
        if tag == "html":
            self.lang = attrs.get("lang", "")
        if tag == "meta" and attrs.get("name") == "viewport":
            self.viewport = attrs.get("content", "")
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.refresh_target = attrs.get("content", "").partition("url=")[2].strip()
        if tag == "title":
            self._in_title = True

    def handle_data(self, data):
        self._text.append(data)
        if self._heading is not None:
            self._heading[1] += data
        if self._venue is not None:
            self._venue += data
        if self._in_title:
            self.title += data

    def handle_endtag(self, tag):
        if self._heading is not None and tag == self._heading[0]:
            self.headings.append(tuple(self._heading))
            self._heading = None
            self._publication_heading = False
        if tag == "p" and self._venue is not None:
            self.publication_venues.append(" ".join(self._venue.split()))
            self._venue = None
        if tag == "title":
            self._in_title = False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("_site"))
    args = parser.parse_args()
    site = args.site.resolve()
    source = Path(__file__).resolve().parents[1]
    errors = []
    cache = {}

    def check(condition, message):
        if not condition:
            errors.append(message)

    def load(path):
        if path not in cache:
            cache[path] = Page(path)
        return cache[path]

    publication_pages = sorted((site / "publications").glob("*/index.html"))
    records = [path for path in (source / "_publications").iterdir()
               if path.is_file() and not path.name.startswith(".")]
    expected_logos = {f"/assets/logos/{path.name}" for path in (source / "assets/logos").iterdir()
                      if path.suffix in (".svg", ".png", ".jpg")}
    expected_venues = {
        "/publications/figlang/": "FigLang@NAACL 2024",
        "/publications/cataractbot/": "UbiComp 2025",
        "/publications/v-flute/": "NAACL 2025",
        "/publications/nanoparticle-dynamics/": "Science 2025",
        "/publications/360fusionnerf/": "IROS 2023",
        "/publications/crackseg9k/": "CVCIE@ECCV 2022",
        "/publications/icml/": "ICML 2022",
    }
    check(len(publication_pages) == len(records),
          f"Expected {len(records)} publication pages, found {len(publication_pages)}")
    paths = [site / "index.html", site / "publications/index.html",
             site / "credits/index.html", *publication_pages]

    for path in paths:
        label = str(path.relative_to(site))
        if not path.is_file():
            errors.append(f"{label}: missing page; run the Jekyll build first")
            continue
        page = load(path)
        check(page.h1_count == 1, f"{label}: expected exactly one h1")
        check(bool(page.title.strip()), f"{label}: missing title")
        check(bool(page.lang), f"{label}: missing document language")
        check("width=device-width" in page.viewport, f"{label}: missing responsive viewport")
        check(page.missing_alt == 0, f"{label}: image is missing alternative text")
        check(page.scripts == 0, f"{label}: refreshed pages should not require JavaScript")
        check(not any(count > 1 for count in Counter(page.ids).values()),
              f"{label}: duplicate element IDs")
        levels = [int(tag[1]) for tag, _ in page.headings]
        check(all(level <= previous + 1 for previous, level in zip([0, *levels], levels)),
              f"{label}: heading hierarchy skips a level")
        check("{{" not in page.html and "{%" not in page.html,
              f"{label}: unrendered Liquid template")
        check("byoeb" not in page.html.lower() and
              "build your own expert bot" not in page.html.lower(),
              f"{label}: a removed project mention or link is still present")
        for logo in page.logo_sources:
            check(logo in expected_logos, f"{label}: missing or unknown institution logo: {logo}")
        if path in publication_pages:
            check(len(page.logo_sources) == 1, f"{label}: expected one research affiliation logo")
            route = "/" + path.parent.relative_to(site).as_posix() + "/"
            if route in expected_venues:
                check(page.publication_venues == [expected_venues[route]],
                      f"{label}: expected venue label {expected_venues[route]}")
        if page.publication_count:
            valid_orders = all(value.isdecimal() and int(value) > 0
                               for value in page.publication_orders)
            check(valid_orders, f"{label}: display_order must be a positive integer")
            if valid_orders:
                orders = [int(value) for value in page.publication_orders]
                check(orders == sorted(set(orders)),
                      f"{label}: publication display orders must be unique and ascending")
            check(len(set(page.publication_urls)) == page.publication_count,
                  f"{label}: missing or duplicate publication links")
            check(len(page.publication_venues) == page.publication_count,
                  f"{label}: publication venue count does not match the list")
            venues = dict(zip(page.publication_urls, page.publication_venues))
            for route, venue in expected_venues.items():
                check(venues.get(route) == venue, f"{label}: expected {venue} for {route}")
            figlang = "/publications/figlang/"
            cataractbot = "/publications/cataractbot/"
            check(figlang in page.publication_urls and cataractbot in page.publication_urls and
                  page.publication_urls.index(figlang) + 1 == page.publication_urls.index(cataractbot),
                  f"{label}: FigLang must appear immediately before CataractBot")

        for reference in page.references:
            check(bool(reference.strip()), f"{label}: empty URL")
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            target_path = unquote(url.path)
            if not target_path:
                target = path
            elif target_path.startswith("/"):
                target = site / target_path.lstrip("/")
            else:
                target = path.parent / target_path
            target = target.resolve()
            if not target.is_relative_to(site):
                errors.append(f"{label}: URL escapes the site: {reference}")
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{label}: broken local URL: {reference}")
                continue
            if url.fragment and target.suffix == ".html":
                check(unquote(url.fragment) in load(target).ids,
                      f"{label}: missing fragment: {reference}")

    home_path = site / "index.html"
    if home_path.is_file():
        home = load(home_path)
        check(home.sections == ["about", "experience", "publications"],
              "Homepage should contain only About, Industry, and Research & Publications")
        check([text for tag, text in home.headings if tag == "h2"] ==
              ["Industry", "Research & Publications"],
              "Homepage still has a separate research or education section")
        check("/courses/" not in home.references and "/#education" not in home.references,
              "Homepage still links to removed coursework or education sections")
        check("Erasmus+" in home.html and "Technical University of Denmark" in home.html,
              "The bio is missing the DTU exchange")
        check("I work on training models for enterprise search relevance in the Frontier Tuning Team "
              "at Microsoft, Redmond." in home.text,
              "The bio is missing the requested team, employer, and location wording")
        check("My research interests" not in home.text,
              "The removed research-interests paragraph is still present")
        for detail in ("Redmond", "IC3 team", "anomaly detection for Microsoft Teams",
                       "Prof. Smaranda Muresan", "Prof. Balaraman Ravindran"):
            check(detail in home.text, f"Homepage is missing {detail}")
        check(home.publication_count == len(records), "Homepage publication count is incorrect")
        check(len(home.logo_sources) == len(records) + 1 and set(home.logo_sources) == expected_logos,
              "Homepage logos do not cover Industry and every publication")
        check("first-year" not in home.html and "Undergraduate Student at" not in home.html,
              "Homepage still contains an outdated student biography")

    archive_path = site / "publications/index.html"
    if archive_path.is_file():
        archive = load(archive_path)
        check(archive.publication_count == len(records),
              "Publication index does not match the homepage")
        check(len(archive.logo_sources) == len(records),
              "Publication index is missing institution logos")
        if home_path.is_file():
            check(archive.publication_urls == load(home_path).publication_urls,
                  "Homepage and publication index have different paper ordering")

    credits_path = site / "credits/index.html"
    if credits_path.is_file():
        check(set(load(credits_path).logo_sources) == expected_logos,
              "Logo credits do not cover every institution asset")

    for route in ("icml", "crackseg9k", "360fusionnerf"):
        check((site / "publications" / route / "index.html").is_file(),
              f"The existing publication route {route} was not preserved")
    for redirect in ("about/index.html", "about.html", "courses/index.html"):
        path = site / redirect
        check(path.is_file() and 'http-equiv="refresh"' in path.read_text(encoding="utf-8"),
              f"The existing {redirect} redirect was not preserved")
    courses_path = site / "courses/index.html"
    if courses_path.is_file():
        target = urlsplit(load(courses_path).refresh_target)
        check((target.path, target.fragment) == ("/", "about"),
              "The removed coursework page should redirect to About")
    for private_path in (".tools", ".bundle", "vendor", "scripts", "Gemfile.lock"):
        check(not (site / private_path).exists(), f"Build tooling leaked into the site: {private_path}")

    if errors:
        print("Site checks failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Validated {len(paths)} pages, {len(records)} publications, "
          f"{len(expected_logos)} institution logos, and all local links/redirects.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
