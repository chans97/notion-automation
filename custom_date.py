import datetime

def getCustomToday():
    now = datetime.datetime.now()
    return now.strftime('%Y/%m/%d')

def getNotionToday():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')
