import json
from enum import Enum

import requests


class ObjectType(Enum):
    PAGES = "pages"
    DATABASES = "databases"


def create_object(headers, data, object_type: ObjectType = ObjectType.PAGES) -> requests.Response:
    url = f"https://api.notion.com/v1/{object_type.value}/"
    payload = json.dumps(data)
    res = requests.request("POST", url, headers=headers, data=payload)
    return res
