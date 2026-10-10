# -*- coding: utf-8 -*-
import argparse,datetime,fcntl,json,shutil
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('stage',choices=['pre','post','fail']);p.add_argument('id');p.add_argument('--source');p.add_argument('--error',default='');a=p.parse_args()
s=next(x for x in json.loads((ROOT/'asset-specs.json').read_text()) if x['id']==a.id)
meter='N/A — provider does not expose a credit meter'
e={'time':datetime.datetime.now().astimezone().isoformat(),'stage':a.stage,'id':a.id,'provider':'OpenAI built-in imagegen','mode':s['mode'],'model':'not exposed','output_count_requested':1,'requested_resolution':[1152,2048],'duration':'N/A','references':s['references'],'displayed_balance':meter,'displayed_per_run_cost':meter,'maximum_expected_usage':'1 call / 1 image; credits not exposed','expected_remaining_balance':meter,'actual_charge':meter,'remaining_balance':meter,'retry_index':s.get('retry',0)}
if a.stage=='post':
 out=ROOT/s['output'];out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(a.source,out)
 with Image.open(out) as im:e['actual_resolution']=list(im.size)
 e.update(output=s['output'],source=a.source,successful=1,failed=0,separate_export_upscale_audio_lipsync_generations=0)
elif a.stage=='fail':e.update(error=a.error,successful=0,failed=1)
with (ROOT/'generation-events.jsonl').open('a') as f:
 fcntl.flock(f,fcntl.LOCK_EX);f.write(json.dumps(e,ensure_ascii=False)+'\n')
with (ROOT/'generation-ledger.md').open('a') as f:
 fcntl.flock(f,fcntl.LOCK_EX);f.write(f"| {e['time']} | {a.stage.upper()} {a.id} | imagegen / {s['mode']} / model not exposed | 1 image / {e.get('actual_resolution',[1152,2048])} / duration N/A | {', '.join(s['references']) or 'none'} | {meter} | {e.get('output',a.error) or 'pending; maximum 1 call / 1 image'}; retry {e['retry_index']}; separate export/upscale/audio/lip-sync 0 |\n")
print(json.dumps(e,ensure_ascii=False))
