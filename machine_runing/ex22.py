import csv, codecs

# 쓰기
with codecs.open("test.csv", "w", encoding="utf-8") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["상품 코드", "상품이름", "가격"])
    writer.writerow(["1", "키보드", 20000])
    writer.writerow(["2", "마우스", 10000])
    writer.writerow(["3", "모니터", 100000])


# 읽기
fileNm = "test.csv"
fp = codecs.open(fileNm, "r", encoding="utf-8")

reader = csv.reader(fp, delimiter=",", quotechar='"')

for field in reader:
    print(field[1], field[2])