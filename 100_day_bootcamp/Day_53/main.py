from ZillowScrapeBot import *
from GoogleSheetsBot import *

zillow_scrape_bot = ZillowScrapeBot()
google_sheets_bot = GoogleSheetsBot()
apartments = zillow_scrape_bot.scrape_apartments()
google_sheets_bot.fill_in_google_sheets(apartments)