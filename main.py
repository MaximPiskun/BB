import telebot
import random
API_TOKEN = ''

START_STICKER = 'CAACAgIAAxkBAAIEvV9Ds7W8VKOrK6IEyAuRI58nk2TgAAJnAAOWn4wOyQZnzEHbDU8bBA'  # @Stiker_id_bot поможет
WIN_STICKER = 'CAACAgIAAxkBAAIEm19DsoNP3CcnnfOl6nTT6GNFzHhoAAJAAAOvxlEaV1XfcKI2zaobBA'
RIGHT_ANSWER = 5

bot = telebot.TeleBot('')
controller = {}

button_1 = types.KeyboardButton('легкий')
button_2 = types.KeyboardButton('средний')
button_3 = types.KeyboardButton('сложный')
ans_kb = types.ReplyKeyboardMarkup()
ans_kb.add(button_1).add(button_2).add(button_3)




bot = telebot.TeleBot(API_TOKEN)
def generation_level1():
    k = random.randint(1,10)
    oper = random.randint(1,3)
    beg = random.randint(-10,10)
    mass = []
    if oper == 1:
        mass.append(beg)
        for i in range (5):
            beg = beg + k
            mass.append(beg)
    if oper == 2:
        mass.append(beg)
        for i in range(5):
            beg = beg - k
            mass.append(beg)
    if oper == 3:
        mass.append(beg)
        for i in range(5):
            beg = beg * k
            mass.append(beg)
    return mass


def generation_level2():
    print("---")
def generation_level3():
    print("---")
class Singleton:
   __instance = None

   def __init__(self, prop):
     self.some_property = prop

   @classmethod
   def get_instance(cls):
       if not cls.__instance:
           cls.__instance = Singleton()
       return cls.__instance


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, START_STICKER)
    bot.send_message(message.from_user.id, "Привет, твоя задача продолжить последовательность чисел. Выбери сложность: ", reply_markup=kb.ans_kb)
    user_choice = message.from_user.id
    controller[user_id] = 'start'
def BB_bot(user_id, user_choice):
    if user_choice == "легкий":
        controller[user_id] = 'start'
        cont =generation_level1()
        return cont
    elif user_choice == "средний":
        controller[user_id] = 'start'
        cont = generation_level2()
        return cont
    elif user_choice == "сложный":
        controller[user_id] = 'start'
        cont generation_level3()
        return cont
    else:
        controller[user_id] = 'start'
        return "ERROR"
    z = Singleton.get_instance(BB_bot(user_id, user_choice))
    for i in range (5):
        print(z[0], end = " ")
    RIGHT_ANSWER = z[5]
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