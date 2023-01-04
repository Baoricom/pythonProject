from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.by import Keys
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('file:///Users/ibraevbaurzhan/Downloads/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH03/03_02/html_code_03_02.html')
select = Select(driver.find_element(By.NAME, str("numReturnSelect")))
select.select_by_index(4)
time.sleep(4)
select.select_by_visible_text('200')
time.sleep(3)
select.select_by_value('250')
time.sleep(3)
options = select.options
submit_button = driver.find_element(By.NAME, str('continue'))
submit_button.submit()
time.sleep(3)
driver.close()