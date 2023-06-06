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
    bot.send_message(message.chat.id, 'Please enter the OGRN or INN of the company you want to check:')
    bot.register_next_step_handler(message, process_company_input)

def process_company_input(message):
    query = message.text.strip()
    api_key = 'm0YsKyAXxQXHcn8k'  # Replace with your API key
    url = f"https://api.checko.ru/v2/company?key={api_key}&{query}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the data as per your requirements
        # You can extract specific information from the JSON response and send it as a message to the user
        bot.send_message(message.chat.id, f"Company details: {data}")
    else:
        bot.send_message(message.chat.id, "An error occurred while retrieving company information. Please try again.")

# Entrepreneur, person, search, finances, contracts, inspections, enforcements, legal_cases, bank commands

# ...

# Start the bot
bot.polling()
