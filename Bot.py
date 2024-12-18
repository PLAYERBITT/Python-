from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. Type /status to check server status.')

# Function to handle the /status command
def status(update: Update, context: CallbackContext) -> None:
    # Replace 'your-server-ip' with the actual server IP or hostname
    server_ip = "your-server-ip"
    response = os.system(f"ping -c 1 {server_ip}")
    
    if response == 0:
        update.message.reply_text(f"The server at {server_ip} is UP.")
    else:
        update.message.reply_text(f"The server at {server_ip} is DOWN.")

def main():
    # Set up the bot
    updater = Updater(7235646357:AAEFqhtbZhYIxxKywRoqI85IZZwY42M70k8)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("status", status))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
