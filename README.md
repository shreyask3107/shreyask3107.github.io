# Shreyas Kulkarni - Personal Website

Source for [shreyask3107.github.io](https://shreyask3107.github.io/), built with
Jekyll and compatible with GitHub Pages.

The refreshed profile is a compact, responsive page with three sections:
About, Industry (all Microsoft roles together), and Research & Publications.
Education and the DTU exchange are summarized in the biography rather than
repeated in a separate section. Its layout is an original implementation inspired by
[Tanay Dixit's profile](https://tanay2001.github.io/); no source code or assets
from that site are copied.

## Editing content

| Content | Source |
| --- | --- |
| Short biography | [_pages/about.md](./_pages/about.md) |
| Microsoft industry experience | [_data/profile.yml](./_data/profile.yml) |
| Institution names, logos, and attribution | [_data/organizations.yml](./_data/organizations.yml) |
| Contact links and site metadata | [_config.yml](./_config.yml) |
| Publication records and summaries | [_publications/](./_publications/) |
| Portrait | [images/shreyas_kulkarni.jpg](./images/shreyas_kulkarni.jpg) |
| Layout and styling | [_layouts/profile-home.html](./_layouts/profile-home.html), [assets/css/profile.css](./assets/css/profile.css) |

Publication records are the single source for the homepage, publication index,
and individual paper pages. Each record needs a title, permalink, authors,
publication year, a short venue label, paper URL, a unique positive integer
`display_order`, and an `organization` key matching
[_data/organizations.yml](./_data/organizations.yml). Institution logos show
Shreyas's research affiliation for the project, not the affiliations of every
coauthor. Logos retain accessible names without duplicate visible affiliation
captions. Code, project, and video URLs are optional.

Lists use `display_order`, lowest first, independently of publication year.
The FigLang shared-task paper is placed immediately before CataractBot;
other papers retain their relative order. Update these numbers when reordering
or adding papers. Keep venue labels concise, such as `CVCIE@ECCV`, `FigLang@NAACL`,
and `IROS`; the year is appended automatically. Use Markdown bold to highlight
Shreyas's name in the author list.

Logo files are served locally from [assets/logos/](./assets/logos/). Their sources,
rights information, and any modifications are documented on the
[logo credits page](./_pages/credits.html), linked from the footer. The IIT Madras
asset retains its CC BY-SA 4.0 license; image rights are separate from the site's
code license.

The existing `/publications/` and three older paper routes remain available.
Paper routes use directory-style URLs; GitHub Pages redirects their original
slashless URLs to the trailing-slash versions. Coursework is no longer displayed,
and `/courses/` redirects to the About section instead of returning a broken link.

Only a short public biography and public contact links are included in the
refresh. Do not copy the full private CV, account recovery codes, or other
credentials into this repository.

## Local development

Use Ruby with Bundler. On this machine, an isolated Ruby installation is already
available inside the ignored `.tools/ruby` directory:

```sh
cd /home/kulkarnis/fun/github_profile
export PATH="$PWD/.tools/ruby/bin:$PATH"
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000 --config _config.yml,_config.dev.yml
```

Open <http://127.0.0.1:4000>. Jekyll watches content changes; restart the server
after editing configuration. On another machine with Ruby and Bundler already
installed, omit the project-local `PATH` line.

The profile, publication, and logo credits pages use local CSS and no JavaScript
or third-party analytics. Older archived pages retain their original theme.

## Validation

```sh
bundle exec jekyll build
python3 scripts/check_site.py
```

The dependency-free check validates the refreshed pages, publication counts and
order, short venue labels, bio/industry content, headings, institution logos,
internal links, fragments, local assets, and the about/coursework redirects.
Also check the preview in a browser at desktop and mobile widths before
publishing.

Local builds do not publish anything. Review the rendered result before pushing
changes to the GitHub Pages repository.

## Template attribution

The original site is based on [AcademicPages](https://academicpages.github.io/)
and [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/).
Their existing license and archived theme files are retained; see
[LICENSE](./LICENSE).
