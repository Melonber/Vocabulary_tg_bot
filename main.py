import telebot
from telebot import types

bot = telebot.TeleBot("6154796253:AAHeLakchnwVCUwoEmhEtkY1FswgREBIlec")


list_aydin_eng = []
list_aydin_chinese = []
list_xinlan_rus = []
list_xinlan_eng = []
list_both = []

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👨艾登")
    btn2 = types.KeyboardButton("👸鑫岚")
    btn3 = types.KeyboardButton("👸👨艾岚")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="你好, {0.first_name}! Lütfen choose комнду".format(
                         message.from_user), reply_markup=markup)

def add_word_to_list(message):
    word = message.text
    list_aydin_eng.append(word)
    bot.send_message(message.chat.id, text=f"Word '{word}' added to list !")

def add_word_to_list_both(message):
    word = message.text
    list_both.append(word)
    bot.send_message(message.chat.id, text=f"Word '{word}' added to list !")

def add_word_to_list_chinese(message):
    word = message.text
    list_aydin_chinese.append(word)
    bot.send_message(message.chat.id, text=f"Word '{word}' added to list !")

def add_word_to_list_eng_xin(message):
    word = message.text
    list_xinlan_eng.append(word)
    bot.send_message(message.chat.id, text=f"Word '{word}' added to list !")

def add_word_to_list_rus_xin(message):
    word = message.text
    list_xinlan_rus.append(word)
    bot.send_message(message.chat.id, text=f"Word '{word}' added to list !")
@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👨艾登"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👨Add 🇬🇧")
        btn2 = types.KeyboardButton("👨List 🇬🇧")
        btn3 = types.KeyboardButton("👨Add 🇨🇳")
        btn4 = types.KeyboardButton("👨List 🇨🇳")
        btn5 = types.KeyboardButton("⬅️Back ⬅️")
        markup.add(btn1, btn2,btn3,btn4,btn5)
        bot.send_message(message.chat.id, text="Lütfen choose комнду", reply_markup=markup)
    elif (message.text == "👨Add 🇬🇧"):
        bot.send_message(message.chat.id, text="Enter the word: ")
        bot.register_next_step_handler(message, add_word_to_list)
    elif (message.text == "👨Add 🇨🇳"):
        bot.send_message(message.chat.id, text="Enter the word: ")
        bot.register_next_step_handler(message, add_word_to_list_chinese)
    elif message.text == "👨List 🇬🇧":
        if list_aydin_eng:
            word_list = '\n'.join(list_aydin_eng)
            bot.send_message(message.chat.id, text=f"List 🇬🇧:\n{word_list}")
        else:
            bot.send_message(message.chat.id, text="Opa. It is empty")
    elif message.text == "👨List 🇨🇳":
        if list_aydin_chinese:
            word_list = '\n'.join(list_aydin_chinese)
            bot.send_message(message.chat.id, text=f"List 🇨🇳:\n{word_list}")
        else:
            bot.send_message(message.chat.id, text="Opa. It is empty")
    elif (message.text == "⬅️Back ⬅️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👨艾登")
        btn2 = types.KeyboardButton("👸鑫岚")
        btn3 = types.KeyboardButton("👸👨艾岚")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Back to menu", reply_markup=markup)

    if (message.text == "👸鑫岚"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👸Add 🇬🇧")
        btn2 = types.KeyboardButton("👸List 🇬🇧")
        btn3 = types.KeyboardButton("👸Add 🇷🇺")
        btn4 = types.KeyboardButton("👸List 🇷🇺")
        btn5 = types.KeyboardButton("⬅️Back ⬅️")
        markup.add(btn1, btn2,btn3,btn4,btn5)
        bot.send_message(message.chat.id, text="Lütfen choose комнду", reply_markup=markup)
    elif (message.text == "👸Add 🇬🇧"):
        bot.send_message(message.chat.id, text="Enter the word: ")
        bot.register_next_step_handler(message, add_word_to_list_eng_xin)
    elif (message.text == "👸Add 🇷🇺"):
        bot.send_message(message.chat.id, text="Enter the word: ")
        bot.register_next_step_handler(message, add_word_to_list_rus_xin)
    elif message.text == "👸List 🇬🇧":
        if list_xinlan_eng:
            word_list = '\n'.join(list_xinlan_eng)
            bot.send_message(message.chat.id, text=f"List 🇬🇧:\n{word_list}")
        else:
            bot.send_message(message.chat.id, text="Opa. It is empty")
    elif message.text == "👸List 🇷🇺":
        if list_xinlan_rus:
            word_list = '\n'.join(list_xinlan_rus)
            bot.send_message(message.chat.id, text=f"List 🇷🇺:\n{word_list}")
        else:
            bot.send_message(message.chat.id, text="Opa. It is empty")
    elif message.text == "👸👨艾岚":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👸👨Add 🇬🇧🇷🇺🇨🇳🇹🇷")
        btn2 = types.KeyboardButton("👸👨List 🇬🇧🇷🇺🇨🇳🇹🇷")
        btn5 = types.KeyboardButton("⬅️Back ⬅️")
        markup.add(btn1, btn2, btn5)
        bot.send_message(message.chat.id, text="Lütfen choose комнду", reply_markup=markup)
    elif (message.text == "👸👨Add 🇬🇧🇷🇺🇨🇳🇹🇷"):
        bot.send_message(message.chat.id, text="Enter the word: ")
        bot.register_next_step_handler(message, add_word_to_list_both)
    elif message.text == "👸👨List 🇬🇧🇷🇺🇨🇳🇹🇷":
        if list_both:
            word_list = '\n'.join(list_both)
            bot.send_message(message.chat.id, text=f"List 🇬🇧🇷🇺🇨🇳🇹🇷:\n{word_list}")
        else:
            bot.send_message(message.chat.id, text="Opa. It is empty")

bot.polling(none_stop=True)
