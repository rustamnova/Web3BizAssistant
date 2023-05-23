import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Replace YOUR_TOKEN with your Telegram bot token
bot = telebot.TeleBot('6238604932:AAHN-8WET49fAFgtEQsBDhYEJR6V7gNAw7E')

# Start command
@bot.message_handler(commands=['start'])
def start_command(message):
    # Creating a menu with buttons
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(KeyboardButton('Юридические вопросы'), KeyboardButton('Налоги'), KeyboardButton('Поиск компаний'),
             KeyboardButton('Аналитика рынка'))

    # Sending the menu to the user
    bot.send_message(message.chat.id, 'Добро пожаловать в Бизнес Ассистент tada.team', reply_markup=menu)

# Stop command
@bot.message_handler(commands=['stop'])
def stop_command(message):
    # Removing the menu
    remove_menu = ReplyKeyboardRemove()

    # Sending a message to confirm the menu has been removed
    bot.send_message(message.chat.id, 'Меню удалено.', reply_markup=remove_menu)


# Start button
@bot.message_handler(func=lambda message: message.text == 'Start')
def start_button(message):
    # Creating an inline keyboard with the start button
    start_button = InlineKeyboardMarkup()
    start_button.add(InlineKeyboardButton('Start', callback_data='start'))

    # Sending the inline keyboard to the user
    bot.send_message(message.chat.id, 'Нажмите кнопку, чтобы начать:', reply_markup=start_button)

# Stop button
@bot.message_handler(func=lambda message: message.text == 'Stop')
def stop_button(message):
    # Creating an inline keyboard with the stop button
    stop_button = InlineKeyboardMarkup()
    stop_button.add(InlineKeyboardButton('Stop', callback_data='stop'))

    # Sending the inline keyboard to the user
    bot.send_message(message.chat.id, 'Нажмите кнопку, чтобы остановить:', reply_markup=stop_button)

# Callback query handler for the inline buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'start':
        # Do something when the start button is pressed
        bot.answer_callback_query(call.id, text='Starting...')
    elif call.data == 'stop':
        # Do something when the stop button is pressed
        bot.answer_callback_query(call.id, text='Stopping...')

# Start button for specific topics
@bot.message_handler(func=lambda message: message.text == 'Юридические вопросы')
def legal_button(message):
    # Do something when the legal button is pressed
    bot.send_message(message.chat.id, 'Вы выбрали юридические вопросы.')

@bot.message_handler(func=lambda message: message.text == 'Налоги')
def tax_button(message):
    # Do something when the tax button is pressed
    bot.send_message(message.chat.id, 'Вы выбрали налоги.')

@bot.message_handler(func=lambda message: message.text == 'Поиск компаний')
def company_search_button(message):
    # Do something when the company search button is pressed
    bot.send_message(message.chat.id, 'Вы выбрали поиск компаний.')

@bot.message_handler(func=lambda message: message.text == 'Аналитика рынка')
def market_analytics_button(message):
    # Do something when the market analytics button is pressed
    bot.send_message(message.chat.id, 'Вы выбрали аналитику рынка.')

# Stop command
@bot.message_handler(commands=['stop'])
def stop_command(message):
    # Removing the menu
    remove_menu = ReplyKeyboardRemove()

    # Sending a message to confirm the menu has been removed
    bot.send_message(message.chat.id, 'Menu removed.', reply_markup=remove_menu)


# Start button
@bot.message_handler(func=lambda message: message.text == 'Start')
def start_button(message):
    # Creating an inline keyboard with the start button
    start_button = InlineKeyboardMarkup()
    start_button.add(InlineKeyboardButton('Start', callback_data='start'))

    # Sending the inline keyboard to the user
    bot.send_message(message.chat.id, 'Press the button to start:', reply_markup=start_button)

# Stop button
@bot.message_handler(func=lambda message: message.text == 'Stop')
def stop_button(message):
    # Creating an inline keyboard with the stop button
    stop_button = InlineKeyboardMarkup()
    stop_button.add(InlineKeyboardButton('Stop', callback_data='stop'))

    # Sending the inline keyboard to the user
    bot.send_message(message.chat.id, 'Press the button to stop:', reply_markup=stop_button)

# Callback query handler for the inline buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'start':
        # Do something when the start button is pressed
        bot.answer_callback_query(call.id, text='Starting...')
    elif call.data == 'stop':
        # Do something when the stop button is pressed
        bot.answer_callback_query(call.id, text='Stopping...')

# Start the bot
bot.polling()