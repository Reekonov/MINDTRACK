from telegram.ext import ApplicationBuilder
from handlers import register_handlers
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if __name__ == "__main__":
    if not BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN не найден в .env!")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    register_handlers(app)
    print("Бот запущен!")
    app.run_polling()
