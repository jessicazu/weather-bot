import os, json, requests, datetime
from requests_oauthlib import OAuth1Session
import random

def update_profile(event, context):
    CK = os.environ["CONSUMER_KEY"]
    CS = os.environ["CONSUMER_SECRET"]
    AT = os.environ["ACCESS_TOKEN"]
    ATS = os.environ["ACCESS_TOKEN_SECRET"]
    twitter = OAuth1Session(CK, CS, AT, ATS)

    weather_data = get_weather()

    weather_id = weather_data["weather"][0]["id"]
    weather_tmp = round(weather_data["main"]["temp"])-273

    update_profile_url = "https://api.twitter.com/1.1/account/update_profile.json"

    now = datetime.datetime.now()
    jst = now + datetime.timedelta(hours=9)
    jst = jst.hour
    n = random.random()
    if 0 < n <= 0.1:
        username = "冨田 一喜"
    elif 0.1 < n <= 0.2:
        username = "とみたかずき"
    elif 0.2 < n <= 0.3:
        username = "とみちゃん"
    elif 0.3 < n <= 0.4:
        username = "とみてぃー"
    elif 0.4 < n <= 0.5:
        username = "かずたん"
    elif 0.5 < n <= 0.6:
        username = "かずたん"
    elif 0.6 < n <= 0.7:
        username = "Tommy"
    elif 0.7 < n <= 0.8:
        username = "トミー"
    elif 0.8 < n <= 0.9:
        username = "Kazuki"
    else:
        username = "エラー"

    if weather_id == 800:
        if jst >= 18 and jst <= 23 or jst >= 0 and jst <= 5:
            username = username + "🌕"
        else:
            username = username + "☀"
    elif weather_id >= 801:
        if jst >= 18 and jst <= 23 or jst >= 0 and jst <= 5:
            username = username + "☁"
        else:
            username = username + "☁"
    elif weather_id >= 802 and weather_id <= 804:
        username = username + "☁"
    elif weather_id >= 300 and weather_id <= 321:
        username = username + "🌂"
    elif weather_id >= 500 and weather_id <= 531:
        username = username + "☔"
    elif weather_id >= 200 and weather_id <= 232:
        username = username + "⚡☔"
    elif weather_id >= 600 and weather_id <= 622:
        username = username + "⛄"
    elif weather_id >= 900:
        username = username + "🌀"

    username = username + str(weather_tmp) + "℃"

    params = {'name': username}

    req = twitter.post(update_profile_url, params = params)
    if req.status_code == 200:
        print ("OK")
    else:
        print ("Error: %d" % req.status_code)

def get_weather():
    KEY = os.environ["WEATHER_API_KEY"]
    id = 1863967 # 福岡市
    weather_url = "http://api.openweathermap.org/data/2.5/weather?id={id}&APPID={key}"
    weather_url = weather_url.format(id = id, key = KEY)
    weather_res = requests.get(weather_url)
    data = json.loads(weather_res.text)
    return data
