from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui


chromedriver_path = 'C:/Users/Nitesh Prajapati/Downloads/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=chromedriver_path)

def medium_blog():
    try:
        sleep(5)
        driver.get("https://medium.com/")
        driver.maximize_window()
        sleep(2)

        sign_in = driver.find_element(By.LINK_TEXT, "Sign In")
        sign_in.click()

        ask = pyautogui.prompt("Do you have an account ?")

        if ask == "No" or ask == "no" or ask == "NO":
            ask_query = pyautogui.prompt("Do you want to create new one ? ")
            if ask_query == "YES" or ask_query == "yes" or ask_query == "Yes":
                create_acc = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div/div[3]/div[6]/div/p/button/b')
                create_acc.click()

                choice = pyautogui.prompt("Select any one ......")
                if choice == 'email':
                    email_option = driver.find_element(By.ID, 'email-susi-button-text')
                    email_option.click()
                    sleep(4)

                    your_email_address = pyautogui.prompt("Your Email Address.......")
                    sleep(2)

                    email_type = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div/div/div[2]/div/p/input')
                    email_type.send_keys(your_email_address, Keys.ENTER)


                    ############## reCaptcha experiment #############

                    # while True:
                    #     generate_captcha = pyautogui.prompt("Want to generate new re-Captcha code ?? ")
                    #     if generate_captcha == "yes":
                    #         driver.find_element(By.ID, 'recaptcha-reload-button').click()
                    #         sleep(1)
                    #     elif not (generate_captcha == "yes"):
                    #         # driver.close()
                    #         pass

                    pyautogui.prompt("Please Solve the reCaptcha puzzle..... and Continue ...")        
                            
                    OK = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[1]/div/div[1]/div[3]/div/button').click()
                    

                    #################################
                    
        sleep(5)

        # driver.quit()

    except Exception as e:
        print("Error Found!!")

medium_blog()
