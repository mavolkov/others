import telebot

token = "716597993:AAEbuSasajgXDTLuWfqfelV3GNUOmN1bngs"
bot = telebot.TeleBot(token)

# bot.send_message(976475, "test from pycharm")
'''
upd = bot.get_updates()          # все обновления в список
last_upd = upd[-1]            # последнее обновление
print(last_upd.message)
print(last_upd.message.text)
'''

@bot.message_handler(content_types="text")
def handle_text(message):
    print("пришло тектовое сообщение от пользователя:")
    print(message.text)
    bot.send_message(message.from_user.id, "Сообщение получено")


bot.polling(none_stop=True, interval=0)
