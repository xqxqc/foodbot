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
    [KeyboardButton(text='Nearest', request_location=True)],
    ],
    one_time_keyboard=True
    )
    return tmp

def hcts_keyboard():
    tmp=ReplyKeyboardMarkup(keyboard=
    [
    [KeyboardButton(text='Nearest', request_location=True)],

    [KeyboardButton(text='Best')],

    ],
    one_time_keyboard=True
    )
    return tmp

def vcts_keyboard():
    tmp=ReplyKeyboardMarkup(keyboard=
    [
    [KeyboardButton(text='Nearest', request_location=True)],

    [KeyboardButton(text='Best')],

    ],
    one_time_keyboard=True
    )
    return tmp

def acts_keyboard():
    tmp=ReplyKeyboardMarkup(keyboard=
    [
    [KeyboardButton(text='Nearest', request_location=True)],

    [KeyboardButton(text='Best')],

    ],
    one_time_keyboard=True
    )
    return tmp
#inline
def canteen_keyboard_select(n):
	# work in progress
    halal_keyboard=InlineKeyboardMarkup(inline_keyboard=
        [
    	[InlineKeyboardButton(text='cantenn 1',callback_data='hcts')],
	[InlineKeyboardButton(text='canteen 2',callback_data='hcts')],
        [InlineKeyboardButton(text='canteen 4',callback_data='hcts')],
    	[InlineKeyboardButton(text='canteen 9',callback_data='hcts')],
        [InlineKeyboardButton(text='canteen 11',callback_data='hcts')],
    	[InlineKeyboardButton(text='canteen 13',callback_data='hcts')],
        [InlineKeyboardButton(text='canteen 14',callback_data='hcts')],
    	[InlineKeyboardButton(text='canteen 16',callback_data='hcts')],
        [InlineKeyboardButton(text='North Hill canteen',callback_data='hcts')],
    	[InlineKeyboardButton(text='North Spine canteen',callback_data='hcts')],
        [InlineKeyboardButton(text='South spine canteen',callback_data='hcts')],
    	[InlineKeyboardButton(text='NIE canteen',callback_data='hcts')],
        ]
        )




# ============= calculation of the nearest library ===============
# by comparing the distance between current location and different libraries
# function parameter: coordinate of current location
# function return: index of the nearest library
def nearest_canteen(x,y):
    dis=99999999
    n=0
    if (pow(x-1.346736,2)+pow(y-103.686092,2) < dis):#can 1
        dis = pow(x-1.346736,2)+pow(y-103.686092,2)
        n=0   	
    if (pow(x-1.348329,2)+pow(y-103.685547,2) < dis):
        dis = pow(x-1.348329,2)+pow(y-103.685547,2) #can 2
        n=1
    if (pow(x-1.344169,2)+pow(y-103.685429,2) < dis):#can 4
        dis = pow(x-1.344169,2)+pow(y-103.685429,2)
        n=2
    if (pow(x-1.352216,2)+pow(y-103.685265,2) < dis):#can 9
        dis = pow(x-1.352216,2)+pow(y-103.685265,2)
        n=3
    if (pow(x-1.354903,2)+pow(y-103.686477,2) < dis):#can 11
        dis = pow(x-1.354903,2)+pow(y-103.686477,2)
        n=4
    if (pow(x-1.351722,2)+pow(y-103.681100,2) < dis):#can 13
        dis = pow(x-1.351722,2)+pow(y-103.681100,2)
        n=5
    if (pow(x-1.352648,2)+pow(y-103.682108,2) < dis):#can 14
        dis = pow(x-1.352648,2)+pow(y-103.682108,2)
        n=6
    if (pow(x-1.350299,2)+pow(y-103.680917,2) < dis):#can 16
        dis = pow(x-1.350299,2)+pow(y-103.680917,2)
        n=7
#north hill north spine south spine nie

    return n




