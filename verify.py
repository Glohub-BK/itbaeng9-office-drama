import collections, hashlib, json, re, subprocess, zipfile
from html.parser import HTMLParser
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parent
s=json.loads((ROOT/'story.json').read_text());m=json.loads((ROOT/'asset-manifest.json').read_text());html=(ROOT/'briefing.html').read_text()
class Links(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.images=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for k in ['src','href','data-image']:
   if a.get(k):self.refs.append(a[k])
  if tag=='img':self.images.append(a)
p=Links();p.feed(html)
duplicates=[x for x,n in collections.Counter(p.ids).items() if n>1];assert not duplicates,duplicates
broken=[]
for ref in p.refs+re.findall(r"url\(['\"]?([^)'\"]+)",html):
 if ref.startswith('#'):
  if ref[1:] not in p.ids:broken.append(ref)
 elif ref!='verification.json' and not ref.startswith(('http:','https:','data:')) and not (ROOT/ref.split('#')[0]).is_file():broken.append(ref)
assert not broken,broken
assert len(s['shots'])==30 and len(s['scenes'])==12
assert sum(x['duration_seconds'] for x in s['shots'])==300
assert len(m['selected_assets'])==90 and m['selected_current_batch_count']==38
all_paths=[x['path'] for x in m['selected_assets']]+m['legacy_identity_images']
for path in all_paths:
 with Image.open(ROOT/path) as im:im.verify()
for rec in m['selected_assets']:assert hashlib.sha256((ROOT/rec['path']).read_bytes()).hexdigest()==rec['sha256']
for shot in s['shots']:
 assert shot['gaze_en'] and shot['gaze_target_ko']
 previous=0
 for q in shot['dialogue']:
  assert previous<=q['start_seconds']<q['end_seconds']<=10,(shot['id'],q)
  assert q['speaker'] in s['cast'],(shot['id'],q['speaker'])
  previous=q['end_seconds']
 mapping=json.loads((ROOT/f"prompts/{shot['id']}-upload.json").read_text())
 assert all((ROOT/r['path']).is_file() for r in mapping['references'])
 assert len(mapping['references'])==mapping['reference_count']
 assert mapping['submitted'] is False
 assert 'Nobody looks into the lens' in (ROOT/f"prompts/{shot['id']}-video-en.txt").read_text()
js=re.search(r'<script>(.*?)</script>',html,re.S).group(1)
subprocess.run(['node','--check','--input-type=commonjs'],input=js.encode(),check=True,capture_output=True)
with zipfile.ZipFile(ROOT/'episode-01-seoyun-kit.zip') as z:
 assert z.testzip() is None
 assert len([p for p in z.namelist() if p.endswith('.png')])==93
out=dict(revision='04',static_checks='pass',selected_png_images_verified=90,legacy_identity_images_verified=3,broken_links=broken,duplicate_ids=duplicates,shot_count=30,scene_count=12,planned_seconds=300,dialogue_timing='within each planned ten-second shot; actual speech untested',js_syntax='pass',zip_crc='pass',zip_png_count=93,video_generated=0,new_image_resolution_counts=dict(collections.Counter(f"{x['resolution'][0]}x{x['resolution'][1]}" for x in m['selected_assets'] if x['origin_revision']=='04')),browser='see browser-verification.json when present')
(ROOT/'verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False))
