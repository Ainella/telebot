import telebot
from telebot import types
#bot = telebot.TeleBot("6203741928:AAEQ9FykRyvZyEdJBAAnml8JAwXZfkVV4Mg")
global bot
type = {}
size = {}
condition = {} 
location = {}
donation_info = {}
fullname = {}


#@bot.message_handler(content_types=['text']) 


def donation_start(message):

    if message.text == '/donation_start':

        bot.send_message(message.from_user.id, 'Hello,do you want to donate clothes?\n/Yes or /No')

        bot.register_next_step_handler(message, get_donation_info1)

    elif message.text == '/help':

        bot.send_message(message.from_user.id, 'Write /start')

    else:

        bot.send_message(message.from_user.id, 'I do not understand , write /help.')

   

def get_donation_info1(message):

    if message.text == '/Yes' or message.text == 'Yes':

        bot.send_message(message.from_user.id, 'Please, enter your fullname?') 

        bot.register_next_step_handler(message, get_donation_info2)

    elif message.text == '/No' or message.text == 'No':

        bot.send_message(message.from_user.id, 'I apologise, I wont be able to help you, Good day') 

    elif message.text == '/help':

        bot.send_message(message.from_user.id, 'Write /Yes')

        bot.register_next_step_handler(message, get_donation_info1)

    else :

        bot.send_message(message.from_user.id, 'I do not understand, write /help') 




def get_donation_info2(message):

    fullname[message.from_user.id] = message.text

    bot.send_message(message.from_user.id, 'Please,enter type of clothes for donation ie shirts, pants, jackets?')

    bot.register_next_step_handler(message, get_donation_info3)




def get_donation_info3(message):

    type[message.from_user.id] = message.text

    bot.send_message(message.from_user.id, 'Please enter the state or condition of the clothes you wish to donate eg old or new?')
    bot.register_next_step_handler(message, get_donation_info4)

def get_donation_info4(message):
    condition[message.from_user.id] = message.text
    
    bot.send_message(message.from_user.id, 'Please,enter the size  of clothes for donation ie small, medium, large, extralarge?')

    bot.register_next_step_handler(message, get_donation_info5)
    
    
def get_donation_info5(message):
    size[message.from_user.id] = message.text
    bot.send_message(message.from_user.id, 'Please,enter the preferred pick up location for donated clothes?')

    bot.register_next_step_handler(message, get_donation_info6)
    
    
    
def get_donation_info6(message):

    location[message.from_user.id] = message.text
    bot.send_message(message.from_user.id, 'Pleaseconfirm the donation\n/Confirm')
    bot.register_next_step_handler(message, get_confirmation)
    

def get_confirmation(message):
    if message.text == '/Confirm' or message.text == 'Confirm':
        bot.send_message(message.from_user.id, 'Thank you for your donation! Your clothes will be given to those in need. If you have any questions or concerns, please contact us at donation@charity.com.')
    
    else:
        bot.send_message(message.from_user.id, 'I do not understand, write /Confirm')
        bot.register_next_step_handler(message, get_confirmation)  
               
    bot.send_message(message.from_user.id, 'Thank you for your donation ' + fullname[message.from_user.id] + ' you are donating ' + type[message.from_user.id] + ' of size ' + size[message.from_user.id] + '. Thank you for your time!')

        



#bot.polling(none_stop=True, interval=0)



