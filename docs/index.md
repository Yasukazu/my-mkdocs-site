# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build -d ../web/www/docs` - Build the documentation site output on a directory of '-d' option.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        blog/
            index.md
            posts/
                article-1.md
        ...       # Other markdown pages, images and other files.
## mkdocs.yml
```yaml
site_name: My Docs
site_url: https://makyno.jp/docs/
theme: 
    name: material
    language: 'ja'
extra:
  search:
    language: 'jp'
plugins:
  - blogging:
      dirs: # The directories to be included
        - blog
```
## ブロギング
  This site uses 'Blogging' plugin: [MkDocs Blogging plugin homepage](https://liang2kl.github.io/mkdocs-blogging-plugin/)

ここから先はブログ(資料の追加・更新の記録です) / From here, blog(i.e. log of add/update of articles):
  
{{ blog_content }}
