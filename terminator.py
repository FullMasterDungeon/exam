import telebot
count = 0
fist = ['e', 'y', 'u', 'i', 'o', 'a']

bot = telebot.TeleBot('1751556596:AAGYxFmWp89tI6YETxtr8DDTd9LvXUd6DOw')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    count = 0
    atext = message.text.lower()
    for i in atext:
        for b in fist:
            if i == b:
                count += 1
    bot.send_message(message.chat.id, count)
    сount = 0
bot.polling()
