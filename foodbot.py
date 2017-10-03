import time
import sys
import telepot
import math
from telepot.loop import MessageLoop
from food_func import Welcome_Keyboard, Halal_Preference_Keyboard, No_Preference_Keyboard, Vegetarian_Preference_Keyboard, Food_Preference_Keyboard, Nearest_Canteen

#start message

canfood=['canteen 1','canteen 2','canteen 4','canteen 9','canteen 11','canteen 13','canteen 14','canteen 16','north hill canteen','north spine canteen','south spine canteen','nie canteen']

def on_chat_message(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

        if content_type =='text':
                if msg['text'] == 'Halal Preference':
                        #================== This means its a Halal reply ============
                        #==================
                        # 1. Get all canteens nearby
                        # 2. Reorder based on 1) Halal, and 2) distance
                        # 3. Entire program should end here.
                        


 
                        print("I prefer Halal lol")
                        bot.sendMessage(chat_id, 'Which canteen?', reply_markup = Halal_Preference_Keyboard())


                elif msg['text'] == 'No Preference':
                        #================== No halal preference ============
                        #================== Same as above ==================
                        print("I don't care haha")
                        bot.sendMessage(chat_id, 'Which canteen?', reply_markup = No_Preference_Keyboard())

                elif msg['text'] == 'Vegetarian':
			#============== I prefer Vegeterian ================
			#================== Same as above ==================
                        print("I'm a fuckin Vegetarian")
                        bot.sendMessage(chat_id, 'Which canteen?', reply_markup = Vegetarian_Preference_Keyboard())

                else :#user to give location / type food preference
                        bot.sendMessage(chat_id, 'Welcome to NTU Food Bot, \nWhat can I do for you?', reply_markup = Welcome_Keyboard())
        #=============== REQUEST FOR LOCATION ========================
        elif content_type == 'Get_Location':
                
        elif content_type == 'location':
                #================= Do location stuff here. Nearest dist can use Pythagoreas ===============
                print("Do location stuff here")

                n = Nearest_Canteen(msg['location']['latitude'],msg['location']['longitude'])
                print(n)
                
                bot.sendMessage(chat_id, 'The nearest is '+canfood[n]+', do keep that in mind.\nChoose your food preference', reply_markup = Food_Preference_Keyboard())
                
                #bot.sendMessage(chat_id, 'The nearest canteen is ', canteenfood[n], 'Please select your food preference', reply_markup = Food_Preference_Keyboard())

#============================== IF ALL GOES CALL BACK QUERY THIS SHOULD NOT BE RUNNED =======================
def on_callback_query(msg):
        query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
        print('Callback Query:', query_id, from_id, data)

        bot.answerCallbackQuery(query_id, text='Got it, please wait a fuckin moment... ')

        if data =='hl':
                print('yes! halal - looking up the database....')
        if data =='nil':
                print('yes! no pref - looking up the database....')
        if data =='veg':
                print('yes! vegetariain - looking up the database....')

TOKEN = '402707033:AAFbGsQBdQKN_0GMqNs-SqRco-nAda5iPfc'

bot = telepot.Bot(TOKEN)

#let it auto receive msg
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)
