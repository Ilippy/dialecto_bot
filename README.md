# Dialecto Telegram Bot
This is a Telegram bot that uses OpenAI's Whisper model to transcribe voice messages into text. 
The bot allows users to send voice messages, which are then transcribed into text using Whisper, 
a powerful speech-to-text model.

## Features
- **Voice-to-text transcription**: Send voice messages to the bot and receive the transcribed text.
- **Supports multiple languages**: Whisper can transcribe voice messages in many languages.
- **Automatic punctuation**: The transcribed text includes punctuation, making it easier to read.
- **Group support**: Add the bot to any Telegram group, and it will automatically transcribe all voice messages sent in the group to text.

## Prerequisites
Before setting up the bot, make sure you have the following:

1. **Python 3.8+**
2. **Telegram Bot Token**: Create a bot using [BotFather](https://core.telegram.org/bots#botfather) and get the bot token.
3. **OpenAI Whisper Model**: Install and configure Whisper for transcription.

## Installation
1. Clone this repository or download the files:
```bash
git clone https://github.com/Ilippy/dialecto_bot.git
cd dialecto_bot
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```
4. Set up your configuration:
Create a `.env` file in the root of the project and add your Telegram bot token:
```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```
5. Run the bot:
```bash
python bot.py
```

## How It Works
* **/start**: Sends a welcome message with an overview of what the bot can do.
* **Voice Message**: When a user sends a voice message, the bot downloads the file and then uses OpenAI's Whisper model to transcribe the audio to text. The bot replies with the transcribed text.
* **Group Mode**: When the bot is added to a group, it listens for voice messages in the group chat and automatically transcribes them into text. The bot will reply with the transcribed text in the group chat.

## Example Usage
1. Start a chat with your bot by sending the /start command.
2. Send a voice message.
3. The bot will reply with the transcribed text from your voice message.
4. **In a Group**: Add the bot to a group, and whenever a voice message is sent, the bot will automatically transcribe it.

## Dependencies
The bot uses the following Python packages:

* `aiogram`: For handling Telegram bot interactions.
* `whisper`: OpenAI Whisper model for speech-to-text transcription.
* `asyncio`: For asynchronous operations.

## Limitations
* **Performance**: Transcription may take time depending on the length of the audio message and the model used.
* **Resource Usage**: Whisper models require significant CPU or GPU resources. For more accurate transcription, larger models will be slower and require more memory.
* **Language Support**: Whisper supports many languages, but results may vary based on the audio quality and the clarity of speech.

## License
This project is licensed under the MIT License.
