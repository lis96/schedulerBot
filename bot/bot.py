import telebot
import json

BOT_TOKEN = '1056372053:AAEIn-HB0uTRZEPZQRL-DakPppdcNh5ucmU'
bot = telebot.TeleBot(BOT_TOKEN)

proxy = {
	'ip': '192.3.228.146',
	'port': '7384',
	'login': 'usa3090712',
	'password': 'rL3LBVUMLi'
}

telebot.apihelper.proxy = {
	'https':'https://{login}:{password}@{ip}:{port}'.format(
		login=proxy['login'],
		password=proxy['password'],
		ip=proxy['ip'],
		port=proxy['port']
	)
}

@bot.message_handler(commands=['start', 'help'])
def upper(message):
	bot.reply_to(message, 'Привет')

@bot.message_handler(func=lambda message: True)
def upper(message):
	bot.reply_to(message, message.text.upper())

bot.polling()