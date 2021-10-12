from time import sleep 
from selenium import webdriver 

browser = webdriver.Chrome() 
browser.implicitly_wait(5) 

browser.get('https://www.instagram.com/') #opens the webpage

#login_link = browser.find_element_by_xpath("//a[text()='Log in']")
#login_link.click() 

sleep(15)  #waits for 30 seconds for the browser to load

username_input = browser.find_element_by_css_selector("input[name='username']") 
#input the username by finding the field by css selector
password_input = browser.find_element_by_css_selector("input[name='password']") 
#same thing as previous

username_input.send_keys("_stalker_tales_") #presses enter
password_input.send_keys("$shushant123") 

login_button = browser.find_element_by_xpath("//button[@type='submit']") 
#finds the login button by xpath
login_button.click() 
#clicks on the login button

sleep(20)

save_info = browser.find_element_by_css_selector("//button[text()='not now']")
#does not saves the login info
save_info.click()
#clicks on the button after finding it

sleep(5) 

browser.close(5)
