from bs4 import BeautifulSoup

html = """
<html>
<body>
    <h1 id="title"> Beautifulsoup 사용방법</h1>
    <p id="subTitle"> 스크래핑 연습하기</p>
    <p> 원하는 데이터 추출하기</p>
</body>
</html>
"""

# html 분석하기
soup = BeautifulSoup(html, "html.parser")

# find 메서드를 이용한 데이터 추출하기
lv_title = soup.find(id="title")
print("title : ", lv_title.string)

lv_subTitle = soup.find(id="subTitle")
print("subTitle : " , lv_subTitle.string)

# find_all : 요소의 이름이 같은것을 모두 가져온다.
html = """
<html>
<body>
    <ul>
        <li><a href="http://www.naver.com" id="lv_naver">네이버</a></li>
        <li><a href="http://www.daum.net">다음</a></li>
    </ul>
</body>
</html>
"""

# html 분석하기
soup = BeautifulSoup(html, "html.parser")

a1 = soup.html.body.ul.li.a
print("a1 : ", a1.string)

#2 = a1.next_sibling.next_sibling.next_sibling

#print("a2 : ", a2)

# find_all 메소드 사용
links = soup.find_all("a")

print("links : ", links)

for link in links:
    print(link.string)
    print(link.attrs) # 태그의 요소를 가져오기, dict 형태로 출럭
    print(link.attrs["href"])