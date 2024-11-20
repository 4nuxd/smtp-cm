import smtplib
import os
import subprocess
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
init()  # Initialize colorama

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

def read_credentials(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            credentials = []
            for line in lines:
                parts = line.strip().split('|')  # Adjusted to '|'
                if len(parts) == 4:
                    credentials.append(parts)
                else:
                    print(f"Invalid format: {line.strip()}")
            return credentials
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")

def read_message(file_path):
    try:
        with open(file_path, 'r') as file:
            message = file.read()
        return message
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")

def send_email(smtp_info, recipient, message):
    url, port, user, password = smtp_info
    subject = input("Enter the subject of the email: ")
    try:
        print(f"Connecting to {url} on port {port}...")
        server = smtplib.SMTP(url, int(port))
        server.starttls()
        server.login(user, password)
        
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
	
        
        server.send_message(msg)
        server.quit()
        return f"[+] Sent | {url}|{port}|{user} -- Email sent successfully"
    except smtplib.SMTPAuthenticationError:
        return f"[-] Bad | {url}|{port}|{user} -- Authentication error"
    except smtplib.SMTPException as e:
        return f"[-] Bad | {url}|{port}|{user} -- SMTP error: {e}"
    except Exception as e:
        return f"[-] Fail | {url}|{port}|{user} -- An error occurred: {e}"

def save_results_to_file(results):
    banner = print_banner()
    file_path = 'results.txt'
    
    with open(file_path, 'w') as file:
        file.write(banner + '\n')
        for result in results:
            file.write(result + '\n')
    print(f"Results saved to {file_path}")

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    credentials_file = os.path.join(script_dir, 'credentials.txt')
    message_file = os.path.join(script_dir, 'message.txt')
    
    if not os.path.isfile(credentials_file):
        print(f"File not found: {credentials_file}")
        return

    if not os.path.isfile(message_file):
        print(f"File not found: {message_file}")
        return

    try:
        credentials = read_credentials(credentials_file)
        message = read_message(message_file)
        
        recipient = input("Enter the recipient email address: ")
        
        results = []
        for smtp_info in credentials:
            result = send_email(smtp_info, recipient, message)
            results.append(result)
            if "sent successfully" in result:
                print(colored(result, 'green'))
            elif "Authentication error" in result:
                print(colored(result, 'yellow'))
            else:
                print(colored(result, 'red'))

        print("\nSummary:")
        for result in results:
            print(result)

        if results:
            save_results_to_file(results)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    print_banner()
    main()
