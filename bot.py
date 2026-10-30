from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import TeleBot
from logic import DatabaseManager
from config import TOKEN, DATABASE

bot = TeleBot(TOKEN)
manager = DatabaseManager(DATABASE)

def gen_markup(rows):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 1
    for row in rows:
        markup.add(KeyboardButton(row))
    return markup

@bot.message_handler(commands=['get_aircraft'])
def get_aircraft(message):
    bot.send_message(message.chat.id, "Введите примерное название самолета который вы хотите найти и получит ид:")
    bot.register_next_step_handler(message, name)

def name(message):
    name = message.text
    result = manager.get_by_name(name)
    bot.send_message(message.chat.id, f"Ид '{name}':\n{result}")

@bot.message_handler(commands=['get_col_num'])
def colums(message):
    print('aaaaaaaaaaaaaaaa')
    columns = ['game_id', 'aircraft_class', 'rank', 'max_speed_kmh', 'turn_time_s', 'climb_rate_ms']
    bot.send_message(message.chat.id, "Введите название колонки которую хотите найти:", reply_markup=gen_markup(columns))
    bot.register_next_step_handler(message, get_col_num)

def get_col_num(message):
    print('aaaaaaaaaaaaaaaa')
    colum = message.text
    columns = ['game_id', 'aircraft_class', 'rank', 'max_speed_kmh', 'turn_time_s', 'climb_rate_ms']
    if colum in columns:
        bot.send_message(message.chat.id, "Введите название колонки по которой хотите найти:", reply_markup=gen_markup(columns))
        bot.register_next_step_handler(message, col_num, colum = colum)
    else:
        bot.send_message(message.chat.id, "Неверный. Пожалуйста, выберите из предложенных вариантов.")
        bot.register_next_step_handler(message, colums)

def col_num(message, colum):
    print('aaaaaaaaaaaaaaaa')
    col = message.text
    if col not in ['game_id', 'name', 'aircraft_class', 'rank', 'max_speed_kmh', 'turn_time_s', 'climb_rate_ms']:
        bot.send_message(message.chat.id, "Неверный. Пожалуйста, выберите из предложенных вариантов.")
        bot.register_next_step_handler(message, get_col_num)
    else:
        bot.send_message(message.chat.id, "Введите примерное значение которое вы хотите найти:")
        bot.register_next_step_handler(message, text, col = col, colum = colum)

def text(message, col, colum):
    num = message.text
    print('aaaaaaaaaaaaaaaa')
    result = manager.get_wat_wat(col, num, colum)
    print(len(result))
    try:
        bot.send_message(message.chat.id, f"Результат поиска по колонке '{col}' и значению '{num}':{result}, ({col} и {colum})")
    except Exception as a:
        bot.send_message(message.chat.id, f"Простите произошла ошибка пожалуйста уточните значение.Если ето не поможет то вот код оибки {a}")

bot.infinity_polling()