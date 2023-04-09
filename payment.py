import telebot
import random
import re
from datetime import datetime 
from telebot import types
#bot = telebot.TeleBot("6203741928:AAEQ9FykRyvZyEdJBAAnml8JAwXZfkVV4Mg")
global bot
fullname = {}
acc = {}
card_number = {} 
expiry_date = {}
balance = {}
UMR = {}

#@bot.message_handler(content_types=['text']) 

def payment_start(message):
    if message.text == '/payment_start':
        bot.send_message(message.from_user.id, 'Hello,do you want to pay for electricity?\n/Yes or /No')
        bot.register_next_step_handler(message, get_response1)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Write /start')
    else:
        bot.send_message(message.from_user.id, 'I do not understand , write /help.')
   
def get_response1(message):
    if message.text == '/Yes' or message.text == 'Yes':
        bot.send_message(message.from_user.id, 'Please, enter your fullname?') 
        bot.register_next_step_handler(message, get_response2)
    elif message.text == '/No' or message.text == 'No':
        bot.send_message(message.from_user.id, 'Sorry, I can not help you, Goodbye') 
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Write /Yes')
        bot.register_next_step_handler(message, get_response1)
    else :
        bot.send_message(message.from_user.id, 'I do not understand, write /help') 

def get_response2(message):
    fullname[message.from_user.id] = message.text
    bot.send_message(message.from_user.id, 'Please,enter account number?')
    bot.register_next_step_handler(message, get_responce3)

def get_responce3(message):
    acc[message.from_user.id] = message.text
    balance[message.from_user.id] = random.randint(20,500)
    bot.send_message(message.from_user.id, 'Your outstanding balance is '  + str(balance[message.from_user.id]) + ' euro')
    markup = types.InlineKeyboardMarkup()
    methods = ['Card', 'Direct debit', 'Go to Bank']
    buttons = [types.InlineKeyboardButton(method, callback_data=method) for method in methods]
    markup.add(*buttons)
    bot.send_message(message.from_user.id, "How do you want to pay?", reply_markup=markup)
    
        
def get_responce5(message):
    if re.search("^\d{4} \d{4} \d{4} \d{4}$", message.text) == None:
        bot.send_message(message.from_user.id, 'Please, enter your a valid card number')
        bot.register_next_step_handler(message, get_responce5)  
    else:
        card_number[message.from_user.id] = message.text  
        bot.send_message(message.from_user.id, 'Please,enter expiry date')
        bot.register_next_step_handler(message, get_responce8)

def get_responce6(message):
    if message.text == '/Yes' or message.text == 'Yes':
        bot.send_message(message.from_user.id, 'Please, enter your IBAN number (2 Letters,2 digits,2 Letter,2 digits)')
        bot.register_next_step_handler(message, get_responce7)
    elif message.text == '/No' or message.text == 'No':
        bot.send_message(message.from_user.id, 'You can pay in bank. Goodbye!')
    else:
        bot.send_message(message.from_user.id, 'I do not understand, write /Yes or /No')
        bot.register_next_step_handler(message, get_responce4)
    
def get_responce7(message):
    if re.search("^[A-Z]{2} \d{2} [A-Z]{2} \d{2}$", message.text) == None:
        bot.send_message(message.from_user.id, 'Please, enter your a valid IBAN number (2 Letters,2 digits,2 Letter,2 digits)')
        bot.register_next_step_handler(message, get_responce7)  
    else:
        card_number[message.from_user.id] = message.text  
        bot.send_message(message.from_user.id, 'Please, write Confirm ' + fullname[message.from_user.id])
        bot.register_next_step_handler(message, get_responce9)

def get_responce9(message):
    UMR[message.from_user.id] = random.randint(000,100)
    if message.text == '/Confirm' or message.text == 'Confirm':
        bot.send_message(message.from_user.id, 'Your UMR is ' + str(UMR[message.from_user.id]) )
        bot.send_message(message.from_user.id, 'Thank you for your payment ' + fullname[message.from_user.id] + ' your account number is ' + acc[message.from_user.id] + ' you paid ' + str(balance[message.from_user.id]) + ' euro. Goodbye!')
    else:
        bot.send_message(message.from_user.id, 'I do not understand, write /Yes or /No')
        bot.register_next_step_handler(message, get_responce4)   
    
def get_responce8(message):
    if re.search("^\d{2}/\d{2}$", message.text) == None:
        bot.send_message(message.from_user.id, 'Please, enter a valid  expire date')
        bot.register_next_step_handler(message, get_responce6) 
    elif datetime.strptime(message.text, '%m/%y') < datetime.today():
         bot.send_message(message.from_user.id, 'Your card is expired,please enter a valid expire date') 
         bot.register_next_step_handler(message, get_responce6)    
    else:
        expiry_date[message.from_user.id] = message.text    
        bot.send_message(message.from_user.id, 'Thank you for your payment ' + fullname[message.from_user.id] + ' your account number is ' + acc[message.from_user.id] + ' you paid ' + str(balance[message.from_user.id]) + ' euro. Goodbye!')

#bot.polling(none_stop=True, interval=0)