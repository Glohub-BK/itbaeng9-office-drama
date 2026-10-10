import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
d = json.loads((ROOT / 'story.json').read_text())
specs = json.loads((ROOT / 'asset-specs.json').read_text())
names = {k: v['name'] for k, v in d['cast'].items()}
english_names = {'S':'Sujeong','J':'Yoon Junseo','H':'Han Jinwoo','Y':'Seoyun'}
gazes = {
 'K01': ('유리 출입구와 걷는 방향', 'Sujeong looks toward the glass entrance to viewer right, never toward the lens.'),
 'K02': ('커피를 건네는 직원 → 출입구', 'Look at the person handing her coffee, then the entrance along her walking direction.'),
 'K03': ('수정이 ↔ 준서', 'Both coworkers look at each other, not at the observer camera.'),
 'K04': ('준서는 수정이, 수정이는 준서', 'Junseo answers while looking at Sujeong; she listens looking at him.'),
 'K05': ('의자·키보드·모니터', 'Sujeong looks down at her chair and keyboard, then at the monitor.'),
 'K06': ('파일 → 상대 얼굴', 'Eyes follow the one folder during handoff, then the colleague face.'),
 'K07': ('인사하는 한 실장과 수정이', 'Han looks toward Sujeong while greeting; Sujeong looks toward Han.'),
 'K08': ('모니터와 키보드', 'Sujeong watches her work monitor and keyboard with tired concentration.'),
 'K09': ('오른쪽 사무실 출구', 'Sujeong eyes follow the open office exit to viewer right.'),
 'K10': ('복도 진행 방향 → 왼쪽 기획실 문', 'Initially look down the corridor, then turn head toward the planning-room door on viewer left.'),
 'K11': ('왼쪽 기획실 문틈', 'Look toward the doorway on viewer left, listening with lips closed.'),
 'K12': ('서윤과 한 실장은 보고서 → 상대 얼굴', 'Seoyun studies the report and Han; Han points at the report and glances at Seoyun.'),
 'K13': ('문틈 쪽에 시선을 둔 채 듣기', 'Sujeong eyes point toward the door gap at viewer left; she listens, her lips remain closed.'),
 'K14': ('한 실장은 화면 밖 서윤', 'Han addresses Seoyun off-screen at the existing desk-side eyeline, not the lens.'),
 'K15': ('문틈 → 뒤로 물러설 바닥', 'Sujeong briefly watches the doorway, then checks the floor while retreating.'),
 'K16': ('돌아갈 사무실과 복도 옆 방향', 'Sujeong looks toward the return path beside the camera, sufficiently off-axis to avoid eye contact.'),
 'K17': ('휴대폰 화면', 'Sujeong looks down at her one phone, visibly worried, no portrait smile.'),
 'K18': ('수정이 ↔ 준서', 'Both remain seated and look at each other across the table.'),
 'K19': ('수정이는 준서에게 설명', 'Sujeong speaks toward Junseo, with occasional downward thinking glances.'),
 'K20': ('준서는 수정이에게 확인', 'Junseo looks at Sujeong while asking his clarification.'),
 'K21': ('수정이 ↔ 준서', 'Sujeong confirms while looking at Junseo; he listens to her.'),
 'K22': ('준서는 수정이에게 약속', 'Junseo addresses Sujeong with a steady reassuring eyeline.'),
 'K23': ('대화 상대', 'Speakers alternate naturally and keep their gaze on their partner.'),
 'K24': ('출구·퇴근 방향', 'Sujeong looks along the path toward the office exit while leaving.'),
 'K25': ('휴대폰 화면 → 퇴근길', 'Sujeong checks her phone, then looks along her route home.'),
 'K26': ('수정이 ↔ 서윤', 'Seoyun looks at Sujeong while delivering the news; Sujeong listens looking at her.'),
 'K27': ('수정이 ↔ 서윤, 뒤쪽 빈 의자는 공간 단서', 'Both keep their gaze on their conversation partner. The empty chair stays a background clue, not a required final eyeline.'),
 'K28': ('수정이 ↔ 서윤', 'Seoyun leans toward seated Sujeong and meets her gaze; both keep their attention on their conversation.'),
 'K29': ('수정이 ↔ 한 실장', 'Han addresses Sujeong; Sujeong responds toward him, not the lens.'),
 'K30': ('한 실장이 떠난 복도 방향', 'Sujeong looks toward the corridor Han used, off-camera rather than into the lens.'),
}
patch = {
 'K01': dict(start_ko='수정이가 회사 앞을 걸으며 오른쪽 출입구를 바라보는 전신 컷', start_en='Full-body Sujeong walking along the office sidewalk, gaze at entrance on viewer right, tote on her right shoulder; her right hand naturally grips the strap.'),
 'K09': dict(camera_ko='허리 위 구도에서 천천히 뒤로 이동하며 전신으로 열고, 출구를 향한 첫걸음을 따라간다', motion_en='Start in the selected waist-up composition. During seconds 1–3, visibly pass the ONE phone from her left hand to her right hand. Slowly pull back while she releases the chair and takes a step toward the office exit on viewer right, ending with her full body visible. Stay on the same office side; no sudden framing jump or phone duplication.'),
 'K10': dict(qa_note_ko='시작·끝 모두 새 시선 보정본. 뒤에서 복도 진행 방향을 바라보다 왼쪽 기획실 문으로 고개를 돌린다. 실제 출력 941×1672.'),
 'K14': dict(title='한 실장의 정상 처리 지시', motion_en='A shallow camera arc on the same desk side with modest tightening. Han answers the question heard in the previous shot while looking toward off-screen Seoyun. Only Han speaks in this shot; do not animate an additional speaker.'),
 'K16': dict(camera_ko='수정이가 사무실로 되돌아가도록 천천히 몸을 돌리고, 카메라는 같은 복도 축에서 뒤로 물러난다', motion_en='The start shows Sujeong rear three-quarter. During seconds 0–4 she physically pivots toward the return path and walks back toward her office. The camera retreats along the same corridor axis to reveal the selected front three-quarter end. Her gaze stays toward the path at viewer right, never the camera. Keep ONE phone low in her anatomical right hand. This is an actor pivot, not an instantaneous camera reverse.'),
 'K17': dict(qa_note_ko='시작 시선과 표정을 휴대폰을 보는 걱정으로 보정했다. 미소를 유지하는 인물 포즈를 요청하지 않는다.', motion_en='Slow push keeping her face and one phone together. She starts worried, reads the screen and contacts Junseo; no smiling or gaze toward the camera. Phone message lettering is added in post.'),
 'K27': dict(start_ko='업무 자리 옆에 앉아 서로 바라보는 수정이 왼쪽·서윤 오른쪽의 가까운 투샷', start_en='Close seated two-shot near their work desks, Sujeong viewer left and Seoyun viewer right. Sujeong looks toward Seoyun and asks about the accident. No phone held.', end_ko='수정이는 손을 내리며 서윤에게 시선을 유지하고 서윤이 답한다. 뒤쪽 빈 의자가 공간 단서로 남는다.', end_en='Same seated two-shot, Sujeong lowers her gesturing hands and keeps her gaze on Seoyun, who answers with concern. Empty chair remains in background.', motion_en='Both remain seated. Sujeong asks her question with a small hand gesture, then lowers her hands naturally as Seoyun answers. Small continuous camera slide and modest tightening on the same side. Gaze remains partner-to-partner, no lens eye contact, no sudden standing or vanishing tote.'),
 'K28': dict(start_ko='수정이는 책상 왼쪽에 앉고 서윤은 오른쪽에서 몸을 조금 기울여 작은 목소리로 말한다. 휴대폰 한 개는 책상 위에 화면이 위로 놓여 있다.', start_en='Sujeong seated viewer left, Seoyun standing viewer right leans slightly toward her. Both hands remain separate and natural; ONE phone lies screen-up, dark screen, on the desk.', end_ko='같은 좌우와 자세를 유지한 더 가까운 투샷. 수정이가 서윤의 고백을 듣고 올려다보며 되묻는다.', end_en='A slightly tighter two-shot with unchanged seated Sujeong left and standing Seoyun right; Sujeong looks up at Seoyun in recognition and fear. Keep the one phone on the desk.', camera_ko='같은 축에서 천천히 접근해 두 사람의 시선과 작은 표정 변화를 보여준다'),
}
for s in d['shots']:
 s.update(patch.get(s['id'], {}))
 s['gaze_target_ko'], s['gaze_en'] = gazes[s['id']]
 s['background_asset'] = next(x['output'] for x in specs if x['id']==s['background'] + ('-r1' if s['background'] in ['B06','B07'] else ''))
 visible = list(dict.fromkeys(d['character_wardrobe_map'][w] for w in s['wardrobe']))
 s['visible_cast'] = visible
 s['offscreen_cast'] = list(dict.fromkeys(q['speaker'] for q in s['dialogue'] if q['speaker'] in names and q['speaker'] not in visible))
 for edge in ['start','end']:
  assert (ROOT / s['keyframes'][edge]).is_file(), (s['id'], edge)
 refs=[dict(path=d['cast'][k]['identity'],role='authoritative facial identity: '+english_names[k],role_ko=names[k]+' 얼굴 원본') for k in visible]
 refs += [dict(path='assets/wardrobe/'+w+'.png',role='clothing and hair only: '+english_names[d['character_wardrobe_map'][w]],role_ko=names[d['character_wardrobe_map'][w]]+' 복장·헤어 '+w) for w in s['wardrobe']]
 refs += [dict(path=s['background_asset'],role='room topology and lighting',role_ko='배경·공간·조명'),dict(path=s['keyframes']['start'],role='exact initial composition',role_ko='같은 쇼트 시작 구도'),dict(path=s['keyframes']['end'],role='target final composition',role_ko='같은 쇼트 끝 구도')]
 mapping=dict(shot=s['id'],duration_seconds=10,aspect_ratio='9:16',visible_cast=visible,offscreen_cast=s['offscreen_cast'],references=refs,reference_count=len(refs),voice_refs=[],submitted=False,provider_mode='planned start/end image-conditioned video; current input limits must be verified',requires_current_cost_check=True,gaze_target_ko=s['gaze_target_ko'],priority_if_provider_limits_references='Start/end frames first; use additional identity/wardrobe references only when supported. Do not imply that all listed images can be uploaded to every provider.')
 (ROOT / f"prompts/{s['id']}-upload.json").write_text(json.dumps(mapping,ensure_ascii=False,indent=2))
 prompt=f"Generate ONE continuous approximately 10-second live-action shot, portrait 9:16. Restrained Korean summer office mystery. Shot {s['id']}. Visible actors: {', '.join(english_names[k] for k in visible)}. Fictional adult characters. The camera is an unnoticed observer, not a photographer. Nobody looks into the lens, smiles at the audience, holds a fashion pose or turns back without a story reason.\nUse each actor face master solely for that actor facial identity, each separate wardrobe image for their summer garments, the location master for geography and the start/end images for exact compositions. Sujeong is the short-bob woman, Seoyun is the long-haired woman; NEVER blend their faces or exchange hair. Preserve original face, adult age, body proportions, opaque summer workwear, skirts, flat footwear, jewelry and employee ID.\nSTART: {s['start_en']}\nEND: {s['end_en']}\nCAMERA AND ACTION: {s['motion_en']}\nGAZE: {s['gaze_en']}\nOne motivated camera move on the same side of the action axis. Natural walking, weight transfer, hands, listening reactions and breathing. No hard reverse-angle morph, teleportation, sudden body turn, extra limbs, frozen dissolve, object duplication or unexplained hand swaps. Let eyes follow the scene target, never the moving camera. Different angles between neighboring shots are editorial cuts, not continuous interpolation. Camera distances and degrees are approximate direction, not measured calibration.\nDIALOGUE (exact Korean; local times within this 10-second shot are estimates to test):\n"
 for q in s['dialogue']:
  prompt += f"{q['start_seconds']}–{q['end_seconds']}s | {english_names.get(q['speaker'],q['speaker'])} | {q['mode']} | \"{q['text_ko']}\"\n"
 if not s['dialogue']: prompt+='No spoken dialogue.\n'
 prompt+='One speaker at a time. Visible listeners keep lips closed during another speaker line. Off-screen voices never animate the listener lips. No voice samples are prepared; test Korean diction, actor voice continuity and speaking duration before full production. Ambient sound only; one episode music track is added in post. Phone messages, company labels, time cards, report wording and Korean subtitles are composited later, no invented readable text. Hold a usable end composition for about one second after action. These reference pairs do not prove video motion will succeed. No video has been submitted. Check current provider duration, reference limits, displayed balance and quoted charge before any submission.'
 (ROOT / f"prompts/{s['id']}-video-en.txt").write_text(prompt)
 s['keyframes_status']='generated_reference_pair; video motion and speech not tested'
