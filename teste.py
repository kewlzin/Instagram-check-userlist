from  random import randint
import time
import random
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')
print ("Opened Instagram")

sleep(randint(1,4))
username = driver.find_element_by_name('username')
username.send_keys('your_user')
password = driver.find_element_by_name('password')
password.send_keys('your_password')


button_login = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
button_login.click()
sleep(randint(3,5))

f = open("usernames.csv", "r")
data = f.readlines()

for un in data:
  time.sleep(3 * random.random())
  driver.get("https://www.instagram.com/"+str(un[:20]))
  try:
     existe = driver.find_element_by_xpath("//*[contains(text(), 'Esta página não está disponível')]").text
     f2 = open("available.txt", "a")
     f2.write(un)
     f2.close()
  except:
     
     print("Usuário já existe")

  
