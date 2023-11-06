import json
import requests
from custom_date import getCustom6dayLate


def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data['results'][0]


def readPage(pageId, headers):
    readUrl = f"https://api.notion.com/v1/pages/{pageId}"
    res = requests.request("get", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data




def appendBlock(blockId, headers):
    url = f"https://api.notion.com/v1/blocks/{blockId}/children"
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
    data = json.dumps(new_block_data)
    res = requests.request("PATCH", url, headers=headers, data=data)
    print("status_code : ", res.status_code)


def create_daily_task(database_id, headers, time):
    notion_date_text = getCustom6dayLater('%Y-%m-%d')
    url = 'https://api.notion.com/v1/pages'
    payload = json.dumps({
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
            }
        }
    })

    res = requests.request("POST", url, headers=headers, data=payload)
    print("status_code : ", res.status_code)
    print("날짜 : ", notion_date_text)
    print("시간대 : ", time)

def create_database(page_id, headers):

    url = 'https://api.notion.com/v1/databases/'
    payload = json.dumps({
        "parent": {
            "type": "page_id",
            "page_id": page_id
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
    })
    res = requests.request("POST", url, headers=headers, data=payload)
    print("status_code : ", res.status_code)

# 나중에 page 만드는 reference로 남기기 위해서 삭제하지 않고 그대로 둠
# Create a Page
def createPage(databaseID, headers):
    custom_date_text = getCustomTomorrow('%Y/%m/%d')
    notion_date_text = getCustomTomorrow('%Y-%m-%d')

    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": {"database_id": databaseID},
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
    data = json.dumps(newPageData)
    res = requests.request("POST", createUrl, headers=headers, data=data)
    print("status_code : ", res.status_code)


# Update a Page
pageID = "--> page ID <--"


def updatePage(pageID, headers):
    updateUrl = f"https://api.notion.com/v1/pages/{pageID}"
    updateData = {
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
    data = json.dumps(updateData)
    response = requests.request("PATCH", updateUrl, headers=headers, data=data)
    print(response.status_code)


################ 아래부터는 목적에 맞게 커스텀 ######################

def createTodayDiary(databaseID, headers):
    custom_date_text = getCustomTomorrow('%Y/%m/%d')
    notion_date_text = getCustomTomorrow('%Y-%m-%d')

    create_url = 'https://api.notion.com/v1/pages'
    new_page_data = {
        "parent": {"database_id": databaseID},
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
    data = json.dumps(new_page_data)
    res = requests.request("POST", create_url, headers=headers, data=data)
    print("status_code : ", res.status_code)
