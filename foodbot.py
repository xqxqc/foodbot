import time
import sys
import telepot
from telepot.loop import MessageLoop
from food_func import Welcome_Keyboard, Halal_Preference_Keyboard, No_Preference_Keyboard, Vegetarian_Preference_Keyboard

#start message


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
                        bot.sendMessage(chat_id, 'Welcome to NTU Food Bot, \nWhat can I do for you?', reply_markup=Welcome_Keyboard())
        #=============== REQUEST FOR LOCATION ========================
        elif content_type == 'Get_Location':
		#================= Do location stuff here. Nearest dist can use Pythagoreas ===============
                
                print("Do location stuff here")
                bot.sendMessage(chat_id, 'Please select your food preference', reply_markup=Food_Preference_keyboard())

#============================== IF ALL GOES CALL BACK QUERY THIS SHOULD NOT BE RUNNED =======================
def on_callback_query(msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        print('Callback Query:', query_id, from_id, query_data)

        print ('ERROR: THIS SHOULD NOT BE RUNNING - BY ROLAND, testing inline kb m8')
        bot.answerCallbackQuery(query_id, text='Got it, please wait a fucking moment... ')

        if query_data=='hl':
                print('yes! halal')


TOKEN = '402707033:AAFbGsQBdQKN_0GMqNs-SqRco-nAda5iPfc'

bot = telepot.Bot(TOKEN)

#let it auto receive msg
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)
