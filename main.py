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

def content(update, context):
    update.message.reply_text(
        """
        i am an AI/ML engineer
"""
    )

def contact(update, context):
    update.message.reply_text(
        """
        ph:9043450829
        mail:maha@gmail.com
"""
    )

def handle_meaasage(update, context):
    update.message.reply_text(f"you said {update.message.text}")



updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('help', helps))
dispatch.add_handler(telegram.ext.CommandHandler('content', content))
dispatch.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_meaasage))



updater.start_polling()
updater.idle()

