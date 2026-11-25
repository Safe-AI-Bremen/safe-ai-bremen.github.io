# Safe AI Bremen

The English site starts at `index.html` and the German edition at `de/index.html`. Both work directly from disk. To preview the site in a browser, run this command from the repository directory, then open <http://127.0.0.1:4173>.

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

To edit the site, update page copy and dated event listings in `site_source/content.py`. Shared layouts, navigation and homepage copy live in `site_source/build.py`. Run `python3 site_source/build.py` to regenerate both editions. Styling and locally hosted artwork and fonts live in `assets/`.

The founder contacts and the operator’s postal address are defined at the top of `site_source/content.py`. The privacy notice covers GitHub Pages and the founders’ Gmail inboxes. Update both language editions if the hosting provider, email provider or data-handling practices change.
