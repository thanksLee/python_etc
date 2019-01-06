from urllib import request, parse #URL encoding을 하기 위해 불러오는 모듈

rssUrl = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개 변수 지역별 코드를 지정하는 변수
# stnId 코드 : 108(전국), 109(서울, 경기), 105(강원도), 131(충청북도)
#              133(충청남도), 146(전라북도), 156(전라남도), 143(경상북도)
#              159(경상남도), 184(제주도)

values = {
    "stnId":"108"
}

params = parse.urlencode(values)

url = rssUrl + '?' + params
print(url)

data = request.urlopen(url).read()
text = data.decode("utf-8")

print(text)

