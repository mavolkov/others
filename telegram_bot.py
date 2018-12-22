import telebot

token = "PUT_YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(token)

# bot.send_message(976475, "test from pycharm")

#upd = bot.get_updates()          # все обновления в список
#last_upd = upd[-1]            # последнее обновление
#print(last_upd.message)
#print(last_upd.message.text)







'''----------------------- клавиатура показать/скрыть -----------------------'''

@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False) # (автомасштаб, исчезнет после нажатия)
    user_markup.row('/start', '/hide')
    user_markup.row('фото', 'аудио', 'документы')
    user_markup.row('стикер', 'видео', 'голос', 'локация')
    bot.send_message(message.from_user.id,"Клавиатура открыта(start)", reply_markup=user_markup)


@bot.message_handler(commands=["hide"])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id,"Клавиатура закрыта(hide)", reply_markup=hide_markup)



'''------------------------ для записи лога  ------------------------'''

print(bot.get_me())  # пишет инфо о боте

def log(message, answer):
    print("-----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст: {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))


'''------------------------- обработчики команд -------------------------'''
# используем декораторы
# следующая дальше функция должна быть вызвана, когда боту приходит сообщение с подходящим типом содержимого
# сообщение будет обработано только в одном декореторе(в первом, для которого подошел тип сообщения)

@bot.message_handler(content_types="command")
def handle_command(message):
    bot.send_message(message.from_user.id, "Пришла команда для бота")


@bot.message_handler(content_types="document")
def handle_document(message):
    bot.send_message(message.from_user.id, "Пришел документ")


@bot.message_handler(content_types="audio")
def handle_audio(message):
    bot.send_message(message.from_user.id, "Пришла аудиозапись")


@bot.message_handler(content_types="photo")
def handle_photo(message):
    bot.send_message(message.from_user.id, "Пришло изображение")


@bot.message_handler(content_types="sticker")
def handle_sticker(message):
    bot.send_message(message.from_user.id, "Пришел стикер")


@bot.message_handler(content_types="text")
def handle_text(message):
    bot.send_message(message.from_user.id, "Получен текст: " + message.text)
    answer = "Получен текст: " + message.text
    log(message,answer)


bot.polling(none_stop=True, interval=0)
