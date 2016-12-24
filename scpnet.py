#!/usr/bin/env python3
from lxml import html
import requests
import sys
import random

if len(sys.argv) > 2:
    sys.exit("Usage: scpnet.py [SCP#]")
elif len(sys.argv) == 1:
    print("Generating random file...\n")
    rnum = random.randint(0, 2999)
    scpnum = ""
    if rnum < 100:
        scpnum += "0"
        if rnum < 10:
            scpnum += "0"
    scpnum = str(rnum)
else:
    scpnum = sys.argv[1]
    print("Generating file for SCP-" + scpnum + "...\n")
page = requests.get("http://www.scp-wiki.net/scp-" + scpnum)
tree = html.fromstring(page.content)
content = tree.xpath('//div[@id="page-content"]/p')
ps = ["".join(item.xpath('.//text()')) for item in content]
final = ""
for item in ps:
    final += (item + "\n\n\n")
print(final)
