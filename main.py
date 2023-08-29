
from dotenv import dotenv_values
from notion_client import Client
from notion_interface import readDatabase, createTodayDiary

# notion api 초기화
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
    createTodayDiary(db_id, headers)


if __name__ == "__main__":
    main()
