
from dotenv import dotenv_values
from notion_client import Client
from notion_interface import readDatabase, createTodayDiary

# 초기화
config = dotenv_values(".env")
notion_secret = config.get('NOTION_API_KEY')
notion = Client(auth=notion_secret)
headers = {
    "Authorization": "Bearer " + notion_secret,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}
db_id = config.get('DATABASE_ID')


def main():
    print("start")
    createTodayDiary(db_id, headers)
    print("end")


if __name__ == "__main__":
    main()
