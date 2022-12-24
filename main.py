import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
import string
import random

options = uc.ChromeOptions()
driver = uc.Chrome(options=options, use_subprocess=True) 

def autobump(link,msg):
  driver.get(link)
  time.sleep(4)
  driver.find_element(By.XPATH,"/html/body/div[7]/div[1]/div[3]/form/div/div[1]/div[1]/textarea").click()
  time.sleep(4)
  driver.find_element(By.XPATH,"/html/body/div[7]/div[1]/div[3]/form/div/div[1]/div[1]/textarea").send_keys(msg)
  time.sleep(4)
  driver.find_element(By.XPATH,"/html/body/div[7]/div[1]/div[3]/form/div/div[2]/input[1]").click()
  print(Fore.GREEN + 'message sent!: ' + msg)

sleep_time = 1000
driver.get("http://ogu.gg/login") 
driver.find_element(By.XPATH,"/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/div[1]/span/label/input").send_keys("username")
driver.find_element(By.XPATH,"/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/div[2]/label/input").send_keys("password")
driver.find_element(By.XPATH,'/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/button/span').click()
time.sleep(10)

try:
  driver.find_element(By.XPATH,'/html/body/div[5]/div/div/a[1]/span')
  print('homepage was found! Continuing. ')
except:
  print('homepage not detected. Try again! Closing window.')
  driver.close()

time.sleep(5)

letters = string.digits

for i in range(100000000):
  autobump('https://ogu.gg/Thread-CHEAP-PASTEBIN-AND-EMAIL-OG-USERNAMES',str(''.join(random.choice(letters) for i in range(10))) + ' a;#6937') ## my personal message here + random number generator to avoid detection
  time.sleep(10)
  autobump('https://ogu.gg/Thread-PSN-2k21-elite-2-rep-Cod-mw2-2022-gta-rdr2-AND-MUCH-MORE-STACKED-ACCOUNT',str(''.join(random.choice(letters) for i in range(10))) + ' a;#6937')
  time.sleep(10)
  autobump('https://ogu.gg/Thread-%E2%AD%90-Selling-Homework-Services-%E2%AD%90',str(''.join(random.choice(letters) for i in range(10))) + ' a;#6937')
  time.sleep(sleep_time)
