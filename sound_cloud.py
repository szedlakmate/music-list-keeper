from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://soundcloud.com/szedl-k-m-t/sets/soft-mixes")
driver.implicitly_wait(5)
titles = driver.find_elements_by_xpath('//*[@id="content"]/div/div[3]/div[1]/div/div[2]/div[2]/div/div[3]/div/ul/li/div')

print('hey')
print(titles)

for title in titles:
    print(title.text)

driver.close()