for c in d['scenes']:
 shots=[s for s in d['shots'] if s['scene_id']==c['id']]
 c['dialogue']=[{k:q[k] for k in ['speaker','text_ko','mode']} for s in shots for q in s['dialogue']]
 for plan in c['shot_plan']:plan['description_ko']=next(s['title'] for s in shots if s['id']==plan['id'])
d['continuity'] += [x for x in [
 '서윤 Y는 긴 짙은 갈색 머리의 별도 성인 인물. 첫날 W06 로즈·아이보리 H라인, 다음 날 W07 민트·샌드 A라인을 사용한다. W08–W13은 후속 화 비교 코디다.',
 '서윤은 은폐 지시를 직접 받은 직원이고 수정이는 문 밖에서 이를 들었다. 서윤은 당시에 문 밖 수정이를 보지 못했다.',
 'K26 사고 소식 후 K27에서는 업무 자리 근처에 앉은 구도로 편집 전환한다. K28에서 서윤은 서서 수정이에게 조용히 말한다. 서로 다른 쇼트의 앉기·서기 상태는 한 영상 안의 순간 변신으로 연결하지 않는다.',
 'K28→K29는 편집 컷. 서윤은 자기 자리로 돌아간 뒤 한 실장이 접근한 것으로 연결하며 프레임 안 인물 삭제 모핑을 요청하지 않는다.',
 '장면 사진의 배우 시선은 문·휴대폰·상대·작업을 향한다. 스튜디오 복장·방향 참조는 실제 장면 연기용 키프레임으로 사용하지 않는다.'
] if x not in d['continuity']]
d['video_submissions']=0;d['voice_samples']=0
d['duration_validation']='30 planned shots x approximately 10s = 300s source target, not an edited five-minute film; motion and speech untested'
(ROOT/'story.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
def mm(v):return f'{v//60}:{v%60:02}'
md=['# 그날 밤, 기획실 — 개정안 04','','수정이 시선 보정·서윤 추가. 2026-10-10. 영상 미생성·미접수.','','평범한 출근 → 근무·야근 → 문틈에서 한 실장의 지시와 서윤의 질문 → 준서에게 상담 → 다음 날 보고 전 사고 → 서윤이 직접 지시받았다고 고백 → 수정이의 불안. 사고 원인과 회사 개입은 미확정.','','## 촬영 시선','','렌즈 응시·촬영자를 향한 미소·동기 없는 뒤돌아보기 금지. 인물은 대화 상대, 문틈, 휴대폰, 모니터와 진행 방향을 본다. 반응 쇼트의 입은 실제 화자와 구분한다.','','## 날짜·복장','','수정이 첫날 W01 / 다음 날 W02. 서윤 첫날 W06 / 다음 날 W07. 후속 화 비교 W08–W13을 같은 날 섞지 않는다.','','## 쇼트 계획','']
for c in d['scenes']:
 md += [f"## {c['id']} {c['title']} · {mm(c['timeline_start_seconds'])}–{mm(c['timeline_end_seconds'])}",'',c['story_time']+' / '+c['location'],'','관객이 알게 되는 것: '+c['audience_understands'],'']
 for s in [s for s in d['shots'] if s['scene_id']==c['id']]:
  md += [f"### {s['id']} {s['title']}",'','시작: '+s['start_ko'],'','끝: '+s['end_ko'],'','시선: '+s['gaze_target_ko'],'','카메라: '+s['camera_ko'],'',f"[시작]({s['keyframes']['start']}) · [끝]({s['keyframes']['end']}) · [영문 영상 프롬프트](prompts/{s['id']}-video-en.txt)",'']
  md += [f"- {q['start_seconds']}–{q['end_seconds']}초 {names.get(q['speaker'],q['speaker'])}: “{q['text_ko']}” ({q['mode']})" for q in s['dialogue']]
  md += ['', '검수: '+s['qa_note_ko'],'']
(ROOT/'episode-01-script.md').write_text('\n'.join(md))
(ROOT/'README.md').write_text('# 개정안 04 — 수정이 시선과 여직원 서윤\n\n[HTML 브리핑](briefing.html) · [대본](episode-01-script.md) · [서윤 상세 설정](character-bible.md) · [원장](generation-ledger.md) · [실제 이미지 목록](asset-manifest.json) · [ZIP](episode-01-seoyun-kit.zip)\n\n스튜디오 복장 8장과 45도 간격 방향 참조 8장을 별도로 준비했다. 장면에는 첫날 W06, 다음 날 W07만 사용한다. 수정이 시선 13프레임, 서윤 장면 4쇼트의 시작·끝 8프레임을 교체했다. 개정안 03의 기존 결과는 보존한다. 실제 해상도와 생성 수는 매니페스트 기준이며 이미지 자체를 2K로 확대하지 않았다. 영상·음성·립싱크는 아직 생성하지 않았다.\n')
print('Finalized 30 gaze-aware prompts and four-character mappings')
