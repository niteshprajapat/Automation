from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chromedriver_path = 'C:/Users/Nitesh Prajapati/Downloads/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("https://www.spacex.com")

sleep(5)

############################################### 

