import Contants as keys
from telegram import *
from telegram.ext import *
from typing import Final
import responses as res


print("Bot iniciado")

TOKEN: Final = keys.API_KEY
BOT_USERNAME: Final = '@Admisiones_UPTC_bot'

# Comandos

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Buenas, bienvenido al chatbot de telegram \nEscribe el comando /help para continuar')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text('Escribe \na) Preguntas mas frecuentes \nb) Si quieres enviarnos un mensaje \nc) Para responder nuestra encuesta de satisfaccion \nd) Para contactarnos \n/help Para volver al menu de inicio')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('este es un comando custom')
    
async def one(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    allQ = res.connection('1')
    for row in allQ:
        
         await update.message.reply_text(row[0],row[1])
    
    

#Respuestas

def custom_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    update.message.reply_text('t')
    
    return None
    


def handle_responses(text: str) -> str:
    
    processed: str = text.lower()
    
    
    if 'a' in text:
        
        
        
        return res.connection(processed)
        
    if 'b' in text:
        return 'pregunta especifica'
    
    if 'c' in text:
        return 'encuesta'
    
    if 'd' in text:
        return 'contactanos'
    
    
    if '1':
    
        return res.connection(processed)
    
    if '2':
    
        return res.connection(processed)
    if '3':
        return res.connection(processed)
    
    if '4':
        return res.connection(processed)
    
    if '5':
        return res.connection(processed)
    
    if '6':
        return res.connection(processed)
    
    if '7':
        return res.connection(processed)
    
    if '8':
        return res.connection(processed)
    
    
    return 'opcion incorrecta'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str =update.message.text
    
    print(f'User  ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        
        
        response: str = handle_responses(text)
        
    print('Bot: ', response)
    
    await update.message.reply_text(response)
    

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('Update {update} caused error {context.error}')
    

if __name__ == '__main__':
    
    print('Starting bot....')
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('custom',custom_command))
    
    #messages
    
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    
    #error 
    app.add_error_handler(error)
    
    
    #polls
    
    print('Polling....')
    app.run_polling(poll_interval=1)
    

#def start_command(update, context):
#    update.message.reply_text('Escribe hola para iniciar')
    

#def help_command(update, context):
#    update.message.reply_text('Este es un chatbot de la UPTC')

#def message_handler(update, context):
#    input = str(update.message.text).lower()
#    response = res.sample_responses(input)
#    update.message.reply_text(response)

#def error(update, context):
    print(f"Update {update} cause error {context.error}")

#def main():
#    updater = updater(keys.API_KEY, use_context=True)
#    dp = updater.dispatcher
#    dp.add_handler(CommandHandler("start", start_command))
#    dp.add_handler(CommandHandler("start", help))
#    dp.add_handler(MessageHandler(Filters.text, message_handler))
#    
#    updater.start_polling()
#    updater.idle()

#main()


