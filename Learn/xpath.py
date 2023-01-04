from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('file:///Users/ibraevbaurzhan/Downloads/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html')
login_form_absolute = driver.find_element(By.XPATH, str('/html/body/form[1]'))
login_form_relative = driver.find_element(By.XPATH, str('//form[1]'))
login_form_id = driver.find_element(By.XPATH, str("//form[@id='loginForm']"))
print('absolute is:')
print(login_form_absolute)
print('relative is:')
print(login_form_relative)
print(login_form_id)


driver.close()