import telebot
import random
import time

bot = telebot.TeleBot('Ваш API') #Вставьте сюда ваш API ключ полученный в @BotFather 

# Команда /start

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, скинь мне любую фотку')

# Фото и компилмент в зависимости от рандома

@bot.message_handler(content_types=['photo'])
def user_photo(message):
    randomm = random.randint(1,3)
    time.sleep(1)
    if randomm == 1:
        bot.send_message(message.chat.id, 'Какое красивое фото😍')
    elif randomm == 2:
        bot.send_message(message.chat.id, 'Это очень красиво..')
    elif randomm == 3:
        bot.send_message(message.chat.id, 'Запредельная красота')
    else:
        bot.send_message(message.chat.id, 'Помоему это не фото')

bot.infinity_polling()