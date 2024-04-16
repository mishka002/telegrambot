from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests



TOKEN: Final = '7138793715:AAGnbb6iFjBIH9iJ4w8a5VVKyPIrqSRdmas'
BOT_USERNAME: Final = '@shotarustaveli_bot'

# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE ):
  await update.message.reply_text('გამარჯობა, და მადლობა დაინტერესებისთვის')  

  photo_url = 'https://ibb.co/sVNzQCH'
  await update.message.reply_photo(photo=photo_url)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE ):
  await update.message.reply_text('მე შოთა ვარ და მომწერე რამე.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE ):
  await update.message.reply_text('ეს არის კარგი შეკითხვა')


# Responses

def handle_response(text: str) -> str:

  processed: str = text.lower()

  if 'გამარჯობა' in processed:
    return 'გაგიმარჯოს'
  
  if 'ვინ ხარ' in processed:
    return 'მე შოთა ვარ რუსთაველი'
  
  if 'ვინ არის კუმბა?' in processed:
    return 'კუმბა არის პიროვნება'
  
  if 'რას საქმიანობ?' in processed:
    return 'მე პოეტი ვარ და უსახლკარო'
  
  return 'ვერ გავიგე აბა გაიმეორე'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  message_type: str = update.message.chat.type
  text: str = update.message.text
  
  print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

  # if message_type == 'group':
  #   if BOT_USERNAME in text:
  #     new_text: str = text.replace(BOT_USERNAME, '').strip()
  #     response: str = handle_response(new_text)

  #   else:
  #     return
  # else:
  response: str = handle_response(text)
  
  print("Bot", response)

  await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
  print(f'update {update} error {context.error}')



if __name__ == "__main__":

  print('starting bot')

  app = Application.builder().token(TOKEN).build()

  # Commands
  app.add_handler(CommandHandler('start', start_command))
  app.add_handler(CommandHandler('help', help_command))
  app.add_handler(CommandHandler('custom', custom_command))

  # Message
  app.add_handler(MessageHandler(filters.TEXT, handle_message))

  # Errors 

  app.add_error_handler(error)
  
  # Polls the bot
  print('polling bot')
  app.run_polling(poll_interval=5)