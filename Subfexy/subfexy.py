# SUBFEXY v1.0.0
import requests
import os
import fade
from time import sleep
from urllib.parse import urlparse
from colorama import Fore, Style, init

init(autoreset=True)

cmd_list = """
----------CMD List----------

1) s / start    = Starts the tool.
2) h / help     = Shows this page.
3) v / version  = Displays the current version.
4) q / quit     = Quits the tool.
5) x / exit     = Also quits the tool.
6) cc / credits = Credits to the dev.
7) cls / clear  = Clears the screen.

----------------------------
"""

ASCIIart = """
   ▄████████ ███    █▄  ▀█████████▄     ▄████████    ▄████████ ▀████    ▐████▀ ▄██   ▄   
  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███   ███▌   ████▀  ███   ██▄ 
  ███    █▀  ███    ███   ███    ███   ███    █▀    ███    █▀     ███  ▐███    ███▄▄▄███ 
  ███        ███    ███  ▄███▄▄▄██▀   ▄███▄▄▄      ▄███▄▄▄        ▀███▄███▀    ▀▀▀▀▀▀███ 
▀███████████ ███    ███ ▀▀███▀▀▀██▄  ▀▀███▀▀▀     ▀▀███▀▀▀        ████▀██▄     ▄██   ███ 
         ███ ███    ███   ███    ██▄   ███          ███    █▄    ▐███  ▀███    ███   ███ 
   ▄█    ███ ███    ███   ███    ███   ███          ███    ███  ▄███     ███▄  ███   ███ 
 ▄████████▀  ████████▀  ▄█████████▀    ███          ██████████ ████       ███▄  ▀█████▀  
"""

def CS():
    os.system('cls' if os.name == 'nt' else 'clear')


print(fade.purpleblue(ASCIIart))
while True:
    choice = input("""
-- Type "h" or "help" for a list of commands
-- Type "s" or "start" to begin

>> """).lower()
    if choice in ['h', 'help']:
        print(cmd_list)
    elif choice in ['s', 'start']:
        break
    elif choice == 'v':
        print('\nVersion: v1.0.0')
    elif choice == 'cc' or choice == 'credits':
        print('\nCredits to ' + Fore.MAGENTA + 'Exyth.')
    elif choice in ['cls', 'clear']:
        CS()
    elif choice in ['q', 'quit', 'x', 'exit']:
        exit(0)



while True:
    MainURL = input("\n[URL] Enter URL >> ").strip()
    print('\n[I] Checking URL...\n')

    try:
        respo = requests.get(MainURL, timeout=5)
        if respo.status_code == 200:
            print(Fore.GREEN + '\n[Success] URL is reachable.\n')
            sleep(2)
            CS()
            break
        else:
            print(Fore.YELLOW + f'\n[Warning] URL reachable but returned STATUS_CODE: {respo.status_code}\n')
            print(Fore.YELLOW + 'Please enter a different URL.\n')
    except requests.exceptions.RequestException as ERR:
        print(Fore.RED + f'\n[ERROR] Could not reach the URL.\nDetails: {ERR}')
        print(Fore.RED + 'Please try again.\n')

URLParse = urlparse(MainURL)
URLdomain = URLParse.netloc or URLParse.path

ssubs, fsubs = 0, 0

with open('SUBDOMAINS.txt', 'r') as subs:
    subdomains = subs.read().splitlines()

print('[+] Checking subdomains...\n')

for sub in subdomains:
    try:
        SUBURL = f'https://{sub}.{URLdomain}'
        SUBRESP = requests.get(SUBURL, timeout=5)

        if SUBRESP.status_code == 200:
            with open('SUBDOMAINS_LOGS.txt', 'a') as subLOGS:
                subLOGS.write(SUBURL + '\n')
            print(f'[!!] SUBDOMAIN {Fore.CYAN + Style.BRIGHT + SUBURL}{Style.RESET_ALL} IS {Fore.GREEN + Style.BRIGHT}SUCCESSFUL!')
            print('You can find it in', Fore.CYAN + '"SUBDOMAINS_LOGS.txt"')
            ssubs += 1

    except requests.RequestException:
        print(f'[X] {SUBURL} ' + Fore.RED + 'No response')
        fsubs += 1

input(f'\n[✔️] Done. {ssubs} successful, {fsubs} failed. Press ENTER to exit.')

# SUBFEXY v1.0.0