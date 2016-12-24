#!/usr/bin/env python3
from lxml import html
import requests
import sys

if len(sys.argv) > 2:
    sys.exit("Usage: scpnet SCP#")

# The SCP number given in commandline
scpnum = sys.argv[1]

page = requests.get("http://www.scp-wiki.net/scp-" + scpnum)
tree = html.fromstring(page.content)

content = tree.xpath('//div[@id="page-content"]/p/*/text() | //div[@id="page-content"]/p/text()')

final = ""

for item in content:
    if item[-1] == ':' or item[-2] == ':':
        final += item
    elif item[0] == ':' or item[1] == ':':
        final = final[:-1] + item
    else:
        final += (item + "\n\n")

print(final)
