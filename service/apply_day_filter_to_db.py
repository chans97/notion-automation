import requests


def apply_day_filter_to_db(database_id, headers):
    # 필터 조건
    filter_params = {
        "filter": {
            "property": "날짜",  # "날짜" 필드의 이름 (본인의 데이터베이스 필드에 맞게 변경)
            "date": {
                "equals": "2023-11-11"  # 필터 조건에 맞는 날짜 (본인의 필터 조건에 맞게 변경)
            }
        }
    }

    # API 요청
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    response = requests.post(url, headers=headers, json=filter_params)

    # 응답 확인
    data = response.json()
    print(data)
