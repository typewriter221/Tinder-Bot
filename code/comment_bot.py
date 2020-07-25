from selenium import webdriver
#from selenium import Keys
from time import sleep
from secrets import phone,psk

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

class FbBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://facebook.com')
        sleep(5)
        phone_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        phone_in.send_keys(phone)
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(psk)
        login_bt = self.driver.find_element_by_xpath('//*[@id="u_0_b"]')
        login_bt.click()
        
    def send(self):
        send_bt = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        send_bt.click()
    def text(self):
        
        text=self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[3]/div/div/div[1]/div/div/div/div[4]/div[2]/div/div[2]/div[13]/div/div/div/div/div/div/div/div/div/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div/div/div/div/form/div[2]/div/div[2]/div/div/div/div')
        text.send_keys(' Congrats',u'\ue007')



    def deploy(self):
        try :
            for i in range (10):
                sleep(0.5)
                self.text()
                
        except :
            print("In Exception")
            sleep(5)
            self.deploy()
        

            
    

        
    
    
bot = FbBot()
#bot.comment()
#bot.auto()
