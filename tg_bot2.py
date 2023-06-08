import requests
import telebot

# Create a new Telegram Bot instance
bot = telebot.TeleBot('5823020818:AAEcYppS_CVVKY2t_wZmR-fN8Ehlwmka9nY')

# Search API
def search_organizations(api_key, query_params):
    url = f"https://api.checko.ru/v2/search?key={api_key}&{query_params}"
    response = requests.get(url)
    return response.json()

# Handler for the /start command
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, 'Welcome to the Search Bot! Please enter your search query.')

# Handler for search request
@bot.message_handler(func=lambda message: True)
def search_handler(message):
    query_params = message.text
    api_key = 'm0YsKyAXxQXHcn8k'  # Replace with your API key
    data = search_organizations(api_key, query_params)
    bot.reply_to(message, str(data))  # Sending the JSON response as a reply

# Start the bot
bot.polling()
