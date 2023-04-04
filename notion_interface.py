import json
import requests
from custom_date import getCustomToday, getNotionToday

def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data['results'][0]


# 나중에 page 만드는 reference로 남기기 위해서 삭제하지 않고 그대로 둠
# Create a Page
def createPage(databaseID, headers):
    custom_date_text = getCustomToday()
    notion_date_text = getNotionToday()

    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": { "database_id": databaseID },
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
    custom_date_text = getCustomToday()
    notion_date_text = getNotionToday()

    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": { "database_id": databaseID },
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


