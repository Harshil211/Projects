from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
from urllib.parse import quote
import time

# Load message
with open(r'D:\Coding\Coding\NIKOL KISHOR MANDAL\message_followp.txt', 'r', encoding='utf-8') as file:
    msg = quote(file.read())

# Load numbers
numbers = []
with open(r'D:\Coding\Coding\NIKOL KISHOR MANDAL\numbers_leader.txt', 'r', encoding='utf-8') as file:
    for num in file.readlines():
        numbers.append(num.strip())

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com')
print("Please scan the QR code...")
time.sleep(15)  # Wait for QR code scan

# Start sending messages
for num in numbers:
    try:
        print(f"Sending message to {num}...")
        link = f'https://web.whatsapp.com/send/?phone=91{num}&text={msg}'
        driver.get(link)
        time.sleep(15)  # Wait for page to load and input box to be ready

        # Send message
        action = ActionChains(driver)
        action.send_keys(Keys.ENTER).perform()
        time.sleep(10)

    except InvalidSessionIdException:
        print(f"Session lost while sending to {num}, skipping.")
    except WebDriverException as e:
        print(f"WebDriverException: {e.msg}, skipping {num}.")
    except Exception as e:
        print(f"Unexpected error: {e}, skipping {num}.")

print("Done sending all messages.")
time.sleep(30)  # Let user see last message before browser closes
driver.quit()
