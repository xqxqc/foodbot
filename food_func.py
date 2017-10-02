# !/usr/local/bin/python3
#  _*_ coding:utf8 _*_

import telepot
from telepot.namedtuple import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton

#might not be needed, determine if canteens are open
import time

TOKEN = '402707033:AAFbGsQBdQKN_0GMqNs-SqRco-nAda5iPfc'

bot = telepot.Bot(TOKEN)


# ============= markup keyboards for 3-level requests ===============
# display clicable buttons for users to choose

# === primary requests: service selection ===
# by replay keyboards
# function reutrn: selected service
def Welcome_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text='Get_Location', request_location=True)],
    ],
    one_time_keyboard=True
    )
    return tmp

def Food_Preference_Keyboard():
    tmp = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Halal Preference')],
    [KeyboardButton(text = 'Vegeterian')]
    [KeyboardButton(text = 'No Preference')]
    ],
    one_time_keyboard=True
    )
    return tmp


#any canteens without halal? will have to remove
def Halal_Preference_Keyboard():
    tmp = InlineKeyboardMarkup(keyboard = [
    [dict(text = 'Canteen 1', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 2', callback_data = 'hl')],
    [dict(text = 'Canteen 4', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 9', callback_data = 'hl')],
    [dict(text = 'Canteen 11', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 13', callback_data = 'hl')],
    [dict(text = 'Canteen 14', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 16', callback_data = 'hl')],
    [dict(text = 'North Hill Canteen', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'North Spine Canteen', callback_data = 'hl')],
    [dict(text = 'South Spine Canteen', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'NIE Canteen', callback_data = 'hl')]
    ])
    return tmp

def No_Preference_Keyboard():
    tmp = InlineKeyboardMarkup(keyboard = [
    [dict(text = 'Canteen 1', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 2', callback_data = 'hl')],
    [dict(text = 'Canteen 4', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 9', callback_data = 'hl')],
    [dict(text = 'Canteen 11', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 13', callback_data = 'hl')],
    [dict(text = 'Canteen 14', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 16', callback_data = 'hl')],
    [dict(text = 'North Hill Canteen', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'North Spine Canteen', callback_data = 'hl')],
    [dict(text = 'South Spine Canteen', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'NIE Canteen', callback_data = 'hl')]
    ])
    return tmp        

def Vegetarian_Preference_Keyboard():
    tmp = InlineKeyboardMarkup(keyboard = [
    [dict(text = 'Canteen 1', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 2', callback_data = 'hl')],
    [dict(text = 'Canteen 4', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 9', callback_data = 'hl')],
    [dict(text = 'Canteen 11', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 13', callback_data = 'hl')],
    [dict(text = 'Canteen 14', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'Canteen 16', callback_data = 'hl')],
    [dict(text = 'North Hill Canteen', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'North Spine Canteen', callback_data = 'hl')],
    [dict(text = 'South Spine Canteen', callback_data = 'hl')],
    [InlineKeyboardButton(text = 'NIE Canteen', callback_data = 'hl')]
    ])
    return tmp

