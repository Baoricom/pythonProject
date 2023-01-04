from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

sys.path.append('../DICOM4')
drier = webdriver.Chrome()
from DICOM4 import login
from DICOM4 import logout


if __name__ == '__main__':
    login


driver.find_element(By.XPATH, str('//@id=body[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]')).click()

driver.close()