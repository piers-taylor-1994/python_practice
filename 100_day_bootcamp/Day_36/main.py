import requests
from datetime import *
import math
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "ITFX68JFP9SGENZP"
NEWS_API_KEY = "5113d93a4d4642829487c1b29faa0ba9"

def month_fixer(m):
    if m < 10:
        return "0" + str(m)
    return str(m)

yesterday_date = date.today() + timedelta(days=-1)
while yesterday_date.weekday() == 6 or yesterday_date.weekday() == 5:
    yesterday_date += timedelta(days=-1)
daybefore_yesterday_date = yesterday_date + timedelta(days=-1)
while daybefore_yesterday_date.weekday() == 6 or daybefore_yesterday_date.weekday() == 5:
    daybefore_yesterday_date += timedelta(days=-1)

# stock_response = requests.get("https://www.alphavantage.co/query", {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": "TSLA",
#     "apikey": "ITFX68JFP9SGENZP"
# })
# stock_response.raise_for_status()

# stock_response_dates = [value for (key, value) in stock_response.json()["Time Series (Daily)"].items()]

# yesterday_closing = stock_response_dates[0]["4. close"]
# daybefore_yesterday_closing = stock_response_dates[1]["4. close"]

# yesterday_closing = stock_response.json()["Time Series (Daily)"][f"{yesterday_date.year}-{month_fixer(yesterday_date.month)}-{yesterday_date.day}"]["4. close"]
# daybefore_yesterday_closing = stock_response.json()["Time Series (Daily)"][f"{daybefore_yesterday_date.year}-{month_fixer(daybefore_yesterday_date.month)}-{daybefore_yesterday_date.day}"]["4. close"]

# stock_closing_diff = round((float(yesterday_closing) - float(daybefore_yesterday_closing)) / float(yesterday_closing) * 100)

stock_closing_diff = 5

if abs(stock_closing_diff) >= 5:
    news_response = requests.get("https://newsapi.org/v2/everything", {
        "q": COMPANY_NAME,
        "from": yesterday_date,
        "apiKey": NEWS_API_KEY
    })
    news_response.raise_for_status()
    news_response_articles = [{"headline":a["title"], "brief":a["description"]} for a in news_response.json()["articles"][:3]]
 
    arrow = ""
    if stock_closing_diff > 0:
        arrow = "🔺"
    else:
        arrow = "🔻"

    body = f"{STOCK}: {arrow}{stock_closing_diff}%"
    for a in news_response_articles:
        body += f"\nHeadline: {a["headline"]}\nBrief: {a["brief"]}"
    print(body)