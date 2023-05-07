import telebot
from telebot import types
from payment import payment_start
import payment
import donation2
import requests
from bs4 import BeautifulSoup
#from save import API_KEY
bot=telebot.TeleBot("6211666522:AAH4tI0D1xD0qIAi3Yv_yho0EJ7s8t-QSec", parse_mode=None)
import telebot
supported = ['Alice\n', 'Betty\n', 'Blaze\n', 'Kacper\n', 'Kacper\n', 'Iga\n', 'Nina\n', 'Dorian\n', 'Alicja\n', 'Emilia\n', '/dog']
# This dictionary will store the user's full names
user_names = {}

@bot.message_handler(commands=['start'])
def ask_name(message):
    # Check if the user's name is already stored
    user_id = message.chat.id
    if user_id in user_names:
        last_name = user_names[user_id].split()[-1]
        bot.reply_to(message, f"Welcome back, {last_name}!")
    else:
        # Ask the user to enter their full name
        bot.reply_to(message, "Hello! Please enter your full name.")
        bot.register_next_step_handler(message, save_name)

def save_name(message):
    # Store the user's full name in the dictionary
    user_id = message.chat.id
    user_names[user_id] = message.text
    last_name = user_names[user_id].split()[-1]
    
    
    bot.send_photo(message.chat.id, "https://s3.amazonaws.com/ellevate-app-uploads-production/image_uploads/25208/original/2.png?1505278391", caption =f"Welcome {last_name}!! please press press /help to see our services")
    
@bot.message_handler(commands=['help'])
def help(message):
    # Ask the user for their favorite color using an inline keyboard
    keyboard = types.InlineKeyboardMarkup()
    colors = ['Electricity payment', 'Walking pets', 'Donating clothes']
    buttons = [types.InlineKeyboardButton(color, callback_data=color) for color in colors]
    keyboard.add(*buttons)
    bot.reply_to(message, "How can we help you today?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    # Save the user's favorite color from the inline keyboard
    color = call.data
    if color == 'Donating clothes':
        keyboard = types.InlineKeyboardMarkup()
        button_click_here = types.InlineKeyboardButton('Donation Clothes', callback_data='/start_clothes_donate')
        keyboard.add(button_click_here)
        bot.send_message(call.message.chat.id, 'Welcome to Clothes Donation! Please click the button below to continue:', reply_markup=keyboard)
        donation2.bot = bot
        bot.register_next_step_handler(call.message, donation2.donation_start)
    elif color == '/start_clothes_donate':
        bot.send_message(call.message.chat.id, 'Please, enter your fullname?') 
        bot.register_next_step_handler(call.message, donation2.get_donation_info2)
    
    elif color == 'Walking pets':
        # Send a love sticker
        bot.send_photo(call.message.chat.id, 'https://www.shutterstock.com/image-photo/portrait-cat-dog-looking-camera-260nw-1929069635.jpg')
        
        # Send a message with the inline keyboards

        bot.send_message(call.message.chat.id, 'Welcome to see information about your dog. please click\n /cat\n /dog\n to see supported names /supported_names')
        
    


    elif color=='Electricity payment':    
        bot.send_photo(call.message.chat.id, 'https://www.jaipurstuff.com/wp-content/uploads/2022/09/pay-advance-electricity-bill.jpg')
        keyboard = types.InlineKeyboardMarkup()
        button_click_here = types.InlineKeyboardButton('Electricity Pay', callback_data='/payment_start')
        keyboard.add(button_click_here)
        bot.send_message(call.message.chat.id, 'Please click the button below to continue:', reply_markup=keyboard)
        payment.bot = bot
        #bot.register_next_step_handler(call.message, payment_start)
    elif color == '/payment_start':
        bot.send_message(call.message.chat.id, 'Please, enter your fullname?') 
        bot.register_next_step_handler(call.message, payment.get_response2)
    
     
    #Ainella's code, please do not remove   
    elif color == 'Card':
        bot.send_message(call.message.chat.id, 'Please, enter your card number')
        bot.register_next_step_handler(call.message, payment.get_responce5)   
    elif color == 'Direct debit':
        bot.send_message(call.message.chat.id, 'Can I offer for you Direct Debit? This option will be automatically debited from your account every month, you do not need to remember to pay the bill.\n/Yes or /No')
        bot.register_next_step_handler(call.message, payment.get_responce6) 
    elif color == 'Go to Bank':
        bot.send_message(call.message.chat.id, 'Please be sure to pay the full amount before the next invoice arrives.Goodbye!')
   
   
   
   
    else:
        bot.send_message(call.message.chat.id, f"Please click /cat or /dog")
@bot.message_handler(commands=['cat', 'dog'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the dog information bot. Please enter the name of a dog to get its information.")

@bot.message_handler(commands=['supported_names'])
def show_parse_help(message):
    bot.send_message(message.from_user.id, f"I am able to find the information only for the following dogs:\n {' '.join(supported)}")
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Get the name of the dog from the user input
    dog_name = message.text.strip().lower()
    
    # Parse the website using BeautifulSoup
    #response = requests.get('https://www.worldometers.info/coronavirus/')
    #soup = BeautifulSoup(response.text, 'html.parser')
    
    with open('Echin.html') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # Find the table rows containing the dog's information
    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip().lower() for col in cols]
        if dog_name in cols:
            # If the dog's name is found, send its information to the user
            bot.reply_to(message, f"Name: {cols[0]}\nGender: {cols[1]}\nBreed: {cols[2]}\nLast_appointment: {cols[3]}\nBehaviour: {cols[4]}\nLast_payment: {cols[6]}")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Please write /help")      
                       



    


    
    
bot.polling()
