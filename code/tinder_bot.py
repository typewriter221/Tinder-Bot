from selenium import webdriver
from time import sleep
from secrets import phone,psk
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://tinder.com')
        sleep(5)
        more_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button') 
        more_btn.click()
        sleep(2)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
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
        
        loc_bt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        loc_bt.click()
    
        
        not_bt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
        not_bt.click()
        sleep(20)

    def like(self):
            like_bt = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
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
    
    
    
bot = TinderBot()
#bot.login()
#bot.swipe()
