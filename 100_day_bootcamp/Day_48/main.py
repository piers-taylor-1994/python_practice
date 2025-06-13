from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
store = driver.find_elements(By.CSS_SELECTOR, "#store div")[::-1]
items_dict = {item.find_element(By.TAG_NAME, "b").text.split()[-1].replace(",", ""):item.get_attribute("id") for item in store if item.find_element(By.TAG_NAME, "b").text}

five_seconds = time.time() + 5
end = time.time() + 60*5

def get_cookie_count():
    return int(driver.find_element(By.ID, "money").text.replace(",", ""))

# def buy_from_store():
#     for item in store:
#         if item.find_element(By.TAG_NAME, "b").text:
#             item_text = item.find_element(By.TAG_NAME, "b").text.split()[-1].replace(",", "")
#             if int(get_cookie_count()) > int(item_text):
#                 item.click()
#                 break

while True:
    cookie.click()
    if time.time() >= five_seconds:
        print("check")
        if get_cookie_count() >= 15:
            for cost, id in items_dict.items():
                if get_cookie_count() > int(cost):
                    driver.find_element(By.ID, id).click()
                    break
        five_seconds = time.time() + 5

    if time.time() >= end:
        print(f"Cookies = {get_cookie_count()}")
        break
    

driver.quit()