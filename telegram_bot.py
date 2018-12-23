import telebot

# api: https://core.telegram.org/bots/api/

token = "716597993:AAEbuSasajgXDTLuWfqfelV3GNUOmN1bngs"
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
    user_markup.row('фото', 'аудио', 'документ')
    user_markup.row('стикер', 'видео', 'голос', 'локация')
    bot.send_message(message.from_user.id,"Клавиатура открыта(start)", reply_markup=user_markup)


@bot.message_handler(commands=["hide"])
def handle_hide(message):
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


'''------------------------- обработчики сообщений -------------------------'''
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
    if message.text == "фото":
        # все файлы в директории
        #import os
        #directory = "/Users/misha/Pictures"
        #all_files_in_directory = os.listdir(directory)
        #print(all_files_in_directory)

        # отправка фото по id
        #bot.send_chat_action(message.from_user.id, "upload_photo")
        #bot.send_photo(message.from_user.id, "AgADAgADD6oxGwEY-EihPT1pkb0fguo78w4ABCF4BT8H-55LpwwFAAEC")

        # отправка фото с компьютера
        #image = open("/Users/misha/Pictures/гриффин-супермен.png", 'rb')
        #bot.send_chat_action(message.from_user.id, "upload_photo")
        #bot.send_photo(message.from_user.id, image)
        #image.close()

        # отправка фото по ссылке
        import urllib.request
        URL = "http://goo.gl/58RCFF"
        urllib.request.urlretrieve(URL, 'url-image.jpg')  # сохраняем к себе
        image = open("url-image.jpg", 'rb')
        bot.send_chat_action(message.from_user.id, "upload_photo")
        bot.send_photo(message.from_user.id, image)
        image.close()
    elif message.text == "аудио":
        # отправка аудио с компьютера
        audio = open("/Users/misha/Music/iTunes/iTunes Media/Music/Various Artists/The Best of Absolute Music/01 The Show Must Go on.mp3",'rb')
        bot.send_chat_action(message.from_user.id, "upload_audio")
        bot.send_audio(message.from_user.id, audio)
        audio.close()
    elif message.text == "документ":
        # отправка аудио с компьютера
        document = open("/Users/misha/Documents/megafon_numbers/out.txt",'rb')
        bot.send_chat_action(message.from_user.id, "upload_document")
        bot.send_document(message.from_user.id, document)
        document.close()
    elif message.text == "стикер":
        # отправка стикера по id
        bot.send_sticker(message.from_user.id, "CAADAgADaAMAAkcVaAm3MdIxWFuUjAI")
    elif message.text == "видео":
        # отправка видео с компьютера
        video = open("/Users/misha/Movies/собакен.mp4", 'rb')
        bot.send_chat_action(message.from_user.id, "upload_video")
        bot.send_document(message.from_user.id, video)
        video.close()
    elif message.text == "голос":
        # отправка голосового .ogg сообщения с компьютера
        voice = open("/Users/misha/Music/голосовое.ogg",'rb')
        bot.send_chat_action(message.from_user.id, "upload_audio")
        bot.send_audio(message.from_user.id, voice)
        voice.close()
    elif message.text == "локация":
        bot.send_chat_action(message.from_user.id, "find_location")
        bot.send_location(message.from_user.id, 55.803220, 37.410170)

bot.polling(none_stop=True, interval=0)
