from bs4 import BeautifulSoup

html = """

<html>
<body>
    <h1> 스크래핑 연습</h1>
    <p> 웹페이지를 분석해 보기</p>
    <p> 데이터 정제하기..</p>
</body>
</html>
"""

# html 분석하기
# class에서 주어진 Instance
soup = BeautifulSoup(html, "html.parser")

# 원하는 요소 접근하기
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# 원하는 요소의 내용을 추출하기
print("h1=", h1.string)
print("p1=", p1.string)
print("p2=", p2.string)