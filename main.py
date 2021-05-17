from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
EMAIL = FACEBOOK_EMAIL
PASSWORD = FACEBOOK_PASSWORD

driver.get("https://tinder.com/")

time.sleep(2)
accept_cookies = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/button")
accept_cookies.click()

login = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login.click()
time.sleep(2)

facebook = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()
time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

facebook_email = driver.find_element_by_name("email")
facebook_email.send_keys(EMAIL)

password = driver.find_element_by_name("pass")
password.send_keys(PASSWORD)

facebook_login = driver.find_element_by_css_selector("#loginbutton input")
facebook_login.click()
time.sleep(5)

driver.switch_to.window(base_window)
print(driver.title)

tinder_location = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
tinder_location.click()
time.sleep(2)

tinder_notification = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
tinder_notification.click()
time.sleep(2)

while True:
    try:
        time.sleep(1)
        swipe = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        swipe.click()
    except NoSuchElementException:
        time.sleep(2)
        swipe = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        swipe.click()

    except ElementClickInterceptedException:
        exit_match = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button')
        exit_match.click()
        time.sleep(2)