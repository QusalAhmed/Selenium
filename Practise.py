import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/Users/qusal/PycharmProjects/Selenium/SeleniumDriver"
driver = webdriver.Chrome()
driver.get("https://www.daraz.com.bd/")
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'header-content'),  # Element filtration
        'SIGNUP / LOGIN'  # The expected text
    )
)
driver.find_element("id", "anonLogin").click()
