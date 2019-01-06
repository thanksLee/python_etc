# 텍스트 데이터 가져오기

import requests

resData = requests.get("http://api.aoikujira.com/time/get.php")

txt = resData.text

print(txt)

# binary 형태로
cont = resData.content
print(cont)

# 이미지 데이터 가져오기
res = requests.get("https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png")

aa = res.content

with open("log.png", "wb") as fp:
    fp.write(aa)

print("이미지파일이 저장되었습니다.")
