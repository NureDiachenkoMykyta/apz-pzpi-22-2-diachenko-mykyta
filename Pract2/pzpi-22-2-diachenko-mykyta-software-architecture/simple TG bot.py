import telebot
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])

def greet(message):
   bot.reply_to(message, 'Вітаю! Це приклад Telegram-бота.')
 
   bot.polling()
