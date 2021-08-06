import urllib.request
import json
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime


def get_soup(url):

	f = urllib.request.urlopen(url)
	
	nyb = f.read()
	mystr = nyb.decode("utf8")
	f.close()

	soup = json.loads(mystr)

	return soup







bot_token = '1946822753:AAETcCQS-stldsUcjlwbIUdCIwe7ios8q-I'





def getAdmin(update, context):
	if len(context.args) == 1:
		url = 'https://api.telegram.org/bot' + bot_token + '/getChatAdministrators?chat_id=@' + context.args[0]
		f = get_soup(url)
		text = ''
		for user in f['result']:
			# text += "id юзера = " + str(user['user']['id']) + '\n'
			# while True:
			# 	try:
			# 		text += "имя = " + str(user['user']['first_name']) + '\n'
			# 		break
			# 	except(KeyError):
			# 		text += "имя = нет имени" + '\n'
			# 		break
			# while True:
			# 	try:
			# 		text += "фамилия = " +  str(user['user']['last_name']) + '\n'
			# 		break
			# 	except(KeyError):
			# 		text += "фамилия = нет фамилии" + '\n'
			# 		break

			while True:
				try:
					
					text += "@" +  str(user['user']['username'] + ' - ')
					break
				except(KeyError):
					text += "нет юзернейма - "
					break

			while True:
				try:
					
					text +=  str(user['status'] + '\n')
					break
				except(KeyError):
					text += "uнет статуса \n"
					break
		update.message.reply_text(text)


	else:
		update.message.reply_text('Форма запроса такая: getAdmin имя_публичного_чата')
		update.message.reply_text('Имя берется из ссылки. Например, для https://t.me/IntexcoinOfficialGroup, имя будет IntexcoinOfficialGroup')



def echo(update, context):

	if (update.message.text == 'hi' or update.message.text == 'Hi' or update.message.text == 'HI'):
		name = update['message']['chat']['first_name']
		update.message.reply_text('Привет, ' + name)
	else:
		chat_name = update.message.text.replace("https://t.me/", "")
		url = 'https://api.telegram.org/bot' + bot_token + '/getChatAdministrators?chat_id=@' + chat_name
		f = get_soup(url)
		text = ''
		for user in f['result']:
			while True:
				try:
					
					text += "@" +  str(user['user']['username'] + ' - ')
					break
				except(KeyError):
					text += "нет юзернейма - "
					break

			while True:
				try:
					
					text +=  str(user['status'] + '\n')
					break
				except(KeyError):
					text += "нет статуса \n"
					break
		update.message.reply_text(text)
	
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text('Произошла ошибка, пингуй Валеру')






# Enable logging (логи)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)



def main():
	updater = Updater(bot_token, use_context=True)
	
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("getAdmin", getAdmin ))
	 
	dp.add_handler(MessageHandler(Filters.text, echo))
	
	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()
	
	

if __name__ == '__main__':
	main()
