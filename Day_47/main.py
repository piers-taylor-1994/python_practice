import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

TARGET = 100.00
URL = "https://www.amazon.com/dp/B075CYMYK6?th=1"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}


site = requests.get(URL, headers=HEADERS).text
soup = BeautifulSoup(site, "html.parser")

# price = soup.find(name="span", class_="aok-offscreen").getText()[2::]
price = soup.find(name="span", class_="a-price-symbol").getText() + soup.find(name="span", class_="a-price-whole").getText() + soup.find(name="span", class_="a-price-fraction").getText()
price_without_sign = price.split("$")[1].strip()
price_as_float = float(price_without_sign)

if price_as_float < TARGET:
    product_title = soup.find(name="span", id="productTitle").getText().strip()
    message = f"{product_title} is on sale for {price}!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS_FROM"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS_FROM"],
            to_addrs=os.environ["EMAIL_ADDRESS_TO"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )