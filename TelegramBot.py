import telebot
from telebot import types
from bot_logic import gen_lot, vin_lot, mon, sm
import time
import requests
import os, random

smile = sm
moneta = mon
admins = ['5736973640']

vin_bil = vin_lot() 
my_bil = gen_lot()
money = mon()
smile = sm()

API_TOKEN = '7831109025:AAEG0Uee-5KkYiJ4foxWcoDRPT2itno-bTM'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, добро пожаловать в бота!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/game")
    item2 = types.KeyboardButton("/work")
    item3 = types.KeyboardButton("/music")
    item4 = types.KeyboardButton("/help")
    item5 = types.KeyboardButton("/image")

    
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)

@bot.message_handler(commands=['help'])
def cmd(message):
    bot.send_message(message.chat.id, '/game (Ответление игрового бота). /work (Ответление рабочего бота).  /music (Ответление музыкального бота) /image (Ответление графического бота)')
    
@bot.message_handler(commands=['game'])
def coin(message):
    bot.send_message(message.chat.id,"Команды: /lot - Лотерея. /smil - Рандомный смайлик. /coin - Рандомная монета.")

@bot.message_handler(commands=['work'])
def coin(message):
    bot.send_message(message.chat.id,"Команды: /musorazlag.")    

@bot.message_handler(commands=['musorazlag'])
def coin(message):
    bot.send_message(message.chat.id, 'А вы знали что это разлагается...')

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Пищевые отходы", callback_data='pish')
    button2 = types.InlineKeyboardButton("Газетная бумага", callback_data='gazet')
    button3 = types.InlineKeyboardButton("Картонные коробки", callback_data='kart')
    button4 = types.InlineKeyboardButton("Бумага", callback_data='bum')
    button5 = types.InlineKeyboardButton("Доски деревянные", callback_data='dosk')
    button6 = types.InlineKeyboardButton("Железная арматура", callback_data='sela')
    button7 = types.InlineKeyboardButton("Железные банки", callback_data='selb')
    button8 = types.InlineKeyboardButton("Старая обувь", callback_data='stob')
    button9 = types.InlineKeyboardButton("Обломки кирпича, бетона", callback_data='oblom')
    button10 = types.InlineKeyboardButton("Автоаккумуляторы", callback_data='avto')
    button12 = types.InlineKeyboardButton("Электрические батарейки", callback_data='batr')
    button13 = types.InlineKeyboardButton("Стекло", callback_data='stek')
    button13 = types.InlineKeyboardButton("Пластиковые бутылки", callback_data='plastbut')



    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button12, button13)
    bot.send_message(message.chat.id, 'Нажмите на кнопку:', reply_markup=markup)
    


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'pish':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагоются до 1 месяца") 

    elif call.data == 'gazet':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагается до 1 года")

    elif call.data == 'kart':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагается до 1 года")

    elif call.data == 'bum':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагается 2 года")

    elif call.data == 'dosk':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагается до 10 лет")

    elif call.data == 'sela':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагается до 10 лет")

    elif call.data == 'selb':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагается до 10 лет")

    elif call.data == 'stob':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагается до 10 лет")

    elif call.data == 'oblom':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагается до 100 лет")

    elif call.data == 'avto':
        bot.answer_callback_query(call.id)   
        bot.send_message(call.message.chat.id, "Разлагается до 100 лет") 

    elif call.data == 'batr':
        bot.answer_callback_query(call.id) 
        bot.send_message(call.message.chat.id, "Разлагается до 100 лет")

    elif call.data == 'stek':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "Разлагается более 1000 лет") 

    elif call.data == 'plastbut':
        bot.answer_callback_query(call.id)  
        bot.send_message(call.message.chat.id, "Разлагается более 100 лет")                           





@bot.message_handler(commands=['coin'])
def coin(message):
    global moneta
    bot.send_message(message.chat.id,"Выбираем рандомную монету...")
    money = mon()
    bot.send_message(message.chat.id,f"Вам выпал(а): {money}")

@bot.message_handler(commands=['smil'])
def smil(message):
    global smile
    bot.send_message(message.chat.id,"Выбираем рандомный смайлик...")
    smile = sm()
    bot.send_message(message.chat.id, f"Вам выпал(а): {smile}")


@bot.message_handler(commands=['lot'])
def lot(message):
    global vin_bil, my_bil
    vin_bil = vin_lot()
    bot.send_message(message.chat.id, 'Выбираем рандомное выигрышное число...')
    bot.send_message(message.chat.id, f"Выигрышное число: {vin_bil}")
    
    my_bil = gen_lot()
    bot.send_message(message.chat.id, f"Ваше число: {my_bil}")
    
    if my_bil == vin_bil: 
        bot.send_message(message.chat.id, "Вы выиграли!")
    else:
        bot.send_message(message.chat.id, "Вы проиграли!")


@bot.message_handler(commands=['music'])
def send_meme(message):
    mus_name = random.choice(os.listdir('music'))
    with open(f'music\{mus_name}', 'rb') as f:
        bot.send_audio(message.chat.id, f)


def get_duck_image_url():    
    url = ' https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
    
@bot.message_handler(commands=['image'])
def duck(message):
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)

    





@bot.message_handler(commands=['kick09'])
def kick_user(message):
    if message.reply_to_message:      
            chat_id = message.chat.id
            user_id = message.reply_to_message.from_user.id  
            user_status = bot.get_chat_member(chat_id, user_id).status 
            if user_status == 'administrator' or user_status == 'creator':
                bot.reply_to(message, "Невозможно кикнуть администратора.")
            else:         
                bot.kick_chat_member(chat_id, user_id)
                bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} был кикнут.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите кикнуть.")   


bot.polling(none_stop=True)

