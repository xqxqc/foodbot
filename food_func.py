# !/usr/local/bin/python3
#  _*_ coding:utf8 _*_

import telepot
import time
from telepot.namedtuple import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton


bot = telepot.Bot('02707033:AAFbGsQBdQKN_0GMqNs-SqRco-nAda5iPfc')


# ============= markup keyboards for 3-level requests ===============
# display clicable buttons for users to choose

# === primary requests: service selection ===
# by replay keyboards
# function reutrn: selected service
def welcome_keyboard():
    tmp=ReplyKeyboardMarkup(keyboard=
    [
    [KeyboardButton(text='Get_Location', request_location=True)],
    ],
    one_time_keyboard=True
    )
    return tmp

def Food_Preference_keyboard():
	tmp = ReplyKeyboardMarkup(keyboard=
	[
		[KeyboardButton(text = 'Halal Preference')],
		[KeyboardButton(text = 'Vegeterian')]
		[KeyboardButton(text = 'No Preference')]
	],
	one_time_keyboard=True
	)
	return tmp




