# Telegram Bot for Extracting WebView Data

This repository contains a Python-based Telegram bot that connects to a specific Telegram bot, requests a WebView, and extracts data from the response URL. The bot utilizes the [Pyrogram](https://docs.pyrogram.org/) library to interact with the Telegram API effectively.

## Features

- Connects to the Telegram API using API ID and API hash.
- Sends a WebView request to the `BlumCryptoBot`.
- Extracts `tgWebAppData` from the WebView URL.
- Implements robust error handling and logging for user bans and connection issues.

## Prerequisites

To run this bot, you will need the following:

- **Python 3.7 or higher**
- **Pyrogram** library
- **Telegram API credentials**:
  - **API ID** and **API Hash**: Obtain these from [my.telegram.org](https://my.telegram.org/).
  - **Bot Token**: Create a bot via [BotFather](https://t.me/BotFather) on Telegram.

## Installation

Follow these steps to set up the project:

1. **Clone the repository** (or download the script):

    ```bash
    git clone https://github.com/your-username/telegram-bot-webview.git
    cd telegram-bot-webview
    ```

2. **Install the required dependencies**:

    You can install the necessary dependencies by running:

    ```bash
    pip install pyrogram
    ```

3. **Configure the script**:

   - Open the script file (e.g., `telegram_bot.py`) and replace the placeholders with your Telegram API credentials:
   
     ```python
     API_ID = 'YOUR_API_ID'
     API_HASH = 'YOUR_API_HASH'
     ```

## Usage

1. **Run the bot**:

    After configuring the script with your API keys, execute the bot using:

    ```bash
    python telegram_bot.py
    ```

2. **Expected Output**:

    If everything is set up correctly, the bot will extract the `tgWebAppData` from the WebView URL and print it in the terminal.

    Example output:
    
    ```
    Extracted Data: <your-data-here>
    ```

    If the bot fails to extract the data or encounters an error, it will log the error message.

## Code Overview

### Main Functions

- `get_tg_web_data(self)`:
    - Connects to Telegram using the provided credentials.
    - Sends a WebView request to the `BlumCryptoBot`.
    - Extracts `tgWebAppData` from the URL and returns it.

### Error Handling

- If the user is banned (`USER_DEACTIVATED_BAN`), the bot will disconnect and return an error message.
- If the WebView URL format is incorrect, the bot will log an `IndexError` and return `None`.

## Testing

You can test the bot by sending commands to `BlumCryptoBot` or by modifying the script to interact with other Telegram bots.

## Troubleshooting

- **Connection Issues**: Ensure your API credentials are correct and your internet connection is stable.
- **User Banned Error**: If you receive a `USER_DEACTIVATED_BAN` error, verify if your account has been banned from the bot.
- **Invalid URL Error**: Ensure that the WebView URL you are trying to access is correctly formatted.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Pyrogram](https://docs.pyrogram.org/) - Telegram client API for Python.
- [Telegram](https://telegram.org/) - The platform that makes this bot possible.
