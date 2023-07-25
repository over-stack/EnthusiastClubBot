import os
import asyncio
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import aiogram.utils.markdown as md
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from config import API_TOKEN, DB_FILENAME
from db_map import Base, Vacancies, Resumes, Responses, Tags, VacanciesTags, ResumesTags

# Configure logging
logging.basicConfig(level=logging.INFO)

# Connect DB
engine = create_engine(f'sqlite:///{DB_FILENAME}')

# If there is no DB then we make it
if not os.path.isfile(f'./{DB_FILENAME}'):
    Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class VacResChoice(State):
    VacResChoice = State()


class ResumeForm(StatesGroup):
    name = State()
    title = State()
    description = State()


@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Привет!\n" +
                        "Я - бот, предназначенный для поиска единомышленников!\n" +
                        "Здесь ты можешь найти команду для своего проекта или же присоединиться к уже " +
                        "имеющейся команде!")


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)