
# A Python Based Mass SMTP Checker and Mailer Tool 📨

A Python-based tool designed to:
1. **Check the validity of SMTP credentials** 🔐 by attempting to login and sending Telegram notifications for successful logins 📲.
2. **Send emails using valid SMTP credentials** for mass mailing 📧, with support for multi-threading for fast delivery ⚡.
3. The tool supports **colored console output** 🎨, making it easy to track the results of login attempts and mailer status.

## Features 🌟

### **SMTP Checker 🔍:**
- **SMTP Login Validation** ✅: Checks whether the provided SMTP credentials are valid.
- **Telegram Notifications 📲**: Sends Telegram messages when valid SMTP logins are detected.
- **Multi-threading ⚡**: Uses Python's `concurrent.futures` to process multiple credentials concurrently.
- **Color-Coded Output 🎨**: Displays success, failure, and error messages in different colors in the console.
- **Save Results 💾**: Successful logins are saved to a `good.txt` file.

### **SMTP Mailer 📤:**
- **Send Mass Emails 📧**: Sends emails using valid SMTP credentials.
- **Multi-threaded Mail Delivery ⚡**: Emails are sent concurrently, increasing speed and efficiency.
- **Customizable Email Templates ✍️**: Easily customize email subjects, body content, and attachments.

## Requirements 📋

- Python 3.x
- `termcolor` library
- `colorama` library
- `requests` library

### Install Required Modules 🛠️

To install the required dependencies, run:

```bash
pip install termcolor colorama requests
```

## Usage 📚

### **SMTP Checker 🔍:**

#### 1. **Prepare Credentials File 📄**
Create a `credentials.txt` file with the following format:

```
smtp.example.com|587|username1|password1
smtp.example.com|465|username2|password2
...
```

Each line should contain:
- SMTP server address 🌐
- Port number 🔢
- Username 👤
- Password 🔑

#### 2. **Run the Checker Tool 🏃‍♂️**
To check SMTP credentials, run the following command:

```bash
python smtp_checker.py
```

#### 3. **View Results 👀**
- **Green ✅**: Valid credentials (successful login).
- **Yellow ⚠️**: Invalid credentials (authentication error).
- **Red ❌**: Other errors (e.g., SMTP errors).
- **Telegram Notification 📲**: A notification will be sent to your Telegram when a valid login is found.
- **Log file 💾**: Successful logins are saved in `good.txt`.

#### 4. **Telegram Notifications 📲**
The tool sends a notification to Telegram for every successful login. Make sure to replace `bot_token` and `chat_id` in the `send_telegram_message()` function with your own Telegram bot's token and chat ID.

### **SMTP Mailer 📤:**

#### 1. **Prepare Email Template File 📄**
The `mailer.py` script requires an email template file (`email_template.txt`) in the following format:

```
Subject: Your Email Subject
Body: Your email body content here.
```

You can also include attachments if needed by modifying the script to handle them.

#### 2. **Run the Mailer Tool 🏃‍♂️**
To send emails, run:

```bash
python smtp_mailer.py
```

The tool will read the credentials from `credentials.txt`, attempt to login to the SMTP servers, and send the emails accordingly.

### **Example Telegram Message for SMTP Checker 📲:**
```
===========================
⁪⁬⁮⁮⁮⁮ ‌⏤͟͞⁪⁬⁮⁮⁮⁮𝙋𝙞𝙧𝙖𝙩𝙚⌁𝙃𝙞𝙩𝙨™ </> 
===========================
⌁⌁ SMTP Hit Detected ⌁⌁
===========================
[ ⌁ ] SMTP Server :- smtp.example.com
[ ⌁ ] Port       :- 587
[ ⌁ ] User      :- username1
[ ⌁ ] Password  :- password1
[ ⌁ ] By        : @noobpirate
```

### **Example Mailer Output 📧:**
```
[+] Email sent successfully to user@example.com using smtp.example.com
[-] Failed to send email to user2@example.com via smtp.example.com: Authentication failed
```

## File Structure 📂

```
.
├── credentials.txt      # File containing SMTP credentials (for both checker and mailer)
├── message.txt   # File containing email subject and body for sending emails
├── good.txt            # File to save successful SMTP logins (for checker)
├── raw.txt # File containing combos to be checked
├── smtp_checker.py     # Python script for checking SMTP credentials
├── smtp_mailer.py      # Python script for sending mass emails
```

## License 📜

This tool is for educational purposes only. Use it responsibly and only on systems that you have permission to test or send emails to.

## Author ✍️

Noob Pirate Aka Blionrie

Join our community: [PirateXNetwork](https://t.me/piratexnetwork)
