import twstock
import pandas as pd

target_stock = '0050'
stock = twstock.Stock(target_stock)
target_price = stock.fetch_from(2020, 5)

name_attribute = [
    'Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change',
    'Transcation'
]