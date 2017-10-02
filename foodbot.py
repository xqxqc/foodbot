import sys
import time
import telepot
from telepot.loop import MessageLoop
from food_func import welcome_keyboard,hcts_keyboard,vcts_keyboard,acts_keyboard,nearest_canteen,canteen_keyboard_select
#start message


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    
    if content_type =='text':

        
                        
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

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
