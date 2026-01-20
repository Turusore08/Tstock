import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt
from extractStock import createplot, getData

code = input("Masukkan kode saham: ")

data = getData(code)

createplot(data,code)