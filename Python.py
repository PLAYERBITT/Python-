from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
import time
import subprocess

# Function to check server status
def check_server_status():
    response = subprocess.run(["ping", "-c", "1", "your-server-ip"], stdout=subprocess.PIPE)
    if response.returncode == 0:
        return "Server is up!"
    else:
        return "Server is down!"

# Command to start the bot and send the server status
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('I am here! Type /status to check server status.')

# Command to check the server status
def status(update: Update, context: CallbackContext) -> None:
    server_status = check_server_status()
    update.message.reply_text(f"Server Status: {server_status}")

def main():
    # Telegram Bot API token
    updater = Updater("7235646357:AAEFqhtbZhYIxxKywRoqI85IZZwY42M70k8")

    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("status", status))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
