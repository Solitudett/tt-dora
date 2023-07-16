from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']
ttbirthday = os.environ['TTBIRTHDAY']
kaoyandate = os.environ['KAOYANDATE']
chabendate = os.environ['CHABENDATE']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


def get_weather():
    # url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
    # res = requests.get(url).json()
    # weather = res['data']['list'][0]
    # return weather['weather'], math.floor(weather['temp'])
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['temp']), math.floor(weather['high']), math.floor(weather['low'])

def get_count():
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


def get_birthday():
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


def get_ttbirthday():
    next1 = datetime.strptime(str(date.today().year) + "-" + ttbirthday, "%Y-%m-%d")
    if next1 < datetime.now():
        next1 = next1.replace(year=next1.year + 1)
    return (next1 - today).days


def get_kaoyandate():
    next2 = datetime.strptime(str(date.today().year) + "-" + kaoyandate, "%Y-%m-%d")
    if next2 < datetime.now():
        next2 = next2.replace(year=next2.year + 1)
    return (next2 - today).days


def get_chabendate():
    next3 = datetime.strptime(str(date.today().year) + "-" + chabendate, "%Y-%m-%d")
    if next3 < datetime.now():
        next3 = next3.replace(year=next3.year + 1)
    return (next3 - today).days


def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
# wea,temperature = get_weather()
wea, temperature, highest, lowest = get_weather()
# data = {"weather": {"value": wea}, "temperature": {"value": temperature}, "love_days": {"value": get_count()},
#         "birthday_left": {"value": get_birthday()}, "ttbirthday_left": {"value": get_ttbirthday()},
#         "kaoyan_date": {"value": get_kaoyandate()}, "chaben_date": {"value": get_chabendate()},
#         "words": {"value": get_words(), "color": get_random_color()}}
data = {"weather":{"value":wea,"color":get_random_color()},"temperature":{"value":temperature,"color":get_random_color()}, "love_days": {"value": get_count()},
        "birthday_left": {"value": get_birthday()}, "ttbirthday_left": {"value": get_ttbirthday()},
        "kaoyan_date": {"value": get_kaoyandate()}, "chaben_date": {"value": get_chabendate()},
        "words": {"value": get_words(), "color": get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
