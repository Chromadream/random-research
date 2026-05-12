import re
import glob
import os
import subprocess
from datetime import datetime, timezone

def last_updated(path):
    out = subprocess.run(
        ["git", "log", "-1", "--format=%cI", "--", path],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    if not out:
        return datetime.fromtimestamp(os.path.getmtime(path), tz=timezone.utc)
    return datetime.fromisoformat(out)

pages = []
for f in glob.glob("*.html"):
    if f == "index.html":
        continue
    content = open(f).read()
    m = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE)
    title = m.group(1) if m else os.path.splitext(f)[0]
    pages.append((f, title, last_updated(f)))

pages.sort(key=lambda p: p[2], reverse=True)

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

for f, title, updated in pages:
    utc = updated.astimezone(timezone.utc)
    stamp = utc.strftime("%Y-%m-%d")
    iso = utc.date().isoformat()
    html += (
        f'  <li><a href="{f}">{title}</a> '
        f'<small><time datetime="{iso}">updated {stamp}</time></small></li>\n'
    )

html += """</ul>
</main>
</body>
</html>"""

with open("index.html", "w") as out:
    out.write(html)

print(f"Generated index with {len(pages)} pages")
