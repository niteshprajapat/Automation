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

        

        def signIN():
            try :
                sign_in = driver.find_element(By.LINK_TEXT, "Sign In")
                sign_in.click()

                ask = pyautogui.prompt("Do you have an account ?")

                if (ask == "No" or ask == "no" or ask == "NO") :
                    sleep(2)
                    ask_query = pyautogui.prompt("Do you want to create new one ? ")
                    sleep(2)
                    if ask_query == "YES" or ask_query == "yes" or ask_query == "Yes":
                        sleep(2)
                        create_acc = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div/div[3]/div[6]/div/p/button/b')
                        create_acc.click()
                        sleep(2)

                        choice = pyautogui.prompt("Select any one ......")
                        sleep(2)
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

                            pyautogui.alert("Please Solve the reCaptcha puzzle..... and Continue ...")        
                                    
                            #################################

                        elif choice == "google":
                            google_option = driver.find_element(By.ID, 'susi-modal-google-button')
                            google_option.click()

                            def google_func():


                                email_add = pyautogui.prompt("Enter your valid Email Address :: ")
                                sleep(1)

                                email_signin = driver.find_element(By.ID, 'identifierId')
                                email_signin.send_keys(email_add, Keys.ENTER)

                                pwd = pyautogui.password("Enter password here....")
                                sleep(1)
                            
                            google_func()

                        
                        elif choice == "facebook":
                            fb_option = driver.find_element(By.ID, 'susi-modal-fb-button').click()
                            sleep(2)

                            email_fb = pyautogui.prompt("Enter your Email here..")
                            email_fb_add = driver.find_element(By.ID, 'email')
                            email_fb_add.send_keys(email_fb)
                            sleep(2)
                            pwd_fb = pyautogui.prompt("Enter your Password here..")
                            pwd_fb_add = driver.find_element(By.ID, 'pass')
                            pwd_fb_add.send_keys(email_fb, sleep(2) ,Keys.ENTER)


### starts from here --->>>>>>
### starts from here --->>>>>>

                elif (ask == "yes" or ask == "Yes" or ask == "YES"):   
                    sleep(2)
                    ask_option = str(pyautogui.prompt("Enter Sign-in Option- Google, Facebook, Apple, Twitter, Email"))
                    sleep(1)

                    if ask_option == "google":
                        googlee = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div/div[3]/div[1]/a').click()
                        sleep(1)

                        email_add = pyautogui.prompt("Enter your valid Email Address :: ")
                        sleep(1)

                        email_signin = driver.find_element(By.ID, 'identifierId')
                        email_signin.send_keys(email_add, Keys.ENTER)

                        pwd = pyautogui.password("Enter password here....")
                        sleep(1)
            except Exception as e:
                print("Sign-In Error")

        ohk = pyautogui.prompt("Let's get started.....\n Enter your option..- Sign In, Get Started, Our Story, Membership, Write..")
        sleep(10)
        if ohk == str("sign in"):
            signIN()
                    
        sleep(5)

        # driver.quit()

    except Exception as e:
        print("Error Found!!")

# medium_blog()

if __name__ == '__main__':
    sleep(10)
    medium_blog()

    # elif:
    #     pass

    