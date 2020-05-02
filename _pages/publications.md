---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}


### Note:
****************************************
If any link doesn't work, feel free to email me to get the pdf.

<script type="text/javascript" id="clustrmaps" src="//cdn.clustrmaps.com/map_v2.js?d=vuy8oJHmtOg7LUHtjdY1k-B5CjSIsQ-mzVNm9KPAL0M&cl=ffffff&w=a"></script>
