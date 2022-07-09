import time

import requests

import telebot

from time import sleep

token = "5571144697:AAEpKuvOtfZ7JeR4tbFx5js8u0QOUUID04E"


bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['greet','start'])

def start(message):

	msg=(f"اهلا بك عزيزي المستخدم هذا البوت مخصص لي ريست الباسورد ")	bot.send_message(message.chat.id, msg)

	sleep(2)

	bot.send_message(message.chat.id, f"ارسال الان الايميل او اليوزر او الرقم \nBy : @MVMVP - @W_Y67\nZiald Kareem")

	

	@bot.message_handler(func=lambda followinG:True )

	

	def com(message):

		sid =(message.text)

		

		

		url ="https://www.instagram.com/accounts/password/reset/"

		head1 = {

        'accept':'*/*',

        'accept-encoding':'gzip, deflate, br',

        'accept-language':'en-US,en;q=0.9',

        'content-length':'1487',

        'content-type':'application/x-www-form-urlencoded',

        'cookie':'sessionid=54072972258%3AW2dN46VfKyyNlY%3A3%3AAYcA2HYtSZH7Neg4PL5zfKHFI58Y9BOUpRPAhLMS5g;ds_user_id=54072972258;csrftoken=fudNnn7Q8Wu1S1vXnZyflJAN1Fnvz0m2',

        'origin':'https://www.instagram.com',

        'referer':'https://www.instagram.com/accounts/password/reset/',

        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Opera";v="85"',

        'sec-ch-ua-mobile':'?0',

        'sec-ch-ua-platform':'"Windows"',

        'sec-fetch-dest':'empty',

        'sec-fetch-mode':'cors',

        'sec-fetch-site':'same-origin',

        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.47',

        'x-asbd-id':'198387',

        'x-csrftoken':'fudNnn7Q8Wu1S1vXnZyflJAN1Fnvz0m2',

        'x-ig-app-id':'936619743392459',

        'x-ig-www-claim':'0',

        'x-requested-with':'XMLHttpRequest',

 

}

		data1 = {

  "email_or_username":f"{sid}",

  "recaptcha_challenge_field":"",

  "flow":"",

  "app_id":"",

  "source_account_id":""

   }

		rq = requests.post(url,headers=head1,data=data1).text

		

		if ('"email_or_sms_sent":true') in rq:

			

			if ('@') in sid :

				Oo = rq.split('"message":')[1]

				sss = Oo.split('"Thanks! Please check')[1]

				oo1 =sss.split('for a link to reset your password."')[0]

				bot.send_message(message.chat.id, f"Sent Email or sms : True - تم\nEmail Send : {sid}\nEmail : {oo1}\nBy : @MVMVP - @W_Y67")

			else:

				Oo = rq.split('"message":')[1]

				sss = Oo.split('"Thanks! Please check')[1]

				oo1 =sss.split('for a link to reset your password."')[0]

				url22 = f'https://www.instagram.com/{sid}/?__a=1&__d=dis'

				head1 = {

			                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

			                'accept-encoding': 'gzip, deflate, br',

			                'accept-language': 'en-US,en;q=0.9',

			                'cookie': 'sessionid=54072972258%3AW2dN46VfKyyNlY%3A3%3AAYcA2HYtSZH7Neg4PL5zfKHFI58Y9BOUpRPAhLMS5g;ds_user_id=54072972258;csrftoken=fudNnn7Q8Wu1S1vXnZyflJAN1Fnvz0m2',

			                'referer': 'https://www.instagram.com/{}/'.format(sid),

			                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',

			                'sec-ch-ua-mobile': '?1',

			                'sec-fetch-dest': 'document',

			                'sec-fetch-mode': 'navigate',

			                'sec-fetch-site': 'snone',

			                'upgrade-insecure-requests': '1',

			                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.47'

				}

				rr = requests.get(url22,headers=head1).json()

				iddd = str(rr['graphql']['user']['id'])

				re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   

				ree = re.json()

				dat = ree['data']

				bot.send_message(message.chat.id, f"Sent Email or sms : True - تم\nEmail Send : {sid}\nData : {dat}\nEmail : {oo1}\nBy : @MVMVP - @W_Y67")

				time.sleep(30)

		elif ('"That e-mail address, phone number or username doesn') in rq:

				bot.send_message(message.chat.id, f"Sent Email or sms : Error\nSent Email : False - لايعمل\nUser or Email : {sid}\nBy : @W_Y67 - @MVMVP")

				time.sleep(30)

		else:

				bot.send_message(message.chat.id,f"Sent : Error - Bloak\nTime Sleep 16\n")

				time.sleep(30)

				

while True:

	try:

		bot.polling(none_stop=True)

	except Exception as e:

	       print(e)

	       sleep(10) 
