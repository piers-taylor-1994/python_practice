from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# number_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(number_of_articles.text)
# number_of_articles.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

input1 = driver.find_element(By.NAME, "fName")
input1.send_keys("Piers")
input2 = driver.find_element(By.NAME, "lName")
input2.send_keys("Taylor")
input3 = driver.find_element(By.NAME, "email")
input3.send_keys("piers.taylorr@gmail.com")
input4 = driver.find_element(By.CLASS_NAME, "btn-block")
input4.click()
# input1.send_keys(Keys.ENTER)

input("")