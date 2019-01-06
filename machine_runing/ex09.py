from bs4 import BeautifulSoup
from urllib import request

# 웹문서 가져오기
url = "https://finance.naver.com/marketindex/"

res = request.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.head_info > span.value")
print("usd/krw : ", price.string)

print()
print("=================================================")
print()

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = request.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
lst = soup.select("#mw-content-text > div > ul > li > ul > li > a")

print(lst)

print("--------------------------")
print()

for i in lst:
    print(i.string)