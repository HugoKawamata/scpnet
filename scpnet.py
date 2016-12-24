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

for item in content:
    print(item + "\n")
