import sys
import time
import telepot
from telepot.loop import MessageLoop
from food_func import welcome_keyboard, Halal_keyboard
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
		elif msg['text'] == 'No Preference':
			#================== No halal preference ============
			#================== Same as above ==================
			print("I don't care haha")
		elif msg['text'] == 'Vegeterian':
			#============== I prefer Vegeterian ================
			#================== Same as above ==================
			print("I'm a fuckin Vegeterian")


		else :
			await bot.sendMessage(chat_id, 'Welcome to NTU Food Bot, \n What can I do for you?', reply_markup=welcome_keyboard())
    #=============== REQUEST FOR LOCATION =========================
	elif content_type == 'Get_Location':
		#================= Do location stuff here. Nearest dist can use Pythagoreas ===============
		print("Do location stuff here")
		await.bot.sendMessage(chat_id, 'Please select your food preference', reply_markup=Food_Preference_keyboard())
                        
#============================== IF ALL GOES CALL BACK QUERY THIS SHOULD NOT BE RUNNED =======================
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
	print ('ERROR: THIS SHOULD NOT BE RUNNING - BY ROLAND')
    bot.answerCallbackQuery(query_id, text='Got it, please wait... ')
    if query_data=='hcts':
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
