<h1 align="center">Whisper Bot</h1>

<p align="center">
  <a href="https://github.com/abirxdhack/WhisperBot/stargazers"><img src="https://img.shields.io/github/stars/abirxdhack/WhisperBot?color=blue&style=flat" alt="GitHub Repo stars"></a>
  <a href="https://github.com/abirxdhack/WhisperBot/issues"><img src="https://img.shields.io/github/issues/abirxdhack/WhisperBot" alt="GitHub issues"></a>
  <a href="https://github.com/abirxdhack/WhisperBot/pulls"><img src="https://img.shields.io/github/issues-pr/abirxdhack/WhisperBot" alt="GitHub pull requests"></a>
  <a href="https://github.com/abirxdhack/WhisperBot/graphs/contributors"><img src="https://img.shields.io/github/contributors/abirxdhack/WhisperBot?style=flat" alt="GitHub contributors"></a>
  <a href="https://github.com/abirxdhack/WhisperBot/network/members"><img src="https://img.shields.io/github/forks/abirxdhack/WhisperBot?style=flat" alt="GitHub forks"></a>
</p>

<p align="center">
  <em>Whisper Bot: Send secret, encrypted messages in Telegram groups via inline mode. Easy-to-use, supports private messaging without being part of the group.</em>
</p>
<hr>

## Features

- 🌐 **Inline Mode Support**: Send whisper messages without adding the bot to a group.
- 💬 **Secret Messaging**: Messages are only visible to the sender and the intended recipient.
- 🔄 **Help and Back Button**: Easily access the help menu and navigate back with built-in buttons.
- 📎 **User-Friendly**: Simply use the bot in the inline mode to send private messages easily.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher.
- `pyrofork` library.
- A Telegram bot token (you can get one from [@BotFather](https://t.me/BotFather) on Telegram).
- API ID and Hash: You can get these by creating an application on [my.telegram.org](https://my.telegram.org).

## Installation

To install `pyrofork` run the following command:

```bash
pip install pyrofork
```

**Note: If you previously installed `pyrogram`, uninstall it before installing `pyrofork`.**

## Configuration

1. Open the `config.py` file in your favorite text editor.
2. Replace the placeholders for `API_ID`, `API_HASH`, and `BOT_USERNAME` with your actual values:
   - **`API_ID`**: Your API ID from [my.telegram.org](https://my.telegram.org).
   - **`API_HASH`**: Your API Hash from [my.telegram.org](https://my.telegram.org).
   - **`BOT_TOKEN`**: The token you obtained from [@BotFather](https://t.me/BotFather).
   - **`BOT_USERNAME `**: Your Created Bot Username from [@BotFather](https://t.me/BotFather).

## How to Set Up Inline Mode

To enable inline mode for your bot, follow these steps:

   - Open a chat with **BotFather** in Telegram.
   - Send the command `/setinline` to BotFather.
   - Choose the bot for which you want to enable inline mode.
   - After that, send a sample text like: `Hi` or `Hello`.

For more information on inline bots, refer to the [Telegram Bot Documentation](https://core.telegram.org/bots/inline).

## Deploy the Bot

```sh
git clone https://github.com/abirxdhack/WhisperBot
cd WhisperBot
python whisper.py
```

## Bot Commands

- **/start**: Sends a welcome message with instructions on how to use the bot.
- **Inline Query**: Use `@CcZxdvvtfBot your message @username` in an inline query to send a whisper message. `@CcZxdvvtfBot` Example Bot use your own bot.

## How to Use

1. **Inline Mode**:
   - Use the bot in inline mode by typing `@CcZxdvvtfBot <your whisper> @<recipient_username> or userid`.
   - For example: `@CcZxdvvtfBot hello this is a test messages @abirxdhackz`.
   - Only the sender and the recipient will be able to view the secret message.

## Note

- **User ID Restriction**: If a user has not started the bot, you will not be able to send secret messages to them using their user ID. Ensure that the recipient has interacted with the bot at least once by clicking **Start**.

## Authors
- Name: Bisnu Ray 
- Telegram: [@TheSmartBisnu](https://t.me/TheSmartBisnu)
- Name: Abir Arafat Chawdhury
- Telegram: [@abir_x_official](https://t.me/abir_x_official)

✨ **Note**: If you found this repo helpful, please fork and star it. Also, feel free to share with proper credit!
