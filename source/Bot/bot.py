import config
import telebot
from requests import get


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я подопытный бот, который кое что могу делать")

@bot.message_handler(func=lambda message: True)
def any_message(message):
    bot.reply_to(message, "Сам {!s}".format(message.text))


@bot.edited_message_handler(func=lambda message: True)
def edit_message(message):
    bot.edit_message_text(chat_id=message.chat.id,
                          text="Сам {!s}".format(message.text),
                          message_id=message.message_id + 1)

if __name__ == '__main__':
     bot.infinity_polling()