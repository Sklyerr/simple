from aiogram.fsm.state import StatesGroup, State


class Search(StatesGroup):
    word = State()


class Weather(StatesGroup):
    citys = State()


class Gif(StatesGroup):
    gifs = State()