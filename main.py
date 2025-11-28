import telebot
from taskManager import TaskManager

token=''
bot=telebot.TeleBot(token)

taskManager = TaskManager()

cache = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет чувак ✌️ ")

@bot.message_handler(commands=['show'])
def start_message(message):
    tasks = taskManager.get_str_tasks()
    bot.send_message(message.chat.id,f"{tasks}")

@bot.message_handler(commands=['create'])
def create_task(message):
    chat_id = message.chat.id
    cache[str(chat_id)] = {}
    msg = bot.reply_to(message, "введите название задачи")
    bot.register_next_step_handler(msg, process_name)

def process_name(message):
    try:
        chat_id = message.chat.id
        cache[str(chat_id)]['name'] = message.text
        msg = bot.reply_to(message, 'Введите описание задачи')
        bot.register_next_step_handler(msg, process_desc)
    except Exception as e:
        bot.reply_to(message, 'ошибочка')

def process_desc(message):
    try:
        chat_id = message.chat.id
        cache[str(chat_id)]['desc'] = message.text
        taskManager.create_task(cache[str(chat_id)]['name'], cache[str(chat_id)]['desc'])
        bot.reply_to(message, 'Задача успешно добавлена!')
    except Exception as e:
        bot.reply_to(message, 'что-то не так')

bot.infinity_polling()

