from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters # type: ignore
import logging

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Стартовая команда
async def start(update: Update, context):
    # Ссылка на ваше веб-приложение
    web_app_url = "https://demansion.github.io/OnyxGame/"  # Замените на URL вашего веб-приложения

    keyboard = [
        [InlineKeyboardButton("Играть", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Нажмите кнопку, чтобы начать игру:", reply_markup=reply_markup)

# Обработчик получения данных от веб-приложения
async def handle_web_app_data(update: Update, context):
    # Получаем данные от веб-приложения
    data = update.message.web_app_data.data
    await update.message.reply_text(f"Ты набрал {data['score']} очков!")

# Основная функция
def main():
    # Токен бота
    TOKEN = "7139113186:AAH0SuQp33sA0Wrif-kUc1OVczfAW1TZ58Y"  # Замените на ваш токен

    # Создаем приложение Telegram
    application = Application.builder().token(TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_web_app_data))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
