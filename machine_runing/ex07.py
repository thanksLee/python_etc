from bs4 import BeautifulSoup
from urllib import request

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

# urlopen method으로 데이터 가져오기

res = request.urlopen(url)

print(res)

# 웹데이터 분석하기
soup = BeautifulSoup(res, "html.parser")
    AJU
wf = soup.find("wf")
print(wf.string)

title = soup.find("title")
print(title.string)