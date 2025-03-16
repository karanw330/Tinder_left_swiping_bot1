from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = webdriver.Chrome(options=chrome_options)
url.get("https://www.tinder.com")

wait = WebDriverWait(url, 10)


time.sleep(2)

login = url.find_element(By.XPATH,
                             '//*[@id="u-1184541582"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login.click()

try:
    time.sleep(1)
    fb = url.find_element(By.XPATH,
                          '//*[@id="u-963201146"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
    fb.click()
except NoSuchElementException:
    time.sleep(2)
    #more_options_div = url.find_element(By.CLASS_NAME,
                                    #'qJTHM')
    more_options = url.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button')
    more_options.click()
    time.sleep(1)
    fb_ = url.find_element(By.XPATH,
                          '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
    fb_.click()



url.implicitly_wait(3)

fb_xp = '//*[@id="u-963201146"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div'

url.implicitly_wait(5)

time.sleep(2)


base_window = url.window_handles[0]
fb_login_window = url.window_handles[1]
url.switch_to.window(fb_login_window)

fb_email = url.find_element(By.XPATH, '//*[@id="email"]')
fb_email.send_keys("sunehrigulambi@gmail.com")

fb_pass = url.find_element(By.XPATH, '//*[@id="pass"]')
fb_pass.send_keys("K@R@N7682")

fb_login = url.find_element(By.NAME, 'login')
fb_login.click()

url.implicitly_wait(4)

time.sleep(5)
continue_button = url.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span')
continue_button.click()

url.switch_to.window(base_window)

time.sleep(1)
location_allow = url.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]/div')
location_allow.click()

time.sleep(1)
notification = url.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[2]/div[2]/div[2]/div')
notification.click()

cookie_decline_xpath = '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]/div'
cookie_decline = url.find_element(By.XPATH, cookie_decline_xpath)
cookie_decline.click()

time.sleep(5)

'''for i in range(1,21):
    try:
        time.sleep(2)
        random_element = url.find_element(By.TAG_NAME, "body")
        random_element.send_keys(Keys.ARROW_LEFT)
    except NoSuchElementException:
        time.sleep(2)
        print("error")'''

for n in range(100):
    try:
        time.sleep(1)
        print("disliking...")
        like_buttons = url.find_elements(By.CSS_SELECTOR, "[class*='button Lts']")
        for button in like_buttons:
            if button.text == "NOPE": button.click()
    except ElementClickInterceptedException:
        time.sleep(1)
        dont_allow = url.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button[2]/div[2]/div[2]/div')
        dont_allow.click()
#tinder changes its xpath after every requests so it's better to find the button by its text

url.quit()

