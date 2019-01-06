# 14aa34acd95b008af7a01796a544593b
import requests
# 보통 웹 API의 결과는 JSON 형식이나 XML 형식으로 리턴을 한다. 여기서(openweathermap) 는 JSON 형식으로 리턴
# 따라서, JSON 형식의 데이터를 파이썬 데이터형식으로 변환해줘야 하는데.. 이때 json 모듈이 필요함.
import json

# API 키를 지정한다.
apiKey = "14aa34acd95b008af7a01796a544593b"

city_list = ["Seoul,KR", "Tokyo, JP", "New York, US"]

# API 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 켈빈 온도를 섭씨온도로 변환하는 함수
k2c = lambda k : k - 273.15

# 각 도시의 정보를 추출하기
for name in city_list:
    # API의 URL 구성하기
    url = api.format(city=name, key=apiKey)
    # API 요청을 보내서 날씨 정보를 가져오기
    res = requests.get(url)
    print(res)
    # JSON 형식의 데이터를 파이썬 형으로 변환한다.
    data = res.json()
    print(json.dumps(data))
    print("** 도시 = ", data["name"])
    print(" | 날씨 = ", data["weather"][0]["description"])
    print(" | 최저 기온 = ", k2c(data["main"]["temp_min"]))
    print(" | 최고 기온 = ", k2c(data["main"]["temp_max"]))
    print(" | 습도 = ", data["main"]["humidity"])
    print(" | 기압 = ", data["main"]["pressure"])
    print(" | 풍향 = ", data["wind"]["deg"])
    print(" | 풍속 = ", data["wind"]["speed"])
    print(" ")
