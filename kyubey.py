import logging
import pickle

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler)

from random import choice

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    reply_texts = ['希望你能跟我立下契約，成爲魔法少女！', '與我結成契約吧（◕‿‿◕）', '成爲魔法少女吧！']
    update.message.reply_text(f'嘿～ {update.effective_user.first_name}，{choice(reply_texts)}')

def pixiv(update: Update, context: CallbackContext) -> None:
    with open('artwork_links.pkl', 'rb') as f:
        artwork_links = pickle.load(f)
        msg = choice(artwork_links)
    update.message.reply_text(msg)


def main():
    updater = Updater(
        'TOKEN', use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('pixiv', pixiv))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
