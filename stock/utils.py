import twstock
import pandas as pd

def generate_stock_ids():
    all_stocks = twstock.codes

    for stock_id, stock_info in all_stocks.items():
        yield stock_id, stock_info.name


def get_stock_price(stock_name):
    stock = twstock.Stock(stock_name)
    target_price = stock.fetch_from(2020, 5)

    columns = [
        'Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change',
        'Transcation'
    ]

    # Convert data to DataFrame
    data = [[
        item.date, item.capacity, item.turnover, item.open, item.high, item.low, item.close, item.change, item.transaction
    ] for item in target_price]

    df = pd.DataFrame(data, columns = columns)

    # Save to CSV
    df.to_csv('stock_0050.csv', index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    get_stock_price('0050')
