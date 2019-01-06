from bs4 import BeautifulSoup
from urllib import request

import os.path

# XML 다운로드
url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnid=108"
filename = "forecast.xml"

if not os.path.exists(filename):
    request.urlretrieve(url, filename)


# 다운로드받은 파일을 분석하기
xml_data = ""
with open(filename, "r", encoding="utf-8") as fp:
    xml_data = fp.read()

soup = BeautifulSoup(xml_data, "html.parser") # html.parser는 모두 소문자롤 변환한다.

# 날씨 별로 지역 분류해보기
# 각 지역 확인하기
info = {}
for location in soup.find_all("location"):
    cityNm = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info):
        info[weather] = []
    info[weather].append(cityNm)

print(info)
# 지역의 날씨를 구분해서 분류하기
for weather in info.keys():
    print("**", weather)
    for name in info[weather]:
        print("--", name)
