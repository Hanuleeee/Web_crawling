from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver'
url ='https://play.google.com/store/apps/top/category/GAME'

browser = webdriver.Chrome(executable_path=driver_path)
browser.get(url)
page = browser.page_source
browser.quit()

soup = BeautifulSoup(page, 'html.parser')

for link in soup.find_all('a'):
    if link.string == "더보기":
        print(link)
        print(link.get('href'))


# for link in soup.find_all('a'): #??? 왜안될까..
#     print(link)
#     print('==--============')
#     if "id-track-click" in link['class']:   # class가 없는 a태그가 있으서 에러남..
#         print(link['href'])


