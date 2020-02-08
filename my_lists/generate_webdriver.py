from selenium import webdriver


def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    return driver