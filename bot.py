from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui


chromedriver_path = 'C:/Users/Nitesh Prajapati/Downloads/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("https://www.spacex.com")

sleep(5)

############################################### 

def falcon_9():
    falcon_btn = driver.find_element(By.LINK_TEXT,"Falcon 9").click()
    sleep(4)

################################################

def falcon_heavy():
    pass


################################################

def dragon():
    pass

################################################

def starship():
    pass

################################################

def human_spaceflight():
    pass

#################################################

def rideshare():
    pass