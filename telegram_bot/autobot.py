#-*-coding: utf-8-*-


import time
import telepot
import os
token = ""
bot = telepot.Bot(token)

InfoMsg = "하림 메뉴 알리미입니다."

status = True

TEXT_MENU_PATH = "../menu/menu_text.txt"

def input_line_menu(fp, list) : 
  i=0
  while True :
    line = fp.readline()
    if not line : break
    if line == "\n" : continue
    list[i] += line
    i+=1
    if i == 5 : break;


menu_date = ["", "", "", "", ""]
moning_menu = ["", "", "", "", ""]
lunch_a_menu = ["", "", "", "", ""]
lunch_b_menu = ["", "", "", "", ""]
lunch_bibim_menu = ["", "", "", "", ""]
lunch_salad_menu = ["", "", "", "", ""]
dinner_menu = ["", "", "", "", ""]
menu = ["", "", "", "", ""]

menu_mon = "--A메뉴--\n계란볶음밥&짜장소스\n홍합국\n춘권튀김*칠리S\n짜사이채무침\n\n--B메뉴--\n부대찌개국\n옥수수밥\n궁중떡볶이\n치킨너겟*허니머스타드S\n열무된장무침\n\n--Salad--\n맛김치/깍두기\n그린샐러드*키위/오리엔탈D"
menu_tus = "--A메뉴--\n하림반계탕\n쌀밥1/2\n모듬야채스틱*쌈장\n요구르트\n\n--B메뉴--\n고추장제육볶음\n차조현미밥\n미역국\n쑥갓전\n연두부*양념장\n\n--Salad--\n맛김치/깍두기\n그린샐러드*흑임자/오리엔탈D"
menu_wen = "--A메뉴--\n등심돈까스\n감자튀김&후리카케밥\n가쓰오장국\n야채쫄면\n\n--B메뉴--\n콩나물영양밥\n건새우아욱국\n고등어구이\n호박볶음\n김구이*부추양념장\n\n--Salad--\n맛김치/깍두기\n그린샐러드*흑임자/오리엔탈D"
menu_thu = "--A메뉴--\n잔치국수\n김주먹밥\n백순대볶음*양념장\n산고추지무침\n\n--B메뉴--\n춘천닭갈비\n보리밥\n콩가루배추국\n스모크햄전\n와사비무생채\n\n--Salad--\n맛김치/깍두기\n그린샐러드*옥수수/오리엔탈D"
menu_fri = "--A메뉴--\n사골만두국\n혼합잡곡밥\n오징어김치전\n도토리묵야채무침\n\n--B메뉴--\n강된장비빔밥\n계란파국\n메밀전병\n미역줄기볶음\n아이스경단\n\n--Salad--\n맛김치/깍두기\n그린샐러드*딸기/오리엔탈D"

f = open(TEXT_MENU_PATH, 'r')

# Header (not use)
for i in range(6) : 
  line = f.readline()

# Date 
input_line_menu(f, menu_date)

# Moring Menu
for i in range(6) : 
  input_line_menu(f, moning_menu)

# Type (not use)
for i in range(27) : 
  line = f.readline()

# Lunch A
for i in range(3) : 
  input_line_menu(f, lunch_a_menu)

# Lunch B
for i in range(3) : 
  input_line_menu(f, lunch_b_menu)

# Lunch bibimbob
input_line_menu(f, lunch_bibim_menu)

#Lunch salad
for i in range(3) : 
  input_line_menu(f, lunch_salad_menu)

# Type (not use)
for i in range(6) : 
  line = f.readline()

# Dinner
for i in range(6) : 
  input_line_menu(f, dinner_menu)

f.close()

#make menu
for i in range(5) : 
  menu[i] = "\n--A메뉴--\n" + lunch_a_menu[i] + \
            "\n--B메뉴--\n" + lunch_b_menu[i] + \
            "\n--Salad--\n" + lunch_salad_menu[i]

def handle (msg) : 
  content, chat, id = telepot.glance(msg)

  print (content, chat, id)
  print (type(id))

  if content == "text" :
    req_msg = msg["text"].encode("utf-8")
    """
    if req_msg == '/월' : bot.sendMessage(id, menu[0])
    elif req_msg == '/화' : bot.sendMessage(id, menu[1])
    elif req_msg == '/수' : bot.sendMessage(id, menu[2])
    elif req_msg == '/목' : bot.sendMessage(id, menu[3])
    elif req_msg == '/금' : bot.sendMessage(id, menu[4])
    else : 
      bot.sendMessage(id, req_msg)
    """
    if req_msg == '/월' : bot.sendMessage(id, menu_mon)
    elif req_msg == '/화' : bot.sendMessage(id, menu_tus)
    elif req_msg == '/수' : bot.sendMessage(id, menu_wen)
    elif req_msg == '/목' : bot.sendMessage(id, menu_thu)
    elif req_msg == '/금' : bot.sendMessage(id, menu_fri)
    else : 
      bot.sendMessage(id, req_msg)
  else : 
    bot.sendMessage(id, "문자열만 응답을 지원합니다.")

bot.message_loop(handle)

while status == True : 
    time.sleep(10)

