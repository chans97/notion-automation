import json
import requests

from infrastructure.create_object import ObjectType, create_object


def create_page(headers, data=None) -> requests.Response:
    # only for example
    if data is None:
        data = {
            "parent": {"database_id": "${your_data_base_id}"},
            'properties': {
                '날짜': {
                    'type': 'date',
                    'date': {
                        'start': "2023-11-10",
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
                                'content': "2023-11-10",
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
                            'plain_text': "2023-11-10",
                            'href': None
                        }
                    ]
                }
            }
        }

    res = create_object(headers, data, ObjectType.PAGES)
    return res


def read_page(page_id, headers):
    read_url = f"https://api.notion.com/v1/pages/{page_id}"
    res = requests.request("get", read_url, headers=headers)
    data = res.json()
    print(res.status_code)
    print(res.text)
    #
    # with open('full-properties.json', 'w', encoding='utf8') as f:
    #     json.dump(data, f, ensure_ascii=False)
    # return data


def update_page(page_id, headers, update_data):
    update_url = f"https://api.notion.com/v1/pages/{page_id}"
    if update_data is None:
        update_data = {
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": "THIENQCCCCCC"
                            }
                        }
                    ]
                },
                "Text": {
                    "rich_text": [
                        {
                            "text": {
                                "content": "My name is Thienqc"
                            },
                        }
                    ]
                },
                "Checkbox": {
                    "checkbox": False
                },
                "Number": {
                    "number": 2004
                },
                "Select": {
                    "select": {
                        "name": "Mickey",
                    }
                },
                "Multi-select": {
                    "multi_select": [
                        {
                            "name": "Coconut",
                        },
                        {
                            "name": "Banana",
                        }
                    ]
                },
                "Date": {
                    "date": {
                        "start": "2022-08-04",
                        "end": "2022-08-09",
                    }
                },
                "URL": {
                    "url": "ipsum.com"
                },
                "Email": {
                    "email": "thienqc@ipsum.com"
                },
                "Phone": {
                    "phone_number": "32323232"
                },
                "Person": {
                    "people": [
                        {
                            "id": "4af42d2d-a077-4808-b4f7-e960a93fd945",
                        }
                    ]
                },
                "Relation": {
                    "relation": [
                        {
                            "id": "6c320979581b44819d84f941f7eddc41"
                        }
                    ]
                }
            }
        }
    data = json.dumps(update_data)
    response = requests.request("PATCH", update_url, headers=headers, data=data)
    print(response.status_code)


def append_block(block_id, headers, new_block_data=None):
    if new_block_data is None:
        new_block_data = {
            "children": [
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"type": "text", "text": {"content": "Lacinato kale"}}]
                    }
                }
            ]
        }
    url = f"https://api.notion.com/v1/blocks/{block_id}/children"

    data = json.dumps(new_block_data)
    res = requests.request("PATCH", url, headers=headers, data=data)
    print("status_code : ", res.status_code)
