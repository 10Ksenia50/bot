import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7640887728:AAF4-NQ14ufDYPJRon-6VZaW_s9mqseemko"

# Налаштовуємо логування
logging.basicConfig(level=logging.INFO)

# Створюємо об'єкти бота і диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Створюємо клавіатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("💙 Підтримка"))
keyboard.add(KeyboardButton("🧘 Дихальна практика"), KeyboardButton("📖 Корисні матеріали"))

# Оновлений обробник команди /start
@dp.message_handler(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привіт! Я бот психологічної підтримки. Обери, що тобі потрібно:", reply_markup=keyboard)

# Додаємо обробку кнопок
@dp.message_handler(lambda message: message.text == "💙 Підтримка")
async def support_handler(message: types.Message):
    await message.answer("Я тут, щоб тебе підтримати! Напиши, що тебе турбує.")

@dp.message_handler(lambda message: message.text == "🧘 Дихальна практика")
async def breathing_handler(message: types.Message):
    await message.answer("Спробуй цю просту техніку:\n1️⃣ Вдихай на 4 секунди\n2️⃣ Затримай дихання на 4 секунди\n3️⃣ Видихай на 4 секунди\n4️⃣ Повтори 5 разів.")

@dp.message_handler(lambda message: message.text == "📖 Корисні матеріали")
async def materials_handler(message: types.Message):
    await message.answer("Ось кілька корисних статей:\n📌 Як боротися зі стресом: [посилання]\n📌 Методи релаксації: [посилання]")

# Відповідь на будь-яке повідомлення
@dp.message_handler()
async def echo_handler(message: types.Message):
    response = get_psychological_response(message.text)
    await message.answer(response)

def get_psychological_response(text):
    """Проста логіка відповідей"""
    keywords = {
        "стрес": "Спробуй зробити глибокий вдих і видих. Дихальні практики допомагають знизити рівень стресу.",
        "тривога": "Тривога – це нормально. Спробуй зосередитися на теперішньому моменті.",
        "депресія": "Ти не один. Якщо тобі дуже важко, можливо, варто звернутися до спеціаліста.",
        "самотність": "Ти важливий! Поговори з друзями чи сім’єю, це може допомогти."
    }
    
    for word, response in keywords.items():
        if word in text.lower():
            return response
    return "Я тут, щоб підтримати тебе. Напиши, що тебе турбує 💙"



# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
