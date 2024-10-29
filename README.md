# WhatsApp Spam Message Bot 📱💬

A Python-based bot to automate sending messages on WhatsApp Web. This bot leverages **Selenium** and **webdriver-manager** to streamline browser automation, allowing users to send repeated messages to specified contacts or groups with a set interval.

---

## ⚡ Features

- Automated message sending to a specific user or group on WhatsApp Web.
- Adjustable interval between messages.
- Customizable message prompt with optional "bot status" for each message sent.
- **Easy Setup**: Just scan the QR code on WhatsApp Web, and you’re ready to go.

## 📋 Requirements
- **Python 3.7+**
- **Google Chrome Browser**
- **Chrome WebDriver** (handled by `webdriver-manager`)

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Leixien/whatsappSpamMsg_Bot.git
   ```
   ```bash
   cd whatsapp-spam-msg-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
## 💻 Project Structure

```plaintext
  whatsapp-spam-msg-bot/
  ├── int.py               # Main script to run the bot
  ├── README.md            # Project documentation
  ├── requirements.txt     # Project dependencies
  └── .gitignore           # Files and folders to ignore in Git
```
📖 License
This project is licensed under the MIT License - see the LICENSE file for details.

👤 Author
Developed by Giuseppe Scappaticci.
