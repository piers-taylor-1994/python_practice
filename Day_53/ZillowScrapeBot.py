from bs4 import *
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ZillowScrapeBot:
    def __init__(self):
        site = requests.get(os.environ["ZILLOW_URL"], headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}).text
        self.soup = BeautifulSoup(site, "html.parser")

    def scrape_apartments(self):
        apartments_dict = {
            i:{
                "address": a.select_one("address").getText().strip().replace("|", ""),
                "price": a.select_one(".PropertyCardWrapper__StyledPriceLine").getText(),
                "link": a.select_one("a")["href"]
            } for (i, a) in enumerate(self.soup.select(".List-c11n-8-84-3-photo-cards li")) if a.select_one("address")}
        return apartments_dict