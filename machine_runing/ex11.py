from bs4 import BeautifulSoup
from urllib.parse import urljoin

baseUrl = "http://www.example.com/html/a.html"

print(urljoin(baseUrl, "./b.html"))
print(urljoin(baseUrl, "sub/c.html"))
print(urljoin(baseUrl, "../index.html"))
print(urljoin(baseUrl, "../image/a.png"))
print(urljoin(baseUrl, "../css/style.css"))

print()
print()
print()

#urljoin 두번째 매개 변수에 상대경로가 아닌 절대경로를 지정하는 경우("http://~")
print(urljoin(baseUrl, "http://www.other.com/aa"))
print(urljoin(baseUrl, "//www.another.com/bb/index.html"))