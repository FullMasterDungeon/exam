import telebot
count = 0
fist = {'e' : 0, 'y' : 0, 'u' : 0, 'i' : 0, 'o' : 0, 'a' : 0}

bot = telebot.TeleBot('1751556596:AAGYxFmWp89tI6YETxtr8DDTd9LvXUd6DOw')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    atext = message.text.lower()
    for i in atext:
        for a, b in fist.items():
            if i == a:
                fist[i] += 1
    for i, b in fist.items():
        bot.send_message(message.chat.id, f"{i} повторяется {b} раз")
        fist[i] = 0
bot.polling()
