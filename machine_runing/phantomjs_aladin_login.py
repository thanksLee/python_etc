from selenium import webdriver

driver = webdriver.PhantomJS("F:/Utility/python/web_crawling/phantomjs-2.1.1-windows/bin/phantomjs")
driver.implicitly_wait(3)

userid = ""
userpwd = ""

url_login = "https://www.aladin.co.kr/login/wlogin.aspx"

driver.get(url_login)
print("로그인 페이지에 접속했습니다.")

inputId = driver.find_element_by_id("Email")
inputId.clear()
inputId.send_keys(userid)

inputPwd = driver.find_element_by_id("Password")
inputPwd.clear()
inputPwd.send_keys(userpwd)

loginBtn = driver.find_element_by_link_text("로그인")

loginBtn.click()

driver.save_screenshot("aladin.png")

driver.quit()