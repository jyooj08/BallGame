from selenium import webdriver
import time
import requests 
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
url = browser.get(url)

#scroll
#browser.execute_script("window.scrollTo(0,1080)")

browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2 
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

print("스크롤 완료")

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
        #print(title, original_price)
    else:
        #print(title, "할인되지 않은 영화 제외")
        continue

    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    
    print(f"제목: {title}")
    print(f"할인 전 금액: {original_price}")
    print(f"할인 후 금액: {price}")
    print("링크: ", "https://play.google.com"+link)
    print("-"*100)


time.sleep(5)
browser.quit()