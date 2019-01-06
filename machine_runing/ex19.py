import json

# json 데이터
price = {
    "time":"17-01-02",
    "price":{
        "apple":1000,
        "banana":3000,
        "orange":2000
    }
}

# json.dumps 메소드는 json 형식으로 출력한다.
jsonData = json.dumps(price)

print(jsonData)

# 파이썬으로 json 분석하기
from urllib import request
import os.path
import json

# JSON data download
url = "https://api.github.com/repositories"
filename = "rep.json"

if not os.path.exists(url):
    request.urlretrieve(url, filename)

jsonData = ""
with open(filename, "rt", encoding="UTF-8") as fp:
    jsonData = fp.read()

data = json.loads(jsonData)

for dat in data:
    print(dat["name"] + " - " + dat["owner"]["login"])
