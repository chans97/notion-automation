import datetime

def getCustomToday(dateFormat):
    now = datetime.datetime.now()
    return now.strftime(dateFormat)

def getCustom6dayLater(dateFormat):
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=6)
    return tomorrow.strftime(dateFormat)
    # return tomorrow.strftime('%Y-%m-%d')
#
# def getNotionToday():
#     now = datetime.datetime.now()
#     return now.strftime('%Y-%m-%d')
#
# def getNotionTomorrow():
#     now = datetime.datetime.now()
#     tomorrow = now + datetime.timedelta(days=1)
#     return tomorrow.strftime('%Y-%m-%d')