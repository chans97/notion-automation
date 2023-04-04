# notion-diary automation

## 배경
1. 기존에 notion을 활용해서 diary를 적고 있었다.
2. 매일 매일 일기를 처음부터 쓰는 게 귀찮아서 아래 두 가지 기능을 zapier로 자동화시켰다.
   - 매일 자정에 일기 템플릿 생성 
   - 구글 캘린더에 종료된 일정 자동 기록
3. 그러나 zapier가 zap을 다 소진했다고 유료로 바꾸라고 한다.
4. 이 기능이 유료로 월 2만원 씩 쓸 기능은 아닌 것 같다.
5. 스스로 만들어보기로 한다.

## 구현 기능
- [ ] 매일 자정에 일기 템플릿 생성
- [ ] 구글 캘린더에 종료된 일정 자동 기록 

## 서비스 구현
1. 우선 24시간 동작해줄 서버가 필요하다. → oracle 무료 서버로 이용 (완료)
2. notion-api를 활용해서 템플릿 생성
   - notion table을 활용해서 템플릿을 만들어 놓고
   - 그 table에 item을 추가하는 방식
   - jenkins가 자정에 해당 python script 실행
3. google calendar api를 활용해서 event가 종료된 것을 감지하고
   - jenkins가 15분에 한 번씩 종료된 event 감지
4. notion-api를 활용해서 다이어리에 추가