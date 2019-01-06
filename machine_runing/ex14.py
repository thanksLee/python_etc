from selenium import webdriver

url = "http://www.naver.com/"

# PhantomJS 드라이버 추출
driver = webdriver.PhantomJS("F:/Utility/python/web_crawling/phantomjs-2.1.1-windows/bin/phantomjs")

driver.implicitly_wait(3) # 드라이버를 초기화될 때가지 3초간 대기

driver.get(url)

driver.save_screenshot("naver1.png")

driver.quit()

