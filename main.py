from dotenv import dotenv_values
from notion_client import Client
from notion_interface import *

# notion api 초기화
config = dotenv_values(".env")
notion_secret = config.get('NOTION_API_KEY')
notion = Client(auth=notion_secret)
headers = {
    "Authorization": "Bearer " + notion_secret,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

DAILY_TASK_DATABASE_ID = config.get('DAILY_TASK_DATABASE_ID')


def main():
    create_daily_task(DAILY_TASK_DATABASE_ID, headers, "오전")
    create_daily_task(DAILY_TASK_DATABASE_ID, headers, "오후 전반")
    create_daily_task(DAILY_TASK_DATABASE_ID, headers, "오후 후반")
    create_daily_task(DAILY_TASK_DATABASE_ID, headers, "야간 전반")
    create_daily_task(DAILY_TASK_DATABASE_ID, headers, "야간 후반")


if __name__ == "__main__":
    main()
