import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt

def is_valid_symbol(code):
    ticker = yf.Ticker(code)
    info = ticker.info
    return info != {}

def getData(code:str):

    today = date.today()
    data = yf.download(f"{code}.jk",start=today.replace(year=today.year-1),end=today)
    
    if data.empty:
        print(f"{code} tidak valid. silahkan cek ulang")
        return 

    return data

def createplot(data,code):

    if not is_valid_symbol(code + ".jk"):
        print(f"{code} tidak valid. silahkan cek ulang")
        return 

    if data.empty:
        print(f"data tidak valid. silahkan cek ulang")
        return
    data['Close'].plot(title=f"Harga Saham {code} per hari")
    plt.xlabel("Hari")
    plt.ylabel("Harga Rp.")
    plt.savefig(f"Saham {code}.jpg",dpi= 300, bbox_inches ='tight')
    