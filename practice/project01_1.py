from selenium import webdriver
from bs4 import BeautifulSoup

from konlpy.tag import Hannanum
from collections import Counter
import pytagcloud # Add fonts supporting Korean

driver_path = '../resources/chromedriver'  # driver path
url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06'

reviews = []

browser = webdriver.Chrome(executable_path=driver_path)  # Chrome driver
browser.get(url)
soup = BeautifulSoup(browser.page_source, "html.parser")

for list_best in soup.find_all('div', {'class': 'goodsImgW'})[0:1]:
    print(list_best)
    browser.get("http://www.yes24.com" + list_best.a['href'])

    for target_num in range(1,11):
    # find_page = soup_detail.find('div', {'class': 'yesUI_pagenS'})
    # target_num = int(find_page.find('strong').string) + 1
        browser.get("http://www.yes24.com/Product/communityModules/GoodsReviewList/71923011?Sort=1&PageNumber=" + str(target_num) + "&amp;Type=ALL&_=1562899816535")
        soup_detail = BeautifulSoup(browser.page_source, "html.parser")

        for review in soup_detail.find_all('div', {'class': 'reviewInfoBot origin'}):
            reviews.append(review.find('div', {'class': 'review_cont'}).get_text())

print(reviews)
browser.quit()
with open('reviews.txt', 'a', encoding="utf8") as f:
    for item in reviews:
        f.write(item)

f = open("reviews.txt", "r", encoding="UTF-8")
description = f.read()

h = Hannanum()
nouns = h.nouns(description)
count = Counter(nouns)
print(count)

tag = count.most_common(100)
tag_list = pytagcloud.make_tags(tag, maxsize=50)
pytagcloud.create_tag_image(tag_list, 'word_cloud.jpg', size=(900, 600), fontname='Korean', rectangular=False)

import webbrowser
webbrowser.open('word_cloud.jpg')