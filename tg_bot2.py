import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Replace YOUR_TOKEN with your Telegram bot token
bot = telebot.TeleBot('5823020818:AAEcYppS_CVVKY2t_wZmR-fN8Ehlwmka9nY')

# Start command
@bot.message_handler(commands=['start'])
def start_command(message):
    # Creating a menu with buttons
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(KeyboardButton('/company'), KeyboardButton('/entrepreneur'), KeyboardButton('/person'),
             KeyboardButton('/search'), KeyboardButton('/finances'), KeyboardButton('/contracts'),
             KeyboardButton('/inspections'), KeyboardButton('/enforcements'), KeyboardButton('/legal_cases'),
             KeyboardButton('/bank'))

    # Sending the menu to the user
    bot.send_message(message.chat.id, 'Welcome to the API 2.0 menu. Please select an API request:', reply_markup=menu)

# Company command
@bot.message_handler(commands=['company'])
def company_command(message):
    # Do something when the /company command is issued
    bot.send_message(message.chat.id, 'You selected the /company command. Do something with the company API request.')

# Entrepreneur command
@bot.message_handler(commands=['entrepreneur'])
def entrepreneur_command(message):
    # Do something when the /entrepreneur command is issued
    bot.send_message(message.chat.id, 'You selected the /entrepreneur command. Do something with the entrepreneur API request.')

# Person command
@bot.message_handler(commands=['person'])
def person_command(message):
    # Do something when the /person command is issued
    bot.send_message(message.chat.id, 'You selected the /person command. Do something with the person API request.')

# Search command
@bot.message_handler(commands=['search'])
def search_command(message):
    # Do something when the /search command is issued
    bot.send_message(message.chat.id, 'You selected the /search command. Do something with the search API request.')

# Finances command
@bot.message_handler(commands=['finances'])
def finances_command(message):
    # Do something when the /finances command is issued
    bot.send_message(message.chat.id, 'You selected the /finances command. Do something with the finances API request.')

# Contracts command
@bot.message_handler(commands=['contracts'])
def contracts_command(message):
    # Do something when the /contracts command is issued
    bot.send_message(message.chat.id, 'You selected the /contracts command. Do something with the contracts API request.')

# Inspections command
@bot.message_handler(commands=['inspections'])
def inspections_command(message):
    # Do something when the /inspections command is issued
    bot.send_message(message.chat.id, 'You selected the /inspections command. Do something with the inspections API request.')

# Enforcements command
@bot.message_handler(commands=['enforcements'])
def enforcements_command(message):
    # Do something when the /enforcements command is issued
    bot.send_message(message.chat.id, 'You selected the /enforcements command. Do something with the enforcements API request.')

# Legal cases command
@bot.message_handler(commands=['legal_cases'])
def legal_cases_command(message):
    # Do something when the /legal_cases command is issued
    bot.send_message(message.chat.id, 'You selected the /legal_cases command. Do something with the legal cases API request.')

# Bank command
@bot.message_handler(commands=['bank'])
def bank_command(message):
    # Do something when the /bank command is issued
    bot.send_message(message.chat.id, 'You selected the /legal_cases command. Do something with the legal cases API request.')

# Start the bot
bot.polling()