import telebot
import os
from dotenv import load_dotenv
load_dotenv(os.path.join("~/PycharmProjects/untitled4", '.env'))
print(load_dotenv())
TOKEN = os.environ.get('TOKEN')
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN",TOKEN)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row("course1","course2",'course3')

@bot.message_handler(commands=['start'])
def start_message(message):
    text = open('text.txt', 'r')
    bot.send_message(message.chat.id, text,reply_markup=keyboard1)
    text.close()


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'hi':
        bot.send_message(message.chat.id, 'hello')
    elif message.text.lower() == "who is your creator?":
        bot.send_message(message.chat.id, 'YOU')
    elif message.text.lower().startswith("course"):
        number = message.text[-1]
        text = open('course' + str(number) + '.txt', 'r')
        bot.send_message(message.chat.id, text)
    elif message.text.lower().startswith("apply"):
        reply_text = "welcome to our courses"
        bot.send_message(message.chat.id, reply_text)
        app_name = message.text.lower()
        application = open('applicants.txt','a+')
        application.write(app_name + "\n")
        application.close()
    else:
        simple_text=message.text[:3]+' ' + message.text.lower()
        bot.send_message(message.chat.id, simple_text)


bot.polling()