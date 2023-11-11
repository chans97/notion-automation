import json

import requests

from infrastructure.create_object import create_object, ObjectType


def create_database(headers, data=None) -> requests.Response:
    # only for example
    if data is None:
        data = {
            "parent": {
                "type": "page_id",
                "page_id": "${your_page_id}"
            },
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Grocery List",
                        "link": None
                    }
                }
            ],
            "properties": {
                "Name": {
                    "title": {}
                },
                "Description": {
                    "rich_text": {}
                },
                "In stock": {
                    "checkbox": {}
                }
            }
        }

    res = create_object(headers, data, ObjectType.DATABASES)
    print("status_code : ", res.status_code)
    return res


def read_database(database_id, headers):
    read_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    res = requests.request("POST", read_url, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('../full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data['results'][0]
