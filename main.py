import telebot
from config import keys,TOKEN
from utils_class import ConvertionExcaption, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help (massage: telebot.types.Message):
    text  = 'Чтобы начать работу, введите команду боту в следующем формате: <имя валюты> <в какую валюту перевести> <кол-во переводимой валюты>\nСписок всех доступных валют: /values'
    bot.reply_to(massage, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text,key, ))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExcaption('Слишком много параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote,base,amount)*float(amount)
    except ConvertionExcaption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        text = f'Стоимость{amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()