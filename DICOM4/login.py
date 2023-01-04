from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

sys.path.append('../DICOM4')

from DICOM4 import variables

#from selenium.webdriver.common.by import Keys
import time

#from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)


driver.get(variables.address)
print('Starting login test')
driver.find_element(By.NAME, str('credential_0')).send_keys(variables.username)
#time.sleep(2)
driver.find_element(By.NAME, str('credential_1')).send_keys(variables.password)
driver.find_element(By.CLASS_NAME, str('button')).click()
print('Success login')
time.sleep(10)

#driver.close()

