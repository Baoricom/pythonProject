from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('file:///Users/ibraevbaurzhan/Downloads/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html')
login_form = driver.find_element(By.ID, str('loginForm'))
username = driver.find_element(By.NAME, str('username'))
print('element is:')
print(login_form)
print('username is:')
print(username)
driver.close()