import json
import requests

from common.custom_date import get_custom_later_day
from infrastructure.page_interface import create_page


def create_daily_task(database_id, headers, time):
    notion_date_text = get_custom_later_day(days=6)
    data = {
        "parent": {
            "database_id": database_id
        },
        "properties": {
            '기록': {
                'id': 'title',
                'type': 'title',
                'title': [
                    {
                        'type': 'text',
                        'text': {
                            'content': notion_date_text,
                            'link': None
                        },
                        'annotations': {
                            'bold': False,
                            'italic': False,
                            'strikethrough': False,
                            'underline': False,
                            'code': False,
                            'color': 'default'
                        },
                        'plain_text': notion_date_text,
                        'href': None
                    }
                ]
            },
            "시간대": {
                "select": {
                    "name": time
                }
            },
            "날짜": {
                "date": {
                    "start": notion_date_text
                }
            },
            "계획": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "[계획] ",
                        }
                    }
                ]
            },
            "실제": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "[실제] ",
                        }
                    }
                ]
            }
        }
    }

    res = create_page(headers, data)
    print("status_code : ", res.status_code)
    print("날짜 : ", notion_date_text)
    print("시간대 : ", time)
