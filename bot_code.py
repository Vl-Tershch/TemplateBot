import telebot

bot = telebot.TeleBot("ВАШ ТОКЕН")

@bot.message_handler(content_types=['text'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне, но пока я ничего не умею. /start')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    print('Пришло простое сообщение!')

bot.polling(none_stop=True, interval=0)

