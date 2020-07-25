from selenium import webdriver
from time import sleep
from secrets import phone,psk
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

class BumbleBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://bumble.com')
        sleep(5)
        signnin_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a') 
        signnin_btn.click()
        
        sleep(5)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div')
        fb_btn.click()
        base_win = self.driver.window_handles[0]
        login_win = self.driver.window_handles[1]
        self.driver.switch_to_window(login_win)
        phone_in = self.driver.find_element_by_xpath('//*[@id="email"]') 
        phone_in.send_keys(phone)
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(psk)
        login_bt = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_bt.click()
        self.driver.switch_to_window(base_win)
        sleep(10)
        
        #loc_bt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        #loc_bt.click()
        #not_bt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
        #not_bt.click()
        sleep(20)

    def like(self):
            like_bt = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')
            
            like_bt.click()
    def swipe(self):
        try :
            while True:
                sleep(0.5)
                self.like()
        except :
            print("In Exception")
            sleep(5)

            self.swipe()


    
bot = BumbleBot()
bot.login()
#bot.swipe()