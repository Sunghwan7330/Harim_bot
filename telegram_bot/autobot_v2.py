#-*-coding: utf-8-*-


import time
import telepot
import os
token = ""
bot = telepot.Bot(token)

InfoMsg = "하림 메뉴 알리미입니다."

status = True

day_array = ['mon', 'tue', 'wen', 'thu', 'fri']
image_path = "../menu/image_menu"
image_file = image_path + '/{}_lunch_all.jpg'

def handle (msg) : 
  content, chat, id = telepot.glance(msg)

  print (content, chat, id)
  print (type(id))

  if content == "text" :
    req_msg = msg["text"].encode("utf-8")
    if req_msg == '/월' : bot.sendPhoto(id, photo=open(image_file.format(day_array[0]), 'rb'))
    elif req_msg == '/화' : bot.sendPhoto(id, photo=open(image_file.format(day_array[1]), 'rb'))
    elif req_msg == '/수' : bot.sendPhoto(id, photo=open(image_file.format(day_array[2]), 'rb'))
    elif req_msg == '/목' : bot.sendPhoto(id, photo=open(image_file.format(day_array[3]), 'rb'))
    elif req_msg == '/금' : bot.sendPhoto(id, photo=open(image_file.format(day_array[4]), 'rb'))
    else : 
      bot.sendMessage(id, req_msg)
  else : 
    bot.sendMessage(id, "문자열만 응답을 지원합니다.")

bot.message_loop(handle)

while status == True : 
    time.sleep(10)
