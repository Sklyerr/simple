import wikipedia
import re
from config import API, API_S
import requests
import json


def get_weather(city):
  try:
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    return f"В городе {city.title()}:\nТемпература: {temp}℃\nОщущается: {feels_like}℃\nДавление: {pressure}\nВлажность воздуха: {humidity}\nСкорость ветра: {wind_speed} Км/ч"
  except:
    return "Такого города нет или ты мне пудришь мозги, на попробуй еще раз /weather ток на этот раз что бы все было правильно!"


wikipedia.set_lang("ru")

def getwiki(s):
  """Поиск сообщений в wiki"""
  try:
    ny = wikipedia.page(s)
    wikitext = ny.content[:1000]
    wikimas = wikitext.split(".")
    wikimas = wikimas[:-1]
    wikitext2 = " "
    for x in wikimas:
      if not("==" in x):
        if(len(x.strip())>3):
          wikitext2 = wikitext2+x+"."
      else:
        break
    wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
    wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
    wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
    return wikitext2
  except Exception as e:
    return "Я такого не знаю("
  

def get_gif(gif):
  try:
    if gif.lower() == "гульшат":
      gif = "любовь"
    res = requests.get(f"https://api.giphy.com/v1/stickers/search?api_key={API_S}&q={gif}&limit=25&offset=0&rating=g&lang=ru&bundle=messaging_non_clips")
    datas = json.loads(res.text)
    gif_url = datas["data"][0]["images"]["original"]["url"]
    return gif_url
  except:
    return"Я не смог найти такую картинку попробуй еще раз"