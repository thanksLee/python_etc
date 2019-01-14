import openpyxl

fileNm = "stat_100701.xlsx"

book = openpyxl.load_workbook(fileNm)

# 첫번째 시트를 추출하기
sheet = book.worksheets[0]

# 시트의 행을 순서대로 추출하기
excel_record = []

for record in sheet.rows:
    excel_record.append([
        record[0].value,
        record[8].value
    ])

print(excel_record)

del excel_record[0]
del excel_record[0]
del excel_record[0]
del excel_record[0]
del excel_record[0]
del excel_record[17]
del excel_record[17]
del excel_record[17]
del excel_record[17]
del excel_record[17]



i = 0
for data in excel_record:
    i += 1
    data[1] = data[1].replace(",", "")
    data[1] = int(data[1])
    print(i, data)

print()
print()
print()
print()
print()

# 데이터를 인구순으로 정렬하기 위한 값을 선택
excel_record = sorted(excel_record, key = lambda x : x[1])
i = 0
for data in excel_record:
    i += 1
    print(i, data)


# 하위 5개 지역 추출

print("------------------------------------")

for j, name in enumerate(excel_record):
    if (j > 4) : break
    print(j + 1, j, name[0], name[1])

print("------------------------------------")
print()
print()
print()
print()
print(chr(65))
print(chr(66))
print(chr(67))
print(chr(68))
print()
print()
print()
print()
print()

book.close()
# 서울과 계에 해당하는 값을 제외한 인구수 합산하기
book = openpyxl.load_workbook(fileNm)
# 첫번째 시트를 추출하기
sheet = book.worksheets[0]

for i in range(0, 8):
    total = sheet[chr(i + 66) + "5"].value
    total = int(total.replace(",", ""))
    seoul = sheet[chr(i + 66) + "6"].value
    seoul = int(seoul.replace(",", ""))
    reval = format(total - seoul, ',')

    print(total, " - ", seoul, " = ", reval)

    # 필요 없는 값 지우기
    print(sheet[chr(65) + "24"].value)
    sheet[chr(65) + "24"].value = "서울을 제외한"
    sheet[chr(i + 66) + "9"].value = ""
    sheet[chr(i + 66) + "26"].value = ""
    sheet[chr(i + 66) + "27"].value = ""

    sheet[chr(i + 66) + "24"].value = reval
    cell = sheet[chr(i + 66) + "24"]

    cell.font = openpyxl.styles.Font(size=14, color="FF0000")

# Excel 파일에 결과 쓰기
newFileNm = "New_" + fileNm
book.save(newFileNm)
print("파일이 저장되었습니다.")
