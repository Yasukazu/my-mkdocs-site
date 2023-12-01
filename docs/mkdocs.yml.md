``` yaml
site_name: 家族のための資料
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
  - glightbox  
nav:
  - index.md
markdown_extensions:
  - attr_list
  - md_in_html
extra_css:
  - stylesheets/extra.css
#  - blogging:
#      dirs: # The directories to be included
#       - blog
```