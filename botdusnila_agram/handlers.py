from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext

from text import *
from utils import *
from states import Search, Weather, Gif


router = Router()


@router.message(F.content_type == ContentType.NEW_CHAT_MEMBERS)
async def new_members(message : Message):
    """Приветствует новых пользователей"""
    new_member = message.new_chat_members[0]
    await message.answer(f"{WELLCOME_MESSAGE}{new_member.first_name.title()}")


@router.message(Command("help"))
async def help_cmd(message : Message):
    """Команда 'help'"""
    await message.answer(HELP)


@router.message(Command("search"))
async def search_cmd(message : Message, state : FSMContext):
    """Команда 'search'"""
    #Устанавливается состояние "Search.word"
    await state.set_state(Search.word)
    #присылает сообщение о запросе поиска слова
    await message.answer(SEARCH_MESSAGE)


@router.message(Search.word)
async def search_message(message : Message, state : FSMContext):
    """Обрабатывает полученное слово из прошлого состояния"""
    await state.update_data(word = message.text)
    data = await state.get_data()
    await message.answer(getwiki(data["word"]))
    await message.answer(SEARCH_MESSAGE_2)
    await state.clear()


@router.message(Command("weather"))
async def weather_cmd(message : Message, state : FSMContext):
    """Команда weather"""
    await state.set_state(Weather.citys)
    await message.answer(WEATHER_MESSAGE)


@router.message(Weather.citys)
async def weather_message(message : Message, state : FSMContext):
    """Обработка команды weather"""
    await state.update_data(city = message.text)
    data = await state.get_data()
    await message.answer(get_weather(data["city"]))
    await message.answer(WEATHER_MESSAGE_2)
    await state.clear()


@router.message(Command("gif"))
async def gif_cmd(message : Message, state : FSMContext):
    """Команда gif"""
    await state.set_state(Gif.gifs)
    await message.answer(GIF_MESSAGE)


@router.message(Gif.gifs)
async def gif_message(message : Message, state : FSMContext):
    """Обработка команды gif"""
    await state.update_data(gif = message.text)
    data = await state.get_data()
    try:
        await message.answer_animation(get_gif(data["gif"]))
    except:
        await message.answer(get_gif(data["gif"]))
    await message.answer(GIF_MESSAGE_2)
    await state.clear()
