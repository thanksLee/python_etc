from urllib import request, parse #URL encoding을 하기 위해 불러오는 모듈
import sys

# 명령줄 인수가 제대로 입력되었는지 확인
if len(sys.argv) <= 0: # 명령줄 인수가 1이하이면 오류 메시지를 출력
    print("사용 법 : python 인수1 인수2")
    sys.exit()

regionCode = sys.argv[1]

rssUrl = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    "stnId":regionCode
}

params = parse.urlencode(values)

url = rssUrl + '?' + params

print("url = " + url)

data = request.urlopen(url).read()
text = data.decode("utf-8")

print(text)