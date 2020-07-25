from selenium import webdriver
from time import sleep
#from secrets import phone,psk
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

class EmojiBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://web.whatsapp.com')
        sleep(5)
        
    def send(self):
        send_bt = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        send_bt.click()
    def text(self):
        text=self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
        text.send_keys(' hmmm')
    def like(self):
            like_bt = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
            like_bt.click()
    def deploy(self):
        for i in range (10000000):
            bot.text()
            bot.send()
            sleep(1)

    
bot = EmojiBot()
bot.login()
#bot.swipe()
#emoji panel //*[@id="main"]/footer/div[1]/div[1]/div/button[2]
