import telebot
import config
import get_zameny
from telebot import apihelper

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_message(message):
    user_murkup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_murkup.row('/check')
    bot.send_message(message.chat.id, 'Выберите действие ...', reply_markup=user_murkup)

@bot.message_handler(commands=['check'])
def send_message(message):
    # from datetime import datetime
    bot.send_message(message.chat.id, get_zameny.get_zameny(get_zameny.get_html('http://uksivt.ru/zameny')))

    # bot.send_message(message.chat.id, "Время и дата на сервере - {0} {1}".format(datetime.now().date().strftime("%d.%m.%Y"), datetime.now().time().strftime("%H:%M")))
    # bot.send_message(message.chat.id, get_weather.get_weather(get_weather.get_html('https://yandex.ru/pogoda/{0}/'.format(cities[message.text]))))

bot.polling(none_stop=True, interval=0)
