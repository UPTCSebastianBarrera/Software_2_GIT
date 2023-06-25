import Contants as keys
from telegram.ext import *
import responses as res


print("Bot iniciado")

def start_command(update, context):
    update.message.reply_text('Escribe hola para iniciar')
    

def help_command(update, context):
    update.message.reply_text('Este es un chatbot de la UPTC')

def message_handler(update, context):
    input = str(update.message.text).lower()
    response = res.sample_responses(input)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} cause error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    
    updater.start_polling()
    updater.idle()

main()


