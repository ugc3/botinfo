import requests
import telebot
import time
token = "5571144697:AAFAPXRN2f5UEUivu1qA7kOQddQJ7OT4MrU"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id,f"اهلا عزيزي المستخدم")
	time.sleep(1)
	bot.send_message(message.chat.id,f"ارسل الايميل الان من فضلك..")
	@bot.message_handler(func=lambda followinG:True )
	def com(message):
			Bl = message.text
	
			url ='https://www.instagram.com/accounts/account_recovery_ajax/'
			head= {
								        'accept': '*/*',
								        'accept-encoding': 'gzip, deflate, br',
								        'accept-language': 'en-US,en;q=0.9',
								        'content-length': '336',
								        'content-type': 'application/x-www-form-urlencoded',
								        'cookie': 'mid=YPvYkQALAAH7ZlNgkXiBnW6y7AOy; ig_did=1C396C9B-7DC7-463E-A68B-FE991198F88A; ig_nrcb=1; shbid="944\0546317830362\0541658653745:01f7bf09c30c2bf6ae86e32af31b5991cd84a607e1547a0132f6b653c4b76ecc26abbc4e"; shbts="1627117745\0546317830362\0541658653745:01f716bcf5ca94c711aa8ee17e52cf927685a30c29c89e0310cfe9f86589901109fd5b1e"; rur="RVA\05448065200129\0541658659405:01f7d96b5f9c1cf2396b6d00cbc7281da4dc2bb4c75a035bf4917e188315d170aec60aa2"; csrftoken=mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
								        'origin': 'https://www.instagram.com',
								        'referer': 'https://www.instagram.com/',
								        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
								        'sec-ch-ua-mobile': '?0',
								        'sec-fetch-dest': 'empty',
								        'sec-fetch-mode': 'cors',
								        'sec-fetch-site': 'same-origin',
								        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
								        'x-asbd-id': '437806',
								        'x-csrftoken': 'mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
								        'x-ig-app-id': '936619743392459',
								        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
								        'x-instagram-ajax': 'caee87137ae9',
								        'x-requested-with': 'XMLHttpRequest'
								    }
			data={
										'query': '{}'.format(Bl)
			}
			rq = requests.post(url,headers=head,data=data).json()
									
			try:
				fa =str(rq['options']['can_use_facebook'])
				if fa =='True':
					L3 = 'مرتبط في الفيس بوك'
											
				else:
					L3='غير مرتبط في الفيس بوك'
				ph = str(rq['options']['can_send_phone'])
				if ph =='True':
					L5 = ('مرتبط برقم')
				else:
					L5='غير مرتبط برقم'
					bot.send_message(message.chat.id,f"Email : True - مرتبط\nPhone : {L5}\nFacebook : {L3}\nBy : @MVMVP - @W_Y67")
				
			except KeyError as Error:
				bot.send_message(message.chat.id,f"غير مرتبط\nالحساب لا يعمل \nلم يكون بمكانك عمل ريست الانة الحساب غير مرتبط")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		   print(e)
		   time.sleep(3)
