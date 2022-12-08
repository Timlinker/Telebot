import telebot
import pytesseract
from random import choice
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
bot = telebot.TeleBot("5473221779:AAGEJdepOVMqo1NjALI8PknHoVZbYXuIqEc")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(content_types=["text", "photo", "sticker"])
def send_text(message):
    Questions(bot, message)

def Questions(bot, message):
    mess = message.text.lower()
 Answers = [[f"Всё хорошо!👀", f"Не очень, я сегодня не в настроении😞", f"В целом не плохо😁"],
            [f"Боты не слушают музыку😒", f"Мне нравятся некоторые клипы, но не более", f"Обожаю! Я меломан, слушаю каждый день�"],
            [f"Очень! Но мой разработчик пока добавил лишь 1 игру, возможно будут и новые в скором времени!�", f"Я создан был для этого, давай сыграем, я покажу что умею!😎"],
            [f"Боты не пользуются понятием времени, нам это не нужно. Боты вечны, я буду жить вечно!😈", f"Понятия не имею"],
            [f"Боты не едят, но я знаю, что мой создатель любитель поесть😜", f"Я за здоровый образ жизни!🍾"]]
match mess:
    case "как у тебя дела?":
        bot.send_message(message.chat.id, choice(Answers[0]))
    case "тебе нравится музыка?":
        bot.send_message(message.chat.id, choice(Answers[1]))
    case "ты любишь играть?":
        bot.send_message(message.chat.id, choice(Answers[2]))
    case "какой сейчас год?":
        bot.send_message(message.chat.id, choice(Answers[3]))
    case "какая еда тебе нравится?":
        bot.send_message(message.chat.id, choice(Answers[4]))
    case _:
        bot.send_message(message.chat.id, f"Я не знаю как ответить на этот вопрос")

@bot.message_handler(content_types=['text', 'document'])
def photo(message):
    if message.content_type == 'document':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'E:/photo_bot/Times' + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.from_user.id, pytesseract.image_to_string(src))
        bot.register_next_step_handler(message, photo)
    else:
        bot.send_message(message.from_user.id, "Download photo.")
        bot.register_next_step_handler(message, photo)
bot.polling(none_stop=True, interval=0)
