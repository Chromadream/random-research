import re
import glob
import os

pages = []
for f in sorted(glob.glob("*.html")):
    if f == "index.html":
        continue
    content = open(f).read()
    m = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE)
    title = m.group(1) if m else os.path.splitext(f)[0]
    pages.append((f, title))

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Random Research</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/concrete.css/3.1.0/concrete.min.css">
</head>
<body>
<main>
<h1>Random Research</h1>
<ul>
"""

for f, title in pages:
    html += f'  <li><a href="{f}">{title}</a></li>\n'

html += """</ul>
</main>
</body>
</html>"""

with open("index.html", "w") as out:
    out.write(html)

print(f"Generated index with {len(pages)} pages")
