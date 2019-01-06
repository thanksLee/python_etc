from selenium import webdriver

# naver에 로그인 하기
userid = ""
userpwd = ""

driver = webdriver.PhantomJS("F:/Utility/python/web_crawling/phantomjs-2.1.1-windows/bin/phantomjs")
driver.implicitly_wait(3)

url_login = "https://nid.naver.com/nidlogin.login?mode=form"

driver.get(url_login)
print("로그인 페이지에 접속하였습니다.")

# 아이디를 입력하는 input요소를 찾아오기
inputID = driver.find_element_by_id("id")

# 입력박스에 있는 텍스트를 모두 지워준다.
inputID.clear()

# 입력박스에 아이디 입력하기
inputID.send_keys(userid)

# 비밀번호를 입력하는 input요소를 찾아오기
inputPW = driver.find_element_by_id("pw")
inputPW.clear()

# 비밀번호 입력박스에 비밀번호를 입력하기
inputPW.send_keys(userpwd)

# 로그인 버튼을 찾아서 전송하기
loginBtn = driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input')

# 아이디와 비밀번호를 전송한다.
loginBtn.click()
print("로그인에 성공하였습니다.")

driver.save_screenshot("naver3.png")

driver.quit()