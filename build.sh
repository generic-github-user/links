#pandoc --from markdown+footnotes --to gfm+footnotes --toc -s links.md -o README.md
pandoc -s --from markdown --to markdown --toc --toc-depth 1 links.md -o README.md
