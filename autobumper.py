import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

options = uc.ChromeOptions()
driver = uc.Chrome(options=options, use_subprocess=True) 

def autobump(link,msg):
  driver.get(link)
  time.sleep(4)
  driver.find_element(By.XPATH,"/html/body/div[7]/div[1]/div[3]/form/div/div[1]/div[1]/textarea").click()
  time.sleep(2)
  driver.find_element(By.XPATH,"/html/body/div[7]/div[1]/div[3]/form/div/div[1]/div[1]/textarea").send_keys(msg)
  time.sleep(1)
  driver.find_element(By.XPATH,"/html/body/div[7]/div[1]/div[3]/form/div/div[2]/input[1]").click()

sleep_time = 30 * 60
driver.get("http://ogu.gg/login")
driver.find_element(By.XPATH,"/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/div[1]/span/label/input").send_keys("username here")
driver.find_element(By.XPATH,"/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/div[2]/label/input").send_keys("password here")
driver.find_element(By.XPATH,"/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/button/span").click()

time.sleep(10)

try:
  driver.find_element(By.XPATH,'/html/body/div[5]/div/div/a[1]/span')
except:
  print('homepage not detected. Try again!')

time.sleep(10)

for i in range(100000000):
  autobump('https://ogu.gg/Thread-CHEAP-PASTEBIN-AND-EMAIL-OG-USERNAMES','autobumped!')
  autobump('https://ogu.gg/Thread-PSN-2k21-elite-2-rep-Cod-mw2-2022-gta-rdr2-AND-MUCH-MORE-STACKED-ACCOUNT','auto bumping this.')
  autobump('https://ogu.gg/Thread-%E2%AD%90-Selling-Homework-Services-%E2%AD%90','buvmping')
  time.sleep(sleep_time)
