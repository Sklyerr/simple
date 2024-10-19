import telebot
import wikipedia
import re
import requests
import json

wikipedia.set_lang("ru")

token = "6349076340:AAEBn7Th8YVR5D-NIqjnLYZpYJwk-IhRmF4"

bot = telebot.TeleBot(token)

CHNL = "@test999756"
API = "9d9bdfa02b21d17b02cc511b105a809a"
API_S = "EaXtRiZKhNlUjPv6cB2GvEnNGb9vELuB"

HELP = """
/help - Напишу что умею делать.
/search - Раскажу о чем попросишь.
/weather - Прогноз погоды от душнилы.
/gif - отправляет рандомную гифку."""



def getwiki(s):
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



@bot.message_handler(content_types = ["new_chat_members"])
def new_member(message):
  name = message.new_chat_members[0].first_name
  bot.send_message(CHNL, f"Добро пожаловать в группу, {name.title()}!☺️")

@bot.message_handler(commands = ["help"])
def help_message(message):
  bot.delete_message(CHNL, message.message_id)
  bot.send_message(CHNL, HELP)

@bot.message_handler(commands = ["search"])
def search_message(message):
  bot.delete_message(CHNL, message.message_id)
  message = bot.send_message(CHNL, "Про что хочешь узнать?")
  bot.register_next_step_handler(message, wiki_search)

def wiki_search(message):
  bot.send_message(CHNL, getwiki(message.text))
  bot.send_message(CHNL, "Если еще что то надо пиши:  /search, если нет то занимайся своими делами")


@bot.message_handler(commands=['weather'])
def message_weather(message):
  bot.delete_message(CHNL, message.message_id)
  message = bot.send_message(CHNL, "ВВедите город:")
  bot.register_next_step_handler(message, get_weather)

def get_weather(message):
  try:
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    bot.send_message(CHNL, f"В городе {city.title()}:\nТемпература: {temp}℃\nОщущается: {feels_like}℃\nДавление: {pressure}\nВлажность воздуха: {humidity}\nСкорость ветра: {wind_speed} Км/ч")
  except:
    bot.send_message(CHNL, "Такого города нет или ты мне пудришь мозги, на попробуй еще раз /weather ток на этот раз что бы все было правильно!")


@bot.message_handler(commands = ["gif"])
def message_gif(message):
  bot.delete_message(CHNL, message.message_id)
  message = bot.send_message(CHNL, "На какое слово нужен стик?")
  bot.register_next_step_handler(message, get_gif)

def get_gif(message):
  try:
    if message.text.lower() == "гульшат":
      gif = "любовь"
    else:
      gif = message.text.strip()
    res = requests.get(f"https://api.giphy.com/v1/stickers/search?api_key={API_S}&q={gif}&limit=25&offset=0&rating=g&lang=ru&bundle=messaging_non_clips")
    datas = json.loads(res.text)
    gif_url = datas["data"][0]["images"]["original"]["url"]
    bot.send_document(CHNL, gif_url)
  except:
    bot.send_message(CHNL, "Я не смог найти такую картинку попробуй еще раз /gif")


bot.infinity_polling()