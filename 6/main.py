import telebot
import os , random

images = os.listdir('images')

bot = telebot.TeleBot("")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    image = random.choice(images)
    with open(f'images/{image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

bot.polling()
