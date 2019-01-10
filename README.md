### 참고
```
- anaconda 사용
- https://www.anaconda.com/download/ 이곳에서 다운로드
```
### anaconda 명령어
```
- anaconda python version 확인
    > c:\anaconda3\script\conda.exe
    > conda.exe search python
- anaconda 가상 환경
    > conda create -n "가상환경경로" python="파이썬버전" anaconda
    > ex) conda create -n F:\myproject\workspace-python\python_etc\machine_runing\py356 python=3.5.6 anaconda
    > activate 는
        F:\myproject\workspace-python\python_etc\machine_runing\py356\Lib\venv\scripts\nt\activate, deactivate
    가 있다.
```
### 자료구조
```
- ex) ex01.py
- 리스트
    > ss = [ '하이assdfas', '헬로', '안녕']
      print(ss[-1]) 뒤에서 부터 가져온다.
- 튜플
    > 리스트보다 속도가 빠르다
    > 리스트와 비슷하지만 튜플내의 원소를 변경할 수 없다.
    > 튜플은 소괄호를 사용한다.
      tt = 1, 2, 3, 4
      print(tt)
- dictionary
  > {키:값} 으로 이루어져 있다.
```
### 웹스크래핑
```
- ex) ex02.py
- 웹상의 정보를 추출하기 우한 라이브러리 블러오기
- urllib 라이브러리 : Http나 FTP를 사용해서 데이터를 다운로드할때 사용하는 라이브러리
- urllib : URL을 다루는 모듈을 모아 놓은 패키지
- urllib 패키지에 있는 모듈중에서 request모듈을 이용하는데 request 모듈안에 urlretrieve() 함수를 사용한다.
    > urlretrieve() 함수는 파일로 바로 저장.
- urlopen()
    > 파일로 바로 저장하지 않고 메모리에 로딩을 한다.
```
### 기상청 데이터 가져오기
```
- ex) ex03.py, ex04.py
- http://www.kma.go.kr/index.jsp
  http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp
- 참고
    import urllib.request as req # urllib.request를 req로 사용하겠다. (alias)
```
### Beautifulsoup
```
- ex) ex05.py, ex06.py, ex07.py, ex08.py, ex09.py, ex10.py, ex11.py
- Beautifulsoup은 다운로드 기능은 없다.
- pypi(Python Package Index) : Python Package 관리 시스템
- beautifulsoup 설치
  pip install beautifulsoup4
- sibling : 형제관계
    형제 관계의 다음 형제 찾기 (next_sibling)
- 요소 찾기
    > find(), find_all()
    > 태그의 요소를 가져오려면 attrs 를 이용하면 된다. 그러면 결과가 dict 형태로 출력
- prettify():
    > 요소에 New line 처리를 한다.
- css 선택자를 활용하여 element 요소 접근
    > select(선택자) : CSS 선택자로 요소 여러개를 리스트로 추출한다.
    > select_one(선택자) : CSS 선택자로 요소 하나를 추출한다.
    > html element의 요소가 id = # 으로, class = . 으로 한다.
- urljoin 함수는 상대경로를 절대경로로 변환하는 함수
    > urljoin 두번째 매개 변수에 상대경로가 아닌 절대경로를 지정하는 경우("http://~")
```
### Http 통신 및 쿠키, 세션
```
- ex) ex12.py
- HTTP 통신의 특성
    > Connectionless : 클라이언트가 request를 서버에 보내면, 서버는 클라이언트에게 response를 보낸다. 그리고 접속을 끊는 특성
    > Stateless : 접속을 끊는 순간 클라이언트와 서버의 통신은 끝나고 상태정보는 유지하지 않는 특성
- 쿠키 (Cookie)
    > 쿠키는 클라이언트에 저장되는 키와 값이 들어있는 작은 데이터 파일이다.
    > 쿠키는 이름, 값, 만료날짜(쿠키 저장기간), 경로정보가 들어 있다.
    > 쿠키는 일정 시간동안 데이터를 저장할 수 있어서 로그인 상태를 유지한다.
    > 쿠키는 클라이언트의 상태 정보를 유저의 하드디스크에 저장하였다가 필요할때 참조, 재사용한다.
    > 쿠키의 사용 예
        * 방문사이트에서 "아이디와 비밀번호를 저장하시겠습니까?" 라고 메시지가 나오면 쿠키로 저장하겠냐라는 의미이다.
        * 파업창이 뜰때, "오늘 하루 보지않음" 을 체크하면 오늘은 창이 뜨지 않는다.
- 세션(Session)
    > 세션은 클라이어느와 웹서버간 네트워크 연결이 지속 유지되고 있는 상태를 말한다.
      즉, 사용자가 브라우저를 열어 서버에 접속한 뒤 접속을 종료할때까지를 말한다.
    > HTTP프로토콜은 비접속형 프로토콜이기에, 매 접속시마다 새로운 네트워크 연결이 이루어지는데, 세션이 연결유지를 가능하게 해준다.
    > 클라이언트가 Request를 보내면, 해당 서버의 엔진이 클라이언트에게 유일한 ID를 부여하는데, 이 ID를 세션이라고 한다.
    > 세션 ID는 임시로 저장하여 페이지 이동시 이용하거나, 클라이언트가 재 접속했을때 클라이언트를 유일하게 구분하는 수단이 된다.
    > 세션 원리
        * 세션 ID를 서버에서 클라이언트가 웹사이트에 접속시 발급해 준다.
        * 서버에서 클라이언트로 발급해준 세션 ID를 쿠키(쿠키 이름은 JSESSIONID)를 사용해서 저장한다.
        * 클라이언트는 재 접속시, 이 쿠키(JSESSIONID)를 이용해서 세션 ID 값을 서버에 전달한다.
    > 세션의 장점
        * 각 클라이언트에게 고유 ID를 부여한다.
        * 세션 ID로 클라이언트를 구분해서 클라이언트의 욕에 맞는 서비스를 제공할 수 있다.
        * 사용했던 정보들을 서버에 저장하기 때문에 보안 상 쿠키보다 우수하다.
    > 세션의 단점
        * 서버에 저장되는 세션 때문에 서버에 처리를 요구하는 부하와 저장공간을 필요로 한다.
- 쿠키와 세션의 차이점
    > 큰 차이점은 저장위치
        * 쿠키는 클라이언트에 저장되어서 보내는 역할을 하고,
          세션은 서버에 저장되어서 클라이언트에게 알려줘서 사용한다.
```
### Requests 모듈의 메서드
```
- ex) ex13.py
- http에서 사용하는 데이터 전송방식 GET, POST 방식이 있는데, 두 방식의 메소드를 제공
    > r = request.get("hhtp://google.com") # get 방식의 요청을 하는 경우
    > POST 요청
        formData = {"key1":"value1", "key2":"value2"}
        r = requests.post("http://sample.com", data=formdata)
- 세션을 사용하는 경우
    > session = requests.session() # 세션 시작하기

    # 로그인 하기
    login_info = {
        "id":userid,
        "passwd":userPw
    }

    url = "http://www.test.com/loginConfirm.php" # id와 pw를 확인하는 로직 : 서버단 스크립트

    result = session.post(url, data=login_info)
    result.raise_for_status() # 오류체크 : 오류가 발생하면 예외처리를 한다.

    # 로그인 후 get 방식의 서비스를 요청할 경우에는
    myUrl = "http://www.test.com/myPage.html"
    res = session.get(myUrl)
    res.raise_for_status()

    import requests
    from bs4 import BeautifulSoup

    soup = BeautifulSoup.(res.txt, "html.parser")
```
### selenium 소개
```
- ex) ex14.py, ex15.py, ex16.py
- 웹브라우저를 컨트롤하여 웹 자동화하는 도구 중의 하나이다.
- 자동화
    > 자동화의 종류
        * 가장 원초적인 자동화는 화면의 좌표를 기준으로 한 자동화
        * Selenium 도구를 이용하는 웹 자동화 (팬텀 JS)
        * 윈도우즈의 자동화
        * 작업의 자동화
- Selenium은 Selenium Server 와 Selenium Client가 있다.
- 로컬 컴퓨터의 웹브라우저를 컨트롤하기 위해서 Selenium Client를 사용한다.
- Selenium Client는 WebDriver라는 공통 인터페이스와 각 브라우저 타입별로 웹 드라이버로 구성되어 있다.
- 웹드라이버의 구성은
    > WebDriver.Firefox (가장 궁합이 잘 맞는다.)
    > WebDriver.Chrome : 크롬
    > WebDriver.Ie : Explorer
    > WebDriver.Opera
    > WebDriver.PhantomJS : 명령줄 Interface (CLI : Command Line Interface)
- Selenium 설치
    pip install selenium
- Selenium Driver 설치
    Firefox     : https://github.com/mozilla/geckodriver/releases
    Chrome      : https://sites.google.com/a/chromium.org/chromedriver/downloads
    Edge        : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    PhantomJS   : http://phantomjs.org/download.html
- Selenium 사용법
    from selenium import webdriver : 사용할 webdriver를 import 한다.
    > chrome을 사용하는 경우
      browser = webdriver.Chrome('크롬드라이버가 있는 경로')
    > firefox를 사용하는 경우
      browser = webdriver.Firefox('Firefox 드라이버가 있는 경로')
    > PhantomJS의 경우
      browser = webdriver.PhantomJS('PhantomJS 설치 위치 경로')
- 특정 URL을 이용하여 브라우저를 싱행시키는 방법
    > browser.get('https://www.google.com)
- Selenium 으로 DOM 요소를 선택하는 방법
    > DOM 내부에 있는 여러개의 요소들 중에서 처음 찾아지는 요소를 추출하는 메소드
        find_element_by_id(id)                    id 속성으로 요소를 하나 추출한다.
        find_element_by_name(anem)                name 속송으로 요소를 하나 추출한다.
        find_element_by_css_selector(query)       CSS 선택자로 요소를 하나 추출한다.
        find_element_by_xpath(query)              XPath를 지정해 요소를 하나 추출한다.
        find_element_by_tag_name(name)            태그 이름이 name에 해당하는 요소를 하나 추출한다.
        find_element_by_link_text(text)           링크 텍스트로 요소를 하나 추출한다.
        find_element_by_partial_link_text(text)   링크의 자식요소에 포함돼 있는 텍스트로 요소를 하나 추출한다.
        find_element_by_class_name(name)          클래스 이름이 name에 해당하는 요소를 하나 추출한다.
    > DOM 내부에 있는 여러개의 요소들을 모두 추출하는 메소드
        find_elements_by_css_selector(query)       CSS 선택자로 요소를 하나 추출한다.
        find_elements_by_xpath(query)              XPath를 지정해 요소를 하나 추출한다.
        find_elements_by_tag_name(name)            태그 이름이 name에 해당하는 요소를 하나 추출한다.
        find_elements_by_class_name(name)          클래스 이름이 name에 해당하는 요소를 하나 추출한다.
        find_elements_by_partial_link_text(text)   링크의 자식요소에 포함돼 있는 텍스트로 요소를 하나 추출한다.
    위 메소드를 이용해서 어떠한 요소도 찾지 못하는 경우에 발생하는 예외는
        - NoSuchElementException
- DOM 요소에 적용할 수 있는 메소드/속성
    > 메소드
        clear()              : 글자를 입력할 수 잇는 요소의 글자를 지운다.
        click()              : 요소를 클릭한다.
        get_attribute(name)  : 요소의 속성중에 name에 해당되는 속성의 값을 추출한다.
        is_displayed()       : 요소가 화면에 출력되는지 확인한다.
        is_enabled()         : 요소가 활성화 되었는지 확인한다.
        is_selected()        : 체크박스등의 요소가 선택 상태인지 확인한다.
        screenshot(filename) : 화면을 캡처해서 filename으로 저장한다.
        send_keys(value)     : 키를 입력한다. 일반적으로 text데이터를 보낸다.
            * value가 텍스트 데이터가 아닌 경우(특수키 : 방향키, 펑션키 : F1, F2, F3...F12), Enter, Tab, Control..
            즉, 특수키를 사용해야 하는 경우에는 별도의 모듈을 사용해야한다.
            from selenium.Webdriver.common.keys import Keys
            ARROW_DOWN / ARROW_LEFT / ARROW_RIGHT / ARROW_UP
            BACKSPACE / DELETE / HOME / END / INSERT
            ALT / COMMAND / CONTROL / SHIFT
            ENTER / ESCAPE / SPACE / TAB
            F1 / F2 / F3 .... F12
        submit()                    : 입력 양식을 전송한다.
        value_of_css_property(name) : name에 해당하는 CSS 속성 값을 추출한다.
    > 속성
        id                   : 요소의 id 속성
        location             : 요소의 위치
        parent               : 부모요소
        rect                 : 크기와 위치정보를 가진 딕셔너리 자료형을 리턴한다.
        screenshot_as_base64 : 스크린샷을 base64 형태로 추출한다.
        screenshot_as_png    : 스크린샷을 PNG 형식의 바이너리로 추출한다.
        size                 : 요소의 크기
        tag_name             : 태그이름
        text                 : 요소내부의 글자
- PhantomJS 용 메서드와 속성
    > add_cookie(cookie_dict) : 쿠키값을 딕셔너리 형식으로 지정
        * WebDriver.add_cookie({"name":"kim", "value":"test"})
          WebDriver.add_cookie({"name":"kim", "value":"test", "path":"/"})
          WebDriver.add_cookie({"name":"kim", "value":"test", "path":"/", "secure":"True"})
    > back() / forward()                : 이전 페이지 또는 다음 페이지로 이동
    > close()                           : 브라우저를 닫다
    > current_url                       : 현재 url을 추출한다.
    > delete_all_cookies()              : 모든 쿠키를 제거한다.
    > delete_cookie(name)               : 특정 쿠키를 제거한다.
    > get_cookie(name)                  : 특정 쿠키값을 읽는다.
    > get_cookies()                     : 모든 쿠키값을 추출한다.
    > execute(command, params)          : 브라우저의 고유 명령어를 실행
    > get(url)                          : 웹페이지를 읽어 들인다.
    > get_screenshot_as_file(filename)  : 스크린샷을 파일로 저장
    > get_screenshot_as_png             : PNG 형식으로 스크린샷의 바이너리 추출
    > save_screenshot(filename)         : 스크린샷을 저장
    > implicitly_wait(sec)              : 최대 대기시간을 초 단위로 지정해서 처리가 끝날때까지 대기
    > quit()                            : 브라우저 및 드아라이버를 종료시켜서 브라우저를 닫는다.
    > title                             : 현재 페이지의 타이틀을 추출
```
### WEB API(Application Programing Interface)
```
- ex) e17.py
- 어떤 사이트가 가지고 있는 기능을 외부에서 쉽게 사용할 수 있게 공개한 것
- 원래 API는 어떤 프로그램 기능을 외부의 프로그램에서 호출해서 사용할 수 있게 만든것을 의미한다.
  간단히 말하자면 서로 다른 프로그램이 기능을 공유 할 수 있게 절차나 규약을 정의한것.
- WEB API를 제공하는 이유
    > 대부분의 웹서비스는 정보를 웹사이트를 통해서 제공한다. 이러한 정보는 크롤링 대상이 된다.
    > 수많은 개발자들이 크롤링한다고 하면 서버에 부하가 많이 발생한다.
      따라서 , 크롤링이 될 것이라면 차라리 미리 웹 API를 제공해서 서버의 부담을 줄이는 것이 낫다. 결론적으로 WEB API를 제공하는
      첫번째 이유는 서버의 부하를 감소시키는 것.
    > 두번째 이유는 상품을 알리거나, 판매할 기회를 더 많이 늘리기 위해서다.
- WEB API는 유료와 무료로 나뉜다.
- WEB API를 사용시 유의 사항
    > 첫번째 WEB API 제공자의 문제로 인해서 API가 없어지는 경우와 사양의 변화 발생할 수 있다.
    > 웹 API를 신뢰할 수 있는지 확인한다. 즉, 지원을 오래할수 있는지, 수요가 많은지,
      큰기업에서 제공하는지 등등
```
### WEB의 다양한 데이터 형식
```
- ex)
- XML / JSON / YAML / CSV / TSV / EXCEL / PDF 등등
- 기본적인 데이터 포멧
    > 텍스트 데이터와 바이너리 데이터로 분류할 수 있다.
    > 텍스트 데이터는 일반적인 텍스트 에디터로 편집할 수 있는 데이터 포멧을 의미한다.
      자연언어 (한국어, 영어, 일어..)와 숫자로 구성된 데이터
      특수문자 (줄바꿈, 탭 등 제어문자도 포함)
    예) 프로그래밍 소스코드, XML / JSON / YAML / CSV..
- 바이너리 데이터 : 텍스트 데이터 외의 데이터를 의미한다.
                   텍스트 데이터는 문자 데이터로 사용할 수 있는 데이터인 반면에
                   바이너리 데이터는 문자와 상관없이 ㄷ이터를 사용할 수 있는 형식의 데어터
    > filename = "a.bin" # bin : binary
      value = 100
    # 파일 쓰기모드로 열어서 만들기

    with open(filename, "wb") as f : # wb : write binary약자
        f.write(bytearray([value]))
- 장단점
    > 텍스트 데이터     : 텍스트 에디터만 있으면 편집할 수 있다.                바이너리 데이터에 비해 크리가 크다
                         또한 설명을 포함 할 수있으므로 가독성이 높다.
    > 바이너리 데이터   : 텍스트 데이터에 비해 킈가 작다                        텍스트 에디터로 편집할 수 없다.
                                                                            어떤 바이트에 어떤 데이터가 있는지 정의를 해야한다.
    실제로 웹상에서는 텍스트보다 바이너리 데이터가 대부분 많이 사용된다.
    이유는 이미지나 동영상 파일 때문이다.(이미지나 동영상 파일은 요량이 크다, 따라서 서버의 부담이 많다.)
    이미지는 압축률이 다른 형식을 많이 사용한다. jpeg, gif, png

    이러한 이미지 파일은 바이너리 형식을 취하고 있다.
    텍스트 데이터 기반의 이미지 형식도 있지만, 실제로는 거의 사용되지 않는다.
    바이너리 형식으로 사용하는 것이 훨씬 실용적이기 때문에
- 텍스트 데이터의 주의점
    > 어떤 코문자 코드(문자 인코딩)로 저장돼 있느냐에 따라서 다른 의미를 갖게 된다.
      같은 문장을 텍스트 파일로 저장할때 문자 인코딩이 다르면 다른 문자로 나타난다.
      최근에는 UTF-8을 많이 사용한다. (기존에는 EUC-KR)
      HTML 문서에서 <meta charset = "utf-8">
```
### XML 데이터
```
- ex) ex18.py
- 텍스트 데이터를 기반으로한 형식, 웹 API에서 많이 사용되는 형식중의 하나
- XML (Extensible Markup Language) : 특정 목적에 따라 데이터를 태그로 감싸 마크업하는 일반적인 형식의 언어이다.
- W3C에 의해 만들어 졌다.
- XML은 데이터를 계층구조(트리구조, HTML의 DOM 구조)로 표현할 수 있다는 특징이 있다.
- 기본형식
    <요소 속성="속성값">내용</요소>
  내가 원하는 요소이름을 아무거나 사용할 수 있다.
  하나의 요소에는 여러개의 속성을 추가해도 상관없다.
  <products type="a>
    <product id = "a001" price="1000">a1상품</product>
    <product id = "a002" price="2000">a2상품</product>
  </products>
  위와 같이 XML은 계층구조로 만들어서 복잡한 데이터를 표현할 수 있다.
```
### JSON 데이터
```
- ex) ex19.py
- 텍스트 데이터를 기반으로 한 데이터 형식
- JSON(JavaScript Object Notation) : 자바스크립트에서 사용하는 객체 표기 방법
- 자바스크립트 전용 데이터 형식이 아니라, 다양한 소프트웨어와 프로그래밍언어에서 많이 사용되는 형식으로 데이터 교환할때 xml보다 가볍기 때문에 최근 선호하는 형식이다.
- JSON의 확장자는 ".json" 으로 사용한다.
- 구조가 단순하다는 것이 큰 장점이다.
- 수많은 프로그래밍언어에서 인코딩/디코딩 표준으로 JSON 을 제공하고 있다.
- 파이썬 모듈에도 json 모듈을 지원하고 있다.
- 최근 WEB API 들이 JSON형식으로 데이터를 제공하고 있다.
- JSON의 구조
    > 자료형 : 숫자, 문자, 불린값(True, False), 배열, 객체, null 이라는 6가지 종류를 사용할 수 있다.
      ex) 숫자 : 40
          문자 : "stirng"
          boolean : true/false
          array:[1, 2, 3]
          object : {"key" : "value, "key":value...}
          null:null
    > json.dumps 메소드는 json 형식으로 출력한다.
```
### YAML 데이터 분석
```
- ex) py20.py
- YAML은 들여쓰기를 사용해 계층 구조를 표현하는 것이 특징인 데이터 형식
- XML보다 간단하며, JSON과 거의 비슷하다.
- YAML은 JSON 대용으로 많이 사용되기도 하고, 애플리케이션 설정 파일을 작성할때 많이 사용한다.
- 웹 프레임워크인 Ruby나 Symfony(PHP)의 설정 파일 형식으로 사용되고 있다.
- 파이썬 / PHP 루비 등을 포함한 여러 프로그래밍 언어에서 YAML 형식을 다루기 위한 라이브러리가 제공되고 있다.
- 파이썬에서 YAML을 다루기 위해서 PyYAML이라는 모듈을 설치해야 한다.
    설치 예) pip3 install pyyaml
- YAML 데이터 형식
    > YAML의 기본은 배열, 해시, 스칼라(문자열, 숫자, 불리언)입니다.
    > 배열을 나타낼때는 하이픈(-)을 붙여서 사용한다.
      하이픈 뒤에는 공백을 사용해야 한다.
      ex) - apple
          - orange
          - banana
    > 중첩 배열 (배열안에 배열)
      - Yellow
      -
        - orange
        - banana
      - Red
      -
        - apple
        - strawberry
    > Hash 표현 방법
      - 해시는 자바스크립트의 객체와 같은 것을 의미("키" : "값")
      ex) name : hong
          age : 24
          color : white
    > Hash의 계층구조 표현 방법
      ex) name : kim
          property:
             age:10
             color:brown
    > 배열과 hash를 조합하면 조금 더 복잡한 데이터를 표현할 수 있다.
      ex) - name : lee
            color : brown
            age : 10
            favorites:
              - sports
              - movie
          - name : smith
            color:white
            age : 15
            favorites:
              - music
              - baseball
          - name : kim
            color : blue
            age : 20
            favorites:
              - gaming
              - drawing
    > YAML은 flow style이 지원된다.
      - flow style은 한줄로 표현할 수 있는 방법을 말한다.
        {key : value1, key2 : value2, ...}
        이때 쉼표(,)와 콜론(:) 뒤에는 반드시 공백이 있어야 한다.
      ex) - name : lee
            favorites:["sports", "movies"]
          - name : smith
            favorites:["music", "reading"]
    > YAML은 주석을 사용할 수 있다. 주석 기호는 "#" 으로 시작한다.
      # 노란색 과일
      ex) - banana
          - orange
    > Multiline으로 문자열을 지정할 수 있다.
      multi-line: |
        I am a boy.
        I am a student.
        I like orange.
- YAML의 앵커와 별칭(alias)
    > &aaa1 : 일종의 변수 선언 <--- 앵커라고 한다.
      *aaa1 : 별칭
```
### CSV(Comma Separate Valuess)
```
- ex) ex21.py, ex22.py
- 웹에서 가장 많이 사용되는 형식
- 엑셀로 쉽게 만들수 있는 형식
- 수많은 데이터베이스와 데이터 도구에서 CSV 형식을 지원
- 파일은 텍스트 에디터를 이용해서 간편하게 수정할 수 있다.
- CSV와 비슷한 형식의 파일들로
    > TSV(Tab Separated Values) : 콤마가 아닌 탭으로 필드를 구분하는 형식
    > SSV(Space Separated Vaues) : 공백으로 필드를 구분하는 형식
    > CSV 파일 형식
- 파이썬의  csv 모듈을 이용한 CSV데이터 처리 방법
    > CSV 파일에 있는 필드 데이터가 큰 따옴표(")로 둘러싸인경우에는 CSV파일을
      분석하기 어렵다.
      따라서 이때에는 CSV모듈을 이용하는데.
      csv.reader(파일포인터, delimiter=",", quotechar='"')
      여기서, delimiter는 구분문자를 지정하고, quotechar는 어떤 기호로 데이터를 감싸고 있는지를 지정한다.
    > csv.writer(파일포인터, delimiter=",", quotechar='"')
```
### EXCEL
```
- ex) ex23.py
- 파이썬에서 엑설 파일을 분석하기 위해서는 파이썬 엑셀 라이브러리를 설치해야 한다.
- pip install openpyxl
- openpyxl 은 파이썬에서 엑셀 파일을 읽고 쓸수 있는 라이브러리이다.
- 엑셀파일 구조
    > 보통 엑셀 파일을 book이라고 부른다.
      book 내부에는 여러개의 sheet가 존재한다.
      각 시트는 행(row)과 열(column)을 가진 2차원의 셀(cell)로 구성되어 있다.
```