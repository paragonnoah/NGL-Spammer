

import os
import re
import time
import uuid
import random
import socket
try:
    import requests
    import colorama
    import questionary
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install questionary')

from concurrent.futures import ThreadPoolExecutor
from colorama import Fore
from questionary import Style

reset = Fore.RESET
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
white = Fore.WHITE


def print_logo(logo1, logo2, gap=3):
    lines1 = logo1.splitlines()
    lines2 = logo2.splitlines()

    max_length = max(len(lines1), len(lines2))

    lines1.extend([''] * (max_length - len(lines1)))
    lines2.extend([''] * (max_length - len(lines2)))

    for line1, line2 in zip(lines1, lines2):
        print(f"{line1}{' ' * gap}{line2}")


def banner1():
    text = """
          :=*#%@@@@@%#*=:          
       =#@@@@@%+===+%@@@@@#=       
    .+@@@@@@%.       .#@@@@@@*.    
   =@@@@%%@@.         .@@%%@@@@=   
  #@@@@--..%.          @..--@@@@#  
 #@@@@@@%= %*         +% -%@@@@@@# 
-@@%--@@*.:@@:       .@@:.*@@--%@@=
%@@@= %@+. %% +=. .=+ %%..+@% =@@@%
@@@%- #@%=. .   . .   . .=%@# -%@@@
@@@@+. -=-.             .-=- .=@@@@
*@@@@@++==  .-  .#:  -.  ==++@@@@@*
.@@@@@@@@* :#@. -%- .@#: +@@@@@@@@.
 -@@@@@@@* -#@. =@= .@#- +@@@@@@@- 
  :@@@@@@+ :%- :%@%- -%- =@@@@@@:  
    +*--: -#= -%@@@%- -%-.:--**    
     .=##%@@+ -+@@@+- +@@%##=.     
        :+#@@@@@@@@@@@@@#+:        """
        
    faded = ""
    red = 255
    for line in text.splitlines():
        faded += f"\033[38;2;{red};0;220m{line}\033[0m\n"
        if not red == 75:
            red -= 15
            if red < 0:
                red = 0

    return faded

def banner2():
    text = f"""
  ___  __  ___           __     ___ ___  _  _ ___ ___ ___ 
 / __|/  \|   \     ___ / _|   / __/ _ \| \| | __|_ _/ __|
| (_ | () | |) |   / _ \  _|  | (_| (_) | .` | _| | | (_ |
 \___|\__/|___/__  \___/_|__   \___\___/|_|\_|_| |___\___|
             |___|      |___|    {Fore.LIGHTYELLOW_EX}{Fore.RESET}


{Fore.RED}Disclaimer:
{Fore.MAGENTA}This tool/code is intended solely for educational and web testing purposes.
{Fore.MAGENTA}The owner assumes no responsibility for any misuse.
{Fore.MAGENTA}Users are advised to comply with all laws andethical standards.
{Fore.MAGENTA}The owner disclaims liability for damages resulting from the use of this tool.
{Fore.MAGENTA}By using it, you agree to do so responsibly and within legal boundaries.
{Fore.MAGENTA}The owner may modify or discontinue the tool without notice.

{white}-> Telegram: {Fore.LIGHTCYAN_EX}@G0D_of_CONFIG{reset}"""

    faded = ""
    red = 255
    green = 182
    blue = 193
    
    for line in text.splitlines():
        faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
        
        red -= 10
        green += 5
        blue += 10
        
        red = max(200, red)
        green = min(255, green)
        blue = min(255, blue)

    return faded

def banner():
    logo = banner1()
    name = banner2()
    
    print_logo(logo, name, gap=5)

def clean():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
        
def network():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        pass
    return False
        
def main():
    clean()
    banner()
    print('\n')
    print(f"{white}> {reset}{yellow}Checking Internet...{reset}")
    time.sleep(1)
    if network():
        user_input()
    else:
        print(f"{white}! {reset}{red}Error: Connect to Internet or Try again Later.{reset}")
        
def user_input():
    clean()
    banner()
    print('\n')
    my_style = Style([
        ("highlighted", "fg:#ff00d9 reverse")
    ])
    option = questionary.select(
        "Select an option to use this script:",
        choices=["Spam Question", "Spam Questions From List"], style=my_style
    ).ask()

    if option == "Spam Question" or option == "Spam Questions From List":
        url = questionary.text("Enter the NGL url (https://ngl.link/example):").ask()
        user_id = extractid(url)

        if not user_id:
            print(f"{white}! {reset}{red}Error: Invalid URL or missing UserID.{reset}")
            return

        if option == "Spam Question":
            spam_ngl(user_id)
        elif option == "Spam Questions From List":
            file_path = questionary.text("Enter the path of Questions in text file:").ask()
            spam_list(file_path, user_id)
    else:
        print(f"{white}! {reset}{red}Error: Invalid Option.{reset}")
        exit()

def extractid(url):
    match = re.search(r'https://ngl.link/(\w+)', url)
    if match:
        return match.group(1)
    else:
        return None

def spam_ngl(user_id):
    post_url = "https://ngl.link/api/submit"
    question = questionary.text("Enter the text to post as Question:").ask()
    data = {
    'username': user_id,
    'question': question,
    'deviceId': str(uuid.uuid4()),
    'gameSlug': '',
    'referrer': ''
    }
    number = questionary.text("Enter the number of times to post:").ask()

    for _ in range(int(number)):
        response = requests.post(post_url, data=data)
        time.sleep(2)
        if response.status_code == 200:
            json_data = response.json()
            queid = json_data.get('questionId', 'Unable to get Question ID')
            region = json_data.get('userRegion', 'Unable to get Region')
            print(f"{white}> {reset}{green}Spammed - {white}ID: {yellow}{queid}{white} | Region: {yellow}{region}{reset}{reset}")
        else:
            print(f"{white}! {reset}{red}Error: ({response.status_code}) > {response.text}{reset}")
            exit()

    print(f"{white}> {reset}{green}Spamming Done !{reset}")

def spam_list(file_path, user_id):
    post_url = "https://ngl.link/api/submit"

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        exit()
        
    for line in lines:
        data = {
        'username': user_id,
        'question': line.strip(),
        'deviceId': str(uuid.uuid4()),
        'gameSlug': '',
        'referrer': ''
        }
        time.sleep(2)
        response = requests.post(post_url, data=data)
        if response.status_code == 200:
            json_data = response.json()
            queid = json_data.get('questionId', 'Unable to get Question ID')
            region = json_data.get('userRegion', 'Unable to get Region')
            print(f"{white}> {reset}{green}Sending - {white}ID: {yellow}{queid}{white} | Region: {yellow}{region}{white} | Question: {yellow}{line.strip()}{reset}")
        else:
            print(f"{white}! {reset}{red}Error: ({response.status_code}) > {response.text}{reset}")
            exit()

    print(f"{white}> {reset}{green}Successfully Sended !{reset}")


if __name__ == "__main__":
    main()
