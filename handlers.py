import random

from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from config import dp
import  text
import lib

@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}'f'{text.greeting}')

@dp.message_handler(commands=['new_game'])
async def start_nee_game(message: Message):
    lib.new_game()
    if lib.check_game():
        print("Вошел")
        toss = random.randint(0,1)
        if toss:
            await player_turn(message)
        else:
            await bot_turn(message)

async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name},' f' твой ход! Сколько возьмешь конфет?')

@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name
    if lib.check_game():
        if message.text.isdigit():
            take = int(message.text)
            if 0 < take < 29 and take <= lib.get_total():
                lib.take_candies(take)
                if await check_win(message, take, 'player'):
                    return
                await message.answer(text=f'{name}, взял {take} конфет и на столе осталось' 
                                          f'{lib.get_total()}. Твой ход, бот... ')
                await bot_turn(message)
            else:
                await message.answer(text=f'Тут что-то не так! Надо от 1 до 28 и не больше, чем имеется')
        else:
            pass

async def bot_turn(message):
    total = lib.get_total()
    if total <= 28:
        take = total
    else:
        take = random.randint(1, 28)
    lib.take_candies((take))
    await message.answer(text=f'Бот взял {take} конфет, и их осталось {lib.get_total()}')
    if await  check_win(message, take, 'Бот'):
        return
    await  player_turn(message)

async def check_win(message, take: int, player: str):
    if lib.get_total() <= 0:
        if player == 'player':
            await message.answer(f'{message.from_user.first_name} взял {take} конфет и ' 
                                 f'одержал победу над Ботом!')
        else:
            await  message.answer(f'Бот взял {take} конфет и одержал победу!')
        lib.new_game()
        return True
    else:
        return False

# @dp.message_handler(commands=['start'])          # запускает диспатчер через декоратор
# async def on_start(message: Message):            # ответ на команду старт
#     await message.answer(text=f'{message.from_user.first_name}, привет!')
#
# # для примера: ответ на какие-то ключевые слова
# @dp.message_handler(Text(equals='100'))
# async def hundred(message: Message):
#     await message.answer(text=f'Я знаю это число - это сто')
#
# # для примера: ответ на ввод цифр
# @dp.message_handler()  # ловит все, реагирует по условию
# async def digits(message: Message):
#     if message.text.isdigit():
#         await message.answer(text=f'Спасибо! Берем в работу.')
#     else:
#         await message.answer(text=f'С этим невозможно работать!')