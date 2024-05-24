# from binance.client import Client
# api_key=""
# api_secret=""
# client=Client(api_key,api_secret)
# def track_crypto_price(coin):
#     if coin=="BTC":
#         bitcoinprise=client.get_symbol_ticker(symbol="BTCUSDT")
#         price= bitcoinprise["price"]
#         return f" текусщий курс битка ={price}"
#     else:
#         return " ошибка получение данных"
# #if __name__ == "__main__":
#    # track_crypto_price("BTC")
import telebot
from telebot import types
import requests
import qrcode as qc
bot = telebot.TeleBot('7183066891:AAF24OiExccNTc1cTCMcsBuLPOnaJqU7Oik')

def generateqr(link,filename):
    qrur=qc.main.QRCode(
        version=1,
        error_correction=qc .constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qrur.add_data(link)
    qrur.make(fit=True)
    img=qrur.make_image(fill_color="black", back_color="white")
    img.save(filename)


def get_kripto():
    url="https://api.binance.com/api/v3/ticker/price"
    responce=requests.get(url)
    data=responce.json()
    #print(data)
    filtered_data = {item['symbol']: item['price'] for item in data if item['symbol'] in ['BTCUSDT', 'BNBUSDT', 'ETHUSDT','SOLUSDT',"DOGEUSDT"]}
    return filtered_data

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello,<b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['information'])
def information(message):
    mess='hello dear user, this bot will help you with crypto currency, it will announce the cryptocurrency rate and inform you when you can sell and when you can buy\n\n/binance'
    bot.send_message(message.chat.id,mess, parse_mode='html')

@bot.message_handler(commands=['crypto'])
def cryptu(message):
    mess="here you can find out in detail the cryptocurrency rate\n"
    content="/BTC find out about Bitcoi\n /BNB find out about Binance Coin\n /ETH find out about Ethereum \n /SOL find out about SOLANA \n /DOGE find out about DOGECOIN"
    mess=mess+content
    bot.send_message(message.chat.id,mess, parse_mode='html')

@bot.message_handler(commands=["BTC"])
def BTC(message):
    rates=get_kripto()
    BTCarte=rates.get("BTCUSDT","N/A")
    m=f"BTC rate:{BTCarte} USDT"
    bot.send_message(message.chat.id, m, parse_mode='html')

@bot.message_handler(commands=["BNB"])
def BNB(message):
    rates=get_kripto()
    BNBkrard=rates.get("BNBUSDT","N/A")
    m=f"BNB rate:{BNBkrard} USTD"
    bot.send_message(message.chat.id, m, parse_mode='html')

@bot.message_handler(commands=["ETH"])
def ETH(message):
    rates=get_kripto()
    ETHkrard=rates.get("ETHUSDT","N/A")
    m=f"ETH rate:{ETHkrard} USTD"
    bot.send_message(message.chat.id, m, parse_mode="html")
@bot.message_handler(commands=["SOL"])
def SOL(message):
    rates=get_kripto()
    SOLCard=rates.get("SOLUSDT","N/A")
    m=f"SOL rate:{SOLCard} USDT"
    bot.send_message(message.chat.id,m,parse_mode="html")
@bot.message_handler(commands=["DOGE"])
def DOGE(message):
    rates=get_kripto()
    DOGECard=rates.get("DOGEUSDT","N\A")
    m=f"DOGECOIN retes:{DOGECard} USDT"
    bot.send_message(message.chat.id,m,parse_mode="html")

@bot.message_handler(commands=["binance"])
def bin(message):
    foto=open("qr.png","rb")
    bot.send_photo(message.chat.id,foto)
    bot.send_message(message.chat.id,"https://www.binance.com/pl")

@bot.message_handler(commands=["buycrypto"])
def buycrypto(message):
    bot.send_message(message.chat.id,"Which of the cryptos do you want to buy?")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buyBTC=types.KeyboardButton("/buyBTC")
    buyBNB=types.KeyboardButton("/buyBNB")
    buyETH=types.KeyboardButton("/buyETH")
    markup.add(buyBTC,buyBNB,buyETH)
    bot.send_message(message.chat.id, 'Click on', reply_markup=markup)

@bot.message_handler(commands=["buyBTC"])
def buyBTC(message):
    bot.send_message(message.chat.id,"link to buy BTC:https://www.binance.com/en/price/bitcoin")
@bot.message_handler(commands=["buyBNB"])
def buyBNB(message):
    bot.send_message(message.chat.id,"link to buy BNB:https://www.binance.com/en/price/BNB")
@bot.message_handler(commands=["buyETH"])
def buyETH(message):
    bot.send_message(message.chat.id,"link to buy ETH :https://www.binance.com/pl/crypto/buy/PLN/ETH")

@bot.message_handler(commands=['menu'])
def menu(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start=types.KeyboardButton('/start')
    inform=types.KeyboardButton('/information')
    crypto=types.KeyboardButton('/crypto')
    buycrypto=types.KeyboardButton("/buycrypto")
    markup.add(start,inform,crypto, buycrypto)
    bot.send_message(message.chat.id, 'Click on', reply_markup=markup)


bot.polling(none_stop=True)
#get_kripto()
