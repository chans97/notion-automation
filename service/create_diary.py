import json

import requests

from common.custom_date import get_custom_tomorrow
from infrastructure.page_interface import create_page


def create_today_diary(database_id, headers):
    custom_date_text = get_custom_tomorrow('%Y/%m/%d')
    notion_date_text = get_custom_tomorrow('%Y-%m-%d')

    data = {
        "parent": {"database_id": database_id},
        'properties': {
            '날짜': {
                'type': 'date',
                'date': {
                    'start': notion_date_text,
                    'end': None,
                    'time_zone': None
                }
            },
            '이름': {
                'id': 'title',
                'type': 'title',
                'title': [
                    {
                        'type': 'text',
                        'text': {
                            'content': custom_date_text,
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
                        'plain_text': custom_date_text,
                        'href': None
                    }
                ]
            }
        }
    }

    res = create_page(headers, data)
    print("status_code : ", res.status_code)
