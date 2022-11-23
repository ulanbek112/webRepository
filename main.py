import telebot

bot = telebot.TeleBot('5804912391:AAFPWbxPKBeY1mH5xwmr5xU5eeP0kwCTPiU')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Кандайсын":
        bot.send_message(message.chat.id, "Жакшы озун кандайсын", parse_mode='html')
    elif message.text == "Каяктасын":
        bot.send_message(message.chat.id, "Мен Бишкектемин")
    elif message.text == "Эмне кылып жатасын Бишкекте":
        bot.send_message(message.chat.id, "IT Курста окуп жатамын")
    elif message.text == "Сурот жонотчу":
        photo = open('jpg.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "ар кандай создорду жазып башым оорутпа", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Вау Сонун сурот экен!")


#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Сайтка кируу", url="https://www.instagram.com/_solih_kg_?r=nametag"))
#     bot.send_message(message.chat.id, 'Сайтка кириниз', reply_markup=markup)


bot.polling(none_stop=True)
