import telebot
from telebot import types
from payment import payment_start
import payment
import donation2
#from save import API_KEY
bot=telebot.TeleBot("6203741928:AAEQ9FykRyvZyEdJBAAnml8JAwXZfkVV4Mg", parse_mode=None)
import telebot

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
        yes_button = types.InlineKeyboardButton('cat', callback_data='cat')
        no_button = types.InlineKeyboardButton('Dog', callback_data='dog')
        yes_no_keyboard = types.InlineKeyboardMarkup().add(yes_button, no_button)
        
        # Send a message with the inline keyboards

        bot.send_message(call.message.chat.id, 'Looking for a reliable and trustworthy pet walking service? Look no further than our company! We specialize in providing exceptional care and attention to your furry friends, ensuring they get the exercise and attention they need.\n Our experienced team of pet walkers are fully trained and equipped to handle all types of dogs, big or small, and will work with you to create a personalized walking schedule that fits your needs and your pets needs.\n \n We pride ourselves on providing a safe and secure environment for your pets, and our team is fully insured and bonded for your peace of mind. Plus, we offer competitive rates and flexible scheduling options to make it easy and convenient for you to keep your pet healthy and happy. \n \n So why wait? Contact us today to schedule your pets first walk with us and experience the difference that our expert pet walking service can make! \n \n WHICH PET DO YOU HAVE?', reply_markup=yes_no_keyboard)
        
    elif color=='cat':
        bot.send_photo(call.message.chat.id, 'https://www.jacksongalaxy.com/wp-content/uploads/2018/08/walk.jpg')
        Mon_button = types.InlineKeyboardButton('Monday', callback_data='Monday')
        Tue_button = types.InlineKeyboardButton('Tuesday', callback_data='Tuesday')
        Wed_button = types.InlineKeyboardButton('Wednsday', callback_data='Wednsday')
        Thu_button = types.InlineKeyboardButton('Thursday', callback_data='Thursday')
        Fri_button = types.InlineKeyboardButton('Friday', callback_data='Friday')
        Sat_button = types.InlineKeyboardButton('Saturday', callback_data='Saturday')
        Sun_button = types.InlineKeyboardButton('Sunday', callback_data='Sunday')
    
        week_keyboard = types.InlineKeyboardMarkup().add(Mon_button, Tue_button, Wed_button, Thu_button, Fri_button, Sat_button, Sun_button)        
        # Send a message with the inline keyboards
        bot.send_message(call.message.chat.id, 'Choose a date?', reply_markup=week_keyboard)
    
    elif color=='dog':
        bot.send_photo(call.message.chat.id, 'https://www.cesarsway.com/wp-content/uploads/2015/06/6-tips-for-mastering-the-dog-walk.jpg')
        Mon_button = types.InlineKeyboardButton('Monday', callback_data='Monday')
        Tue_button = types.InlineKeyboardButton('Tuesday', callback_data='Tuesday')
        Wed_button = types.InlineKeyboardButton('Wednesday', callback_data='Wednesday')
        Thu_button = types.InlineKeyboardButton('Thursday', callback_data='Thursday')
        Fri_button = types.InlineKeyboardButton('Friday', callback_data='Friday')
        Sat_button = types.InlineKeyboardButton('Saturday', callback_data='Saturday')
        Sun_button = types.InlineKeyboardButton('Sunday', callback_data='Sunday')
        week_keyboard = types.InlineKeyboardMarkup().add(Mon_button, Tue_button, Wed_button, Thu_button, Fri_button, Sat_button, Sun_button)        
        # Send a message with the inline keyboards
        bot.send_message(call.message.chat.id, 'Choose a date?', reply_markup=week_keyboard)
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
    elif color=='Monday':
        
        
        one_button = types.InlineKeyboardButton('13-15', callback_data='13-15')
        two_button = types.InlineKeyboardButton('15-17', callback_data='15-17')
        thr_button = types.InlineKeyboardButton('17-19', callback_data='17-19')
        four_button = types.InlineKeyboardButton('19-21', callback_data='19-21')
        week_keyboard = types.InlineKeyboardMarkup().add(one_button, two_button, thr_button, four_button)
        
        
        
        bot.send_message(call.message.chat.id, 'Choose a time?', reply_markup=week_keyboard)
    elif color=='Tuesday':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        A_button = types.KeyboardButton('13:00-15:00')
        B_button = types.KeyboardButton('15:00-17:00')
        C_button = types.KeyboardButton('17:00-19:00')    
        D_button = types.KeyboardButton('19:00-21:00')
        
        markup.add(A_button, B_button, C_button, D_button)
        
        bot.send_message(call.message.chat.id, 'choose a time?', reply_markup=markup)  
    elif color=='Wednsday':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        A_button = types.KeyboardButton('13:00-15:00')
        B_button = types.KeyboardButton('15:00-17:00')
        C_button = types.KeyboardButton('17:00-19:00')    
        D_button = types.KeyboardButton('19:00-21:00')
        
        markup.add(A_button, B_button, C_button, D_button)
        
        bot.send_message(call.message.chat.id, 'choose a time?', reply_markup=markup)  
    elif color=='Thursday':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        A_button = types.KeyboardButton('13:00-15:00')
        B_button = types.KeyboardButton('15:00-17:00')
        C_button = types.KeyboardButton('17:00-19:00')    
        D_button = types.KeyboardButton('19:00-21:00')
        
        markup.add(A_button, B_button, C_button, D_button)
        
        bot.send_message(call.message.chat.id, 'choose a time?', reply_markup=markup)
    elif color=='Friday':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        A_button = types.KeyboardButton('13:00-15:00')
        B_button = types.KeyboardButton('15:00-17:00')
        C_button = types.KeyboardButton('17:00-19:00')    
        D_button = types.KeyboardButton('19:00-21:00')
        
        markup.add(A_button, B_button, C_button, D_button)
        
        bot.send_message(call.message.chat.id, 'choose a time?', reply_markup=markup)
    elif color=='Saturday':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        A_button = types.KeyboardButton('13:00-15:00')
        B_button = types.KeyboardButton('15:00-17:00')
        C_button = types.KeyboardButton('17:00-19:00')    
        D_button = types.KeyboardButton('19:00-21:00')
        
        markup.add(A_button, B_button, C_button, D_button)
        
        bot.send_message(call.message.chat.id, 'choose a time?', reply_markup=markup)
    elif color=='Sunday':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        A_button = types.KeyboardButton('13:00-15:00')
        B_button = types.KeyboardButton('15:00-17:00')
        C_button = types.KeyboardButton('17:00-19:00')    
        D_button = types.KeyboardButton('19:00-21:00')
        
        markup.add(A_button, B_button, C_button, D_button)
     
     
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
        bot.send_message(call.message.chat.id, f"We are delighted to confirm your appointment for pet walking service with our company. Our team is thrilled to have the opportunity to take care of your beloved pet and ensure that they get the exercise and attention they need. \n \n Your appointment is scheduled for [date] at {color}. Our pet walker will arrive at your specified location, equipped with all the necessary tools and equipment to make sure that your pet has a safe and enjoyable walk. \n \n Our team takes great pride in providing exceptional pet walking services, and we are confident that you and your pet will have a wonderful experience with us. Should you have any questions or concerns prior to your appointment, please do not hesitate to contact us. \n \n Thank you for choosing our company for your pet walking needs. We look forward to serving you and your furry friend soon.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Please write /help")      
                       



    


    
    
bot.polling()