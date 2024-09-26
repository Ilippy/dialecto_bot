# pip install openai-whisper aiogram python-dotenv
import os
import whisper
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram import Router
import asyncio
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize the Whisper model (you can choose a specific model like 'base', 'small', etc.)
whisper_model = whisper.load_model("base")

# Create the bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Welcome message
WELCOME_TEXT = (
    "Hello! I am **Dialecto**, your personal assistant for converting audio messages to text. 🎧✍️\n\n"
    "Here's what I can do:\n"
    "1. **Send** any voice message in the chat.\n"
    "2. **Get** a quick and accurate text transcription.\n\n"
    "Use me for convenient reading of audio messages and simplifying your work with text. 🚀\n\n"
    "Simply send a voice message, and I'll transcribe it for you!"
)


# Handle /start command
@router.message(CommandStart())
async def handle_start(message: types.Message):
    """
    Sends a welcome message when the user types /start.
    """
    await message.answer(WELCOME_TEXT, parse_mode="Markdown")


# Function for transcribing audio using Whisper
async def transcribe_audio(audio_path: str):
    """
    This function uses the Whisper model to transcribe audio files to text.
    """
    try:
        # Use the Whisper model to transcribe the audio
        result = whisper_model.transcribe(audio_path, fp16=False)
        return result['text']
    except Exception as e:
        return f"Error during transcription: {e}"


# Handle voice messages
@router.message(lambda message: message.voice)
async def handle_voice_message(message: types.Message):
    """
    Processes voice messages sent by users, converts them to text using the Whisper model,
    and sends the transcribed text back to the user.
    """
    user_id = message.from_user.id
    message_id = message.message_id
    ogg_file = f"voice_{user_id}_{message_id}.ogg"
    try:
        # Download the voice message
        file_info = await bot.get_file(message.voice.file_id)
        downloaded_file = await bot.download_file(file_info.file_path)

        # Save the OGG file
        with open(ogg_file, 'wb') as f:
            f.write(downloaded_file.read())

        # Transcribe the OGG file using Whisper
        text = await transcribe_audio(ogg_file)

        # Send the transcribed text to the user
        await message.reply(text)

    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

    finally:
        # Remove the temporary audio file
        if os.path.exists(ogg_file):
            os.remove(ogg_file)


# Start the bot
async def main():
    """
    Starts the bot and begins polling for new messages.
    """
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
