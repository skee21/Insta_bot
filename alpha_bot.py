from time import sleep

class login:
	def __init__(self, browser):
		self.browser = browser

	def loginin(self, username, password):
		username_input = "#your_username"

self.browser.find_element_by_css_selector("input[name='username']")
password_input = "#your_password"

self.browser.find_element_by_css_selector("input[name='password']")
username_input.send_keys(username)
password_input.send_keys(password)
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(10)

class home:
        def __init__(self, browser):
        	self.browser = browser
        	self.browser.get('https://www.instaram.com/')

        def comeback(self):
        	self.browser.find_element_by_xpath("//a[text()='log in']")
        	sleep(5)
        	return login(self.browser)

def test(browser):
	home = homepage(browser)
	login_page = homepage.comeback
	login_page.login("#your_username","#your_password")

	errors = browser.find_element_by_css_selector('#error_message')
	assert len(errors) == 0
