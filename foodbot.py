import sys
import time
import telepot
from telepot.loop import MessageLoop
from food_func import welcome_keyboard,hcts_keyboard,vcts_keyboard,acts_keyboard,nearest_canteen,canteen_keyboard_select
#start message

#help message

#canteen list init
canfood=['can1','2','4','9','11','13','14','16']


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    
    if content_type =='text':

        if msg['text']=='/start':
            bot.sendMessage(chat_id, 'Where are you now?', reply_markup=welcome_keyboard())
            
        elif msg['text'].find("1") == 1:
            n=canfood.index(msg['text'])
            bot.sendMessage(chat_id, 'Please choose your canteen', reply_markup=canteen_keyboard_select(n))
        elif msg['text']=='Vegetarian Canteen':
            bot.sendMessage(chat_id, 'Please choose your canteen', reply_markup=vcts_keyboard())    
        elif msg['text']=='Any Canteen':
            bot.sendMessage(chat_id, 'Please choose your canteen', reply_markup=acts_keyboard())
        else:
            bot.sendMessage(chat_id, 'Input proper command?', reply_markup=welcome_keyboard())

    if content_type =='location':
        n=nearest_canteen(msg['location']['latitude'],msg['location']['longitude'])
        print(n)
        bot.sendMessage(chat_id, 'The nearest is canteen'+canfood[n]+'\nChoose your destination', reply_markup=acts_keyboard())#using inline

        
#for inline
                        
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
