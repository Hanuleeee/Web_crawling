from selenium import webdriver
from bs4 import BeautifulSoup

driver_path = '../resources/chromedriver'  # driver path
url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06'

reviews = []

browser = webdriver.Chrome(executable_path=driver_path)  # Chrome driver
browser.get(url)
soup = BeautifulSoup(browser.page_source, "html.parser")
links= soup.find('ul',{'class':'Tab'})

for link_best in links.find_all('a')[1:2]:
    print(link_best)
    browser.get("http://www.yes24.com" + link_best['href'])
    soup_best = BeautifulSoup(browser.page_source, "html.parser")

    for list_best in soup_best.find_all('div',{'class':'goodsImgW'})[0:2]:
        browser.get("http://www.yes24.com" + list_best.a['href'])
        soup_detail = BeautifulSoup(browser.page_source, "html.parser")

        for review in soup_detail.find_all('div', {'class':'reviewInfoBot origin'}):
            print(review)
            reviews.append(review.find('div',{'class':'review_cont'}).get_text())

print(reviews)
browser.quit()
with open('reviews.txt', 'a', encoding="utf8") as f:
    for item in reviews:
        f.write(item)