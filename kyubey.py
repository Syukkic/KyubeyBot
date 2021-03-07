import logging
import pickle

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler)

from random import randint

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        f'嘿～ {update.effective_user.first_name}，希望你能跟我立下契約，成爲魔法少女！')


def pixiv(update: Update, context: CallbackContext) -> None:
    with open('artwork_links.pkl', 'rb') as f:
        artwork_links = pickle.load(f)
        rand_num = randint(0, len(artwork_links)-1)
        msg = artwork_links[rand_num]
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
