from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import sys

# import logout

sys.path.append('../DICOM4')

from DICOM4 import variables

# from selenium.webdriver.common.by import Keys
import time

# from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
window_before = driver.window_handles[0]
print(window_before)
driver.implicitly_wait(7)
driver.maximize_window()

driver.get(variables.address)

print('Starting login test')
driver.find_element(By.NAME, str('credential_0')).send_keys(variables.username)
# time.sleep(2)
driver.find_element(By.NAME, str('credential_1')).send_keys(variables.password)
driver.find_element(By.CLASS_NAME, str('button')).click()
print('Success login')

driver.find_element(By.XPATH, "//a[@id='DICOM ROUTER']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Storage List']").click()
driver.find_element(By.XPATH, "//td[@id='oDiv0']//input[@value='add']").click()

window_after = driver.window_handles[1]

driver.switch_to.window(window_after)

str2 = driver.title
print(str2)
print(window_after)
driver.find_element(By.XPATH, "//input[@id='storageName']").send_keys("Selenium2")
driver.find_element(By.XPATH, "//input[@value='Save']").click()
time.sleep(5)

print("success storage added")
driver.switch_to.window(window_before)
try:
    element = driver.find_element(By.XPATH, "//td[normalize-space()='Selenium2']")
except NoSuchElementException:
    print("Element not found")
else:
    print("Element found")

# exit()


driver.close()
