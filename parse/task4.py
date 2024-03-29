# Task4: parse top game charts
from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver' # driver path
url = 'https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
browser.get(url)
page = browser.page_source  #아, 그 browser의 페이지소스를 가져와라..
browser.quit()

soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())

