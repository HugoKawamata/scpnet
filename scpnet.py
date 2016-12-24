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

content = tree.xpath('//div[@id="page-content"]/p')

ps = ["".join(item.xpath('.//text()')) for item in content]

final = ""

for item in ps:
    final += (item + "\n\n\n")

print(final)
