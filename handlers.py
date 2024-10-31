
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

import keyboards as kb
from squad import services, vk_book, price_list, text_me_tg, text_me_vk

about = FSInputFile("about.txt")

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name}!',
                         reply_markup=kb.main)
    

@router.message(F.text == 'Услуги')
async def cmd_players(message: Message):
    await message.answer('\n'.join(services), reply_markup=kb.main)


@router.message(F.text == 'Портфолио')
async def cmd_goalkeepers(message: Message):
    await message.answer('\n'.join(vk_book), reply_markup=kb.main)


@router.message(F.text == 'Прайс-лист')
async def cmd_defenders(message: Message):
    await message.answer('\n'.join(price_list), reply_markup=kb.main)
    

@router.message(F.text == 'Написать мне в telegram')
async def cmd_defenders(message: Message):
    await message.answer('\n'.join(text_me_tg), reply_markup=kb.main)


@router.message(F.text == 'Написать мне в vk')
async def cmd_defenders(message: Message):
    await message.answer('\n'.join(text_me_vk), reply_markup=kb.main)


@router.message(F.text == 'Условия выполнения работ')
async def cmd_defenders(message: Message):
    await message.answer_document(about) 
