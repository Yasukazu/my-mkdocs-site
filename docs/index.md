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
## Blog
  This site uses 'Blogging' plugin: [MkDocs Blogging plugin homepage](https://liang2kl.github.io/mkdocs-blogging-plugin/)
### Usage of Blogging:
#### Meta tags of articles:
```yaml
---
title: An article
description: A test article
time: 2023-4-13 00:48 
---
```
  
{{ blog_content }}
