import telebot
from consts import TOKEN, HELP_INFO
import textmaker

bot = telebot.TeleBot(TOKEN)
model = textmaker.create_model()

@bot.message_handler(commands=['start',])
def send_welcome(message):
    bot.reply_to(message, 'Привет!')

@bot.message_handler(regexp='историю')
@bot.message_handler(commands=['story'])
def tell_story(message):
    story = textmaker.create_text(model)
    bot.send_message(message.chat.id, story)

@bot.message_handler(commands=['help'])
@bot.message_handler(regexp='умеешь')
@bot.message_handler(regexp='помощь')
def send_help(message):
    bot.send_message(message.chat.id, HELP_INFO)

bot.polling()
