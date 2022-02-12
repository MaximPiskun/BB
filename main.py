import telebot
import random
API_TOKEN = ''

START_STICKER = 'CAACAgIAAxkBAAIEvV9Ds7W8VKOrK6IEyAuRI58nk2TgAAJnAAOWn4wOyQZnzEHbDU8bBA'  # @Stiker_id_bot поможет
WIN_STICKER = 'CAACAgIAAxkBAAIEm19DsoNP3CcnnfOl6nTT6GNFzHhoAAJAAAOvxlEaV1XfcKI2zaobBA'
RIGHT_ANSWER = 5

bot = telebot.TeleBot(API_TOKEN)
def generation_level1():
    k = random.randint(1,10)
    oper = random.randint(1,3)
    beg = random.randint(-10,10)
    if oper ==1:
        print(beg)
        for i in range (5):
            beg = beg + k
            print(beg)
    if oper == 2:
        print(beg)
        for i in range(5):
            beg = beg - k
            print(beg)
    if oper == 3:
        print(beg)
        for i in range(5):
            beg = beg * k
            print(beg)
def generation_level2():

class BaseClass:
	def __init__(self, data):
		self.data = data


	def make_smth(self):
		pass



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, START_STICKER)
    bot.send_message(message.from_user.id, "Привет, твоя задача продолжить последовательность чисел. Выбери сложность: ")


@bot.message_handler(content_types=['text'])
def start(message):
    try:
        input = int(message.text)
        output = str(input * 2 + 1)
        bot.send_message(message.from_user.id, output)
        if output == RIGHT_ANSWER:
            bot.send_sticker(message.chat.id, WIN_STICKER)
    except ValueError:
        bot.send_message(message.from_user.id, "Понимаю только целые числа")







@bot.message_handler(content_types=['voice'])
def start_message(message):
    bot.send_message(message.from_user.id, "Не слышуууу. Ничего не слышу. Глуховат я :(")


@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_message(message.from_user.id, "Картинки какие-то шлют. Ничего не понимаю...")


@bot.message_handler(content_types=['document'])
def start_message(message):
    bot.send_message(message.from_user.id, "Ой, вот только файлы мне тут не надо слать!")


bot.polling()