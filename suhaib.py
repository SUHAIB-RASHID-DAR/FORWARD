import telegram

# Set up the Telegram bot using your bot's token
TOKEN = '5830549215:AAFPIBMULsTr6WpnIXkM1Ics7Xdv1wJn9Ys'
bot = telegram.Bot(token=TOKEN)

# Define the function to forward messages
def forward(update, context):
    # Replace with the ID of the source chat (group/channel)
    source_chat_id = -1001743810895
    # Replace with the ID of the target chat (group/channel)
    target_chat_id = -1001832609217
    
    # Get the command and message text
    command = update.message.text.split()[0]
    message_text = ' '.join(update.message.text.split()[1:])
    
    # Forward the message to the target chat
    if command == '/forward':
        message = update.message.reply_to_message
        if message is None:
            update.message.reply_text('Please reply to a message to forward.')
        else:
            forwarded_message = bot.forward_message(chat_id=target_chat_id, from_chat_id=source_chat_id, message_id=message.message_id)
            update.message.reply_text('Message forwarded successfully.')
    elif command == '/send':
        bot.send_message(chat_id=target_chat_id, text=message_text)
        update.message.reply_text('Message sent successfully.')
    else:
        update.message.reply_text('Invalid command. Use /forward to forward a message or /send <message> to send a message.')

# Define the main function to handle incoming messages
def main():
    updater = telegram.Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Add a handler for the /forward and /send commands
    dispatcher.add_handler(telegram.CommandHandler('forward', forward))
    dispatcher.add_handler(telegram.CommandHandler('send', forward))

    # Start the bot
    updater.start_polling()
    updater.idle()

# Call the main function to start the bot
if __name__ == '__main__':
    main()
