from aiogram import  executor
from handlers import dp # импортируем из хендлерс, а не из конфиг!
async def on_startup(_):
    print("Бот запущен")


if __name__ == '__main__':             #   принимает команду, пойманную диспатчером,  skip_updates=True -
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)   #  пропускает все команды, отправленные боту,
                                                                           #   когда тот был в отключке