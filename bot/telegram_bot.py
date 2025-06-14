import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from django.conf import settings
from django.core.wsgi import get_wsgi_application
import os
import sys
from asgiref.sync import sync_to_async


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
application = get_wsgi_application()

from core.models import CustomUser  

logging.basicConfig(level=logging.INFO)

@sync_to_async
def get_or_create_user(telegram_id, telegram_username):
    user, created = CustomUser.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={
            "username": telegram_username or f"user{telegram_id}",
            "telegram_username": telegram_username or "",
            "email": f"{telegram_username or 'user'}@telegram.fake"
        }
    )
    if user.telegram_username != telegram_username:
        user.telegram_username = telegram_username or ""
        user.save()
    return user, created

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    telegram_id = user.id
    telegram_username = user.username

    await get_or_create_user(telegram_id, telegram_username)

    await update.message.reply_text(f"Welcome, {telegram_username or 'User'}! You're registered.")


def run_bot():
    print("Starting bot...")
    app = ApplicationBuilder().token("8112220603:AAEM5As62gvp8WEZVq0NcipcaCRpnE1K7RI").build()

    app.add_handler(CommandHandler("start", start))
    try:
        app.run_polling()
    except Exception as e:
        print(f"Bot crashed: {e}")

if __name__ == "__main__":
    run_bot()
