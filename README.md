# telebot
A simple and efficient Telegram bot built with Python, designed to automate tasks and provide various functionalities.

## Features

- 📩 **Automated Messaging**: Schedule and send messages automatically.
- 🔍 **Information Retrieval**: Fetch data from APIs and display it in chat.
- 🛠 **Custom Commands**: Define and execute custom commands.
- 🏗 **Easy Deployment**: Simple setup with minimal dependencies.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Ainella/telebot.git
   cd telebot
   ```
2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables**:
   - Create a `.env` file and add your Telegram Bot API token:
     ```
     BOT_TOKEN=your_telegram_bot_token
     ```
4. **Run the Bot**:
   ```sh
   python bot.py
   ```

## Usage

- Start the bot on Telegram by sending `/start`.
- Use `/help` to see available commands.
- Customize responses and behavior by modifying `bot.py`.
