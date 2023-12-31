# MkDocsによる個人的なウェブサイトの試み 'my-mkdocs-site' A trial of personal website using 'MkDocs'

This is a personal MkDocs site based on a site structure generated by `mkdocs` python application.

## Installs

  All at once: `pip install -r requirements.txt`

1. MkDocs

### Static site generator itself

```bash
pip install mkdocs
```
#### To show it's usage, run as `mkdocs -h`.

2. Material theme

<details>
  <summary> a theme with useful intrinsic plugins like: search, blog, tags</summary>
  Every plugin, even if it is intrinsic in the theme, needs to be listed in `mkdocs.yml`.
</details>

```bash
pip install mkdocs-material
```

3. glightbox

image sizing and alignment plugin

```bash
pip install mkdocs-glightbox
```

4. macros
macro plugin

```bash
pip install mkdocs-macros-plugin
```