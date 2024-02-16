# BROWSER AUTOMATION USING SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("--headless")
# chrome_option.headless=True
driver=webdriver.Chrome(options=chrome_option)

driver.get("https://the-internet.herokuapp.com/login")


Username=driver.find_element(By.ID,"username")
Username.send_keys("tomsmith") # to send text  in text bar
# Username.send_keys(Keys.RETURN) # to send it  in google 


password=driver.find_element(By.ID,"password")
password.send_keys("SuperSecretPassword!") # to send text  in text bar
# password.send_keys(Keys.RETURN) # to send it  in google 


submit=driver.find_element(By.CLASS_NAME,"radius")
submit.send_keys(Keys.RETURN) # to send it  in google 

message_element=driver.find_element(By.CLASS_NAME,'subheader')
print(message_element.text)





time.sleep(5)  #close te website with in sec as given in bracketx


driver.close()