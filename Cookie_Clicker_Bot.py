from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Selenium Web Driver for Google Chrome Browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def check_current_money():
    remain_money = driver.find_element(By.ID, value="money").text.replace(" ", "")
    return int(remain_money)

def checking_feature_price(feature):
    current_feature = feature.text.split("\n")[0]
    current_price = current_feature.split("-")[1].strip(" ").replace(",","")
    return(int(current_price))

def check_feature_element():
    cursor = driver.find_element(By.ID, value="buyCursor")
    grandma = driver.find_element(By.ID, value="buyGrandma")
    factory = driver.find_element(By.ID, value="buyFactory")
    mine = driver.find_element(By.ID, value="buyMine")
    shipment = driver.find_element(By.ID, value="buyShipment")
    alchemy = driver.find_element(By.ID, value="buyAlchemy lab")
    portal = driver.find_element(By.ID, value="buyPortal")
    time_machine = driver.find_element(By.ID, value="buyTime machine")
    return [cursor, grandma, factory, mine, shipment, alchemy, portal, time_machine]

def feature_click(feature):
    feature.click()

def end_game():
    return False

continue_game = True 

# Cookie Clicker bot
cookie_clicker = driver.find_element(By.ID, value="cookie")

while continue_game == True:
    cookie_clicker.click()
    feature_element = check_feature_element()
    feature_element.reverse()
    current_money = check_current_money()

    # End Game when time machine feature could be buy
    if current_money >= checking_feature_price(feature_element[0]):
        continue_game = end_game()

    # Check each feature could be buy in descending price order
    for i in range(8):
        if current_money >= checking_feature_price(feature_element[i]):
            feature_click(feature_element[i])

    time.sleep(0.05) # time sleep less than 0.05s raise potential to stale element error
