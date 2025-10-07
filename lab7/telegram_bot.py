import os
from dotenv import load_dotenv
import telebot

load_dotenv()

TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise SystemExit('Помилка: TOKEN не знайдений в .env')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text','sticker','photo','audio','voice','video','document'])
def echo(message):

    try: 
        if message.content_type == 'text':
            bot.send_message(message.chat.id, message.text)
        elif message.content_type == 'sticker':
            bot.send_sticker(message.chat.id, message.sticker.file_id)
        elif message.content_type == 'photo':
            photo = message.photo[-1].file_id
            if hasattr(message, 'caption'):
                caption = message.caption 
            else:
                caption = None
            bot.send_photo(message.chat.id, photo, caption=caption)
        elif message.content_type == 'audio':
            bot.send_audio(message.chat.id, message.audio.file_id)
        elif message.content_type == 'video':
            bot.send_video(message.chat.id, message.video.file_id)
        elif message.content_type == 'voice':
            bot.send_voice(message.chat.id, message.voice.file_id)
        elif message.content_type == 'document':
            bot.send_document(message.chat.id, message.document.file_id)
    except Exception as e:
        print('Помилка:', e)
        bot.send_message(message.chat.id, 'Сталася помилка при відправці повідомлення.')

if __name__ == '__main__':
    bot.polling(none_stop=True)
