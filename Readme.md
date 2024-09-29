# Telegram Bot for Extracting WebView Data

This is a Python-based Telegram bot that connects to a specific bot, requests a WebView, and extracts data from a URL. The bot uses the [Telethon](https://github.com/LonamiWebs/Telethon) library to interact with Telegram's API.

## Features

- Connects to the Telegram API using a bot token, API ID, and API hash.
- Sends a WebView request to the bot `BlumCryptoBot`.
- Extracts `tgWebAppData` from the WebView URL.
- Logs errors and handles user bans.

## Prerequisites

To run this bot, you will need the following:

- **Python 3.7+**
- **Telethon** library
- **Telegram API credentials**
  - `API ID` and `API Hash`: Get these from [my.telegram.org](https://my.telegram.org).
  - `Bot Token`: Create a bot via [BotFather](https://t.me/BotFather) on Telegram to get this.

## Installation

1. **Clone the repository** (or download the script):

    ```bash
    git clone https://github.com/your-repo/telegram-bot-webview.git
    cd telegram-bot-webview
    ```

2. **Install the required dependencies**:

    You can install the required dependencies by running:

    ```bash
    pip install telethon
    ```

3. **Configure the script**:

   - Open the script file and replace the following placeholders with your Telegram API credentials:
   
     ```python
     api_id = 'YOUR_API_ID'
     api_hash = 'YOUR_API_HASH'
     ```

## Usage

1. **Run the bot**:

    After configuring the script with your API keys, run the bot using:

    ```bash
    python telegram_bot.py
    ```

2. **Expected output**:

    If everything is set up correctly, the bot will extract the `tgWebAppData` from the WebView URL and print it in the terminal.

    Example:
    
    ```
    Extracted Data: <your-data-here>
    ```

    If the bot fails to extract the data or encounters an error, it will log the error message.

## Code Overview

### Main Functions:

- `get_tg_web_data(self)`: 
    - Connects to Telegram using the credentials.
    - Sends a WebView request to the `BlumCryptoBot`.
    - Extracts `tgWebAppData` from the URL and returns it.

### Error Handling:

- If the user is banned (`USER_DEACTIVATED_BAN`), the bot will disconnect and return an error message.
- If the WebView URL format is incorrect, the bot will log an `IndexError` and return `None`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Telethon](https://github.com/LonamiWebs/Telethon) - Telegram client API for Python
