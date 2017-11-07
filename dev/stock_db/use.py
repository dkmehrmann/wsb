from stock import Stock
from stock_db import db,stock,ohlc
s = Stock()

symbol = 'MSFT'
start_date = '2017-10-15'
end_date = '2017-10-29'

stock_range = s.grab_range(symbol,start_date,end_date)

if stock_range[0]=='cant pull currently' or stock_range[0]=='cant scrape':
	print stock_range[0]
else:
	for day in stock_range:
		print day
		print day.Date
		print day.Open 
		print day.High
		print day.Low
		print day.Close
		print day.AdjClose
		print day.Volume
