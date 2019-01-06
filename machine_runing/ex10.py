from bs4 import BeautifulSoup
from urllib import request

#fp = open("book.html", encoding="utf-8")
with open("book.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

print(soup.select_one("#DataScience").string)
print(soup.select_one("li#DataScience").string)
print(soup.select_one("ul > li#DataScience").string)
print(soup.select_one("#itBook > li#DataScience").string)
print(soup.select_one("#itBook li#DataScience").string)
print(soup.select_one("ul#itBook > li#DataScience").string)
print(soup.select_one("li[id='DataScience']").string)
print(soup.select_one("li:nth-of-type(3)").string)
print(soup.select("li")[2].string)
print(soup.find_all("li")[2].string)

print()
print("==============================================")
print()
print()


with open("test.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# 파프리카 추출

print(soup.select_one("li:nth-of-type(6)").string)
print(soup.select_one("#vegetable > li.red").string)
print(soup.select_one("#vegetable > li:nth-of-type(2)").string)
print(soup.select("#vegetable > li.green"))
print(soup.select("#vegetable > li.green")[1].string)

print(soup.select_one("li:nth-of-type(4)").string)
print(soup.select_one("#fruits > li.yellow").string)
print(soup.select("#fruits > li.yellow")[1].string)

print(soup.select_one("li.green").string)
print(soup.select("li.green")[2].string)

# find 메서드를 이용해서 추출하기
condition = {"data-lo":"us", "class":"red"}
print(soup.find("li", condition).string)
print(soup.find(id="vegetable").find("li", condition).string)
