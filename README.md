# notion-diary automation

## 배경
1. 기존에 notion을 활용해서 diary를 적고 있었다.
2. 매일 매일 일기를 처음부터 쓰는 게 귀찮아서 아래 두 가지 기능을 zapier로 자동화시켰다.
   - 매일 자정에 일기 템플릿 생성 
   - 구글 캘린더에 종료된 일정 자동 기록
3. 그러나 zapier가 zap을 다 소진했다고 유료로 바꾸라고 한다.
4. 이 기능이 유료로 월 2만원 씩 쓸 기능은 아닌 것 같다.
5. 스스로 만들어보기로 한다.

+) 그 전날 만들어져야 계획도 같이 사용할텐데 그 부분이 안되어 있다. 그 부분까지 완료해야겠다.

## 구현 기능
- [X] 매일 자정에 6일 뒤 시간별 일지 생성
- [ ] 구글 캘린더에 종료된 일정 자동 기록 

## 서비스 구현
1. notion-api를 활용해서 템플릿 생성
   - notion table을 활용해서 템플릿을 만들어 놓고
   - 그 table에 item을 추가하는 방식
   - jenkins가 자정에 해당 python script 실행
2. google calendar api를 활용해서 event가 종료된 것을 감지하고
   - jenkins가 15분에 한 번씩 종료된 event 감지
3. notion-api를 활용해서 다이어리에 추가


# git convention

### branch
- 브랜치는 기능별로 만들어진다. 
- 모든 기능은 이슈를 기반으로 만들어진다.
- 따라서 branch도 이슈를 포함하여 만든다.
- ex) #7 or #7/extra-branch-name

### commit
- commit은 branch에 종속적으로 만들어진다.
- ex) #7: commit message
- 다만 branch를 만들지 못한 경우 아래와 같이 표현한다.
- ex) #hotfix: commit message

# 실행을 위해서
실행을 위해서는 
.env 파일을 root에 두고 아래 내용을 채워주세요.

```commandline
NOTION_API_KEY = your_api_key
DIARY_DATABASE_ID = your_database_id
DAILY_TASK_DATABASE_ID = your_database_id
```

python 가상환경을 구축하고 실행해주세요.
```python
python -m venv venv 
source ./venv/bin/activate
pip install -r requirements.txt
```