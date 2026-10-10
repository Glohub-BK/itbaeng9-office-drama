"""Rebuild this episode locally before committing a Pages update; no generation or upload."""
import json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
deployment=json.loads((ROOT/'deployment.json').read_text())
readme=(ROOT/'README.md').read_text()
for script in ['finalize-story.py','build-briefing.py','verify.py']:
 subprocess.run([sys.executable,str(ROOT/script)],cwd=ROOT,check=True)
(ROOT/'README.md').write_text(readme)
page=(ROOT/'briefing.html').read_text().replace('href="episode-01-seoyun-kit.zip"','href="'+deployment['release_download']+'"')
page=page.replace('</head>',f'<meta property="og:title" content="그날 밤, 기획실 · IT뱅구"><meta property="og:image" content="{deployment["site_url"]}assets/keyframes/K28-end-seoyun.png"></head>')
(ROOT/'index.html').write_text(page)
(ROOT/'briefing.html').write_text(page)
print('HTML updated locally. Review, upload ZIP to the release, then commit and push main to update the same Pages URL.')
