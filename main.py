import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("Hi, Welcome to Raja bot")

def helps(update, context):
    update.message.reply_text(
        """
        Hi, i'm telegram bot created by Raja. pls follow these commands:-
        /start - to start the conversation
        /content - Information about AI/ML
        /contact - Information about contact me
        /help - to get this help menu
        I hope this helps:)

"""
    )


updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('help', helps))


updater.start_polling()
updater.idle()

