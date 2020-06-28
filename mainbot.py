import telebot
from consts import TOKEN
import textmaker

bot = telebot.TeleBot(TOKEN)
model = textmaker.create_model()

@bot.message_handler(commands=['start',])
def send_welcome(message):
    bot.reply_to(message, 'Привет!')

@bot.message_handler(commands=['story'])
def echo_all(message):
    story = textmaker.create_text(model)
    bot.reply_to(message, story)

bot.polling()
