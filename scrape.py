from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget
import time

file_path = 'chromedriver.exe'
driver = webdriver.Chrome(file_path)


driver.get("http://www.instagram.com")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

u_name = ""
with open('creds.txt', 'r') as file:
    for line in file:
        u_name+=line

u_name = u_name.split('\n')

username.clear()
username.send_keys(u_name[0])

password.clear()
password.send_keys(u_name[1])

Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

searchbox = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[1]")))


searchbox.click()

searchbox = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search' and @type='text']")))

keyword = "raw_japan__"
searchbox.send_keys(keyword)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

#scroll
n_scrolls = 1000

images = []
for i in range(1, n_scrolls):
    #select images
    images_list = driver.find_elements_by_tag_name('img')
    images_list = [image.get_attribute('src') for image in images_list]
    images_list = images_list[:-2] #slicing-off IG logo and Profile picture
    images.extend(images_list)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)


images = list(set(images))

print('Found ' + str(len(images)) + ' images')

time.sleep(10)

# for a in anchors:
#     driver.get(a)
#     time.sleep(5)
#     img = driver.find_elements_by_tag_name('img')
#     img = [i.get_attribute('src') for i in img]
#     try:
#         images.append(img[1])
#     except Exception as e:
#         continue




path = 'data/'
counter = 0
for image in images:
    save_as = os.path.join(path, f'image_{counter}.jpg')
    wget.download(image, save_as)
    counter += 1
