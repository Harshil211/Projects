from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

with open(r'D:\Coding\Coding\NIKOL KISHOR MANDAL\message_sbha.txt', 'r', encoding='utf-8') as file:
    msg = file.read()
msg = quote(msg)

numbers = []
with open(r'D:\Coding\Coding\NIKOL KISHOR MANDAL\number_member.txt', 'r', encoding='utf-8') as file:
    for num in file.readlines():
        numbers.append(num.strip())
        
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(15)
for num in numbers:
    link2 = f'https://web.whatsapp.com/send/?phone=91{num}&text={msg}'
    driver.get(link2)
    time.sleep(15)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(10)
time.sleep(20000)
