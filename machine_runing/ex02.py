from urllib import request

url = "https://ssl.pstatic.net/sstatic/search/nlogo/20181221141832.png"
imgNm = "f:\\naver.png"


request.urlretrieve(url, imgNm) #urlretrieve(URL, 저장할 파일 경로)
print("다운로드 완료되었습니다.")


mem = request.urlopen(url).read()

#파일을 저장하는 과정
#f = open("a.txt", "w")
#f.write("테스트로 파일에 내용을 적습니다.")
#f.close()

# 위의 내용을 with 구문으로 변경
#with open("a.txt", "w") as f:
#    f.wite("테스트로 파일에 내용을 적습니다.")

imgNm = "f:\\naver2.png"
with open(imgNm, mode="wb") as f : # w는 쓰기모드, b는 binary 모드(이미지)
    f.write(mem)
print("다운로드 완료되었습니다.")
