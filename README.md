# 그날 밤, 기획실 · IT뱅구

[모바일·PC HTML 브리핑](https://glohub-bk.github.io/itbaeng9-office-drama/) · [선택 원본 제작 자료 ZIP](https://github.com/Glohub-BK/itbaeng9-office-drama/releases/download/v0.4.0/episode-01-seoyun-kit.zip) · [상세 인물 설정](character-bible.md) · [전체 한글 대본](episode-01-script.md)

수정이가 야근 중 문 밖에서 회사의 점검 결과 은폐 지시를 듣고 선배에게 상담한다. 다음 날 선배의 사고 소식을 전한 서윤은 자신이 그 지시를 직접 받았다고 밝힌다. 사고 원인과 회사 개입은 아직 확정하지 않는다.

## 최신 제작 기준

2026-10-10 개정안 04. 성인 창작 인물 수정이·서윤·윤준서·한진우. 서윤 얼굴 1장·여름 복장 8장·45도 간격 방향 참조 8장, 수정이 시선 보정 13장, 서윤 등장 4쇼트의 시작·끝 8장을 새로 선택했다. 신규 선택 38장 + 개정안 03 재사용 52장 + 기존 얼굴 원본 3장이다. 저장소에는 현재 이미지와 보정 이력을 보관하고, ZIP에는 선택 원본 PNG 93장을 포함한다.

카메라는 관찰자다. 인물은 상대·문틈·휴대폰·작업 대상을 보고 렌즈를 응시하지 않는다. 각 장면의 한글 대사·시선·카메라 지시와 영문 생성 프롬프트를 HTML에서 확인할 수 있다.

30쇼트 × 약 10초는 원본 영상 300초의 계획이다. **완성 영상·영상 접수·음성 샘플은 아직 없다.** 이미지 생성은 OpenAI 내장 imagegen. 2K 세로를 요청했지만 신규 실제 출력은 941×1672이며 확대하지 않았다. 호출 42 / 성공 40 / 실패 2 / 실패 후 재요청 2 / 방향 품질 보정 2. 크레딧 잔액·단가·청구는 `N/A — provider does not expose a credit meter`.

## 파일 안내

- `index.html`, `briefing.html`: 모바일·PC 반응형 보기, 장면 필터, 원본 확대, 프롬프트 복사.
- `assets/`: 얼굴·복장·방향·배경·키프레임 원본과 현재 폴더의 보정 전 이력.
- `prompts/`: 영문 이미지·영상 프롬프트, 참조 이미지별 역할과 순서.
- `story.json`, `episode-01-script.md`, `character-bible.md`: 최신 이야기와 인물.
- `asset-manifest.json`, `generation-ledger.md`, `generation-events.jsonl`: 선택 이미지·생성 전후 회계. 공개 기록의 공급자 원본 로컬 경로는 생략했다.
- `quality-review.md`, `verification.json`: 직접 이미지 검수와 파일·대사 시각·링크·JS·ZIP 검사.

## 업데이트

GitHub Pages는 `main` 브랜치 루트를 배포한다. HTML과 자산을 수정해 커밋하면 같은 모바일 주소로 갱신된다. ZIP은 GitHub Release에 별도로 올린다. 버전별 다운로드 주소는 `deployment.json`을 기준으로 관리한다. 다른 이미지 스튜디오·모델 뷰어 앱 저장소와 분리한다.

사진만으로 얼굴 보존율이나 영상의 동작 성공을 보장하지 않는다. 날짜별 W06/W07 우선 참조, 화자·시선·손·소품·대사 길이 검수 사항은 `quality-review.md`에 남긴다.

기획·제작 관리 강병구 · IT뱅구 · 2026.
