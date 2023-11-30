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
  - blog:
      blog_dir: .
  - search
  - tags
nav:
  - index.md
#  - blogging:
#      dirs: # The directories to be included
#       - blog
```
## ブログ
  This site uses the built-in blog plugin in Material theme [How to use the built-in blog plugin](https://squidfunk.github.io/mkdocs-material/blog/2022/09/12/blog-support-just-landed/)
    This site ever used 'Blogging' plugin: [MkDocs Blogging plugin homepage](https://liang2kl.github.io/mkdocs-blogging-plugin/)
      {{ blog_content }}

ここから先はブログ(資料の追加・更新の記録です) / From here, blog(i.e. log of add/update of articles):
