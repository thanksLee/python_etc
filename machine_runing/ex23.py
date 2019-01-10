import openpyxl

# 엑셀파일 열기
fileNm = "02.base_user_info.xlsx"

# 엑셀파일을 불러오기
book = openpyxl.load_workbook(fileNm)

# 엑셒파일에서 원하는 sheet를 추출하기
# worksheets[] : index가 0, 1, 2로 배열과 같은 인덱스 사용
sheet = book.worksheets[0] #첫번째 시트를 가져온다.

# 시트의 각 행을 순서대로 추출해보기
excel_data = [] #엑셀의 각 행을 담기위한 리스트

for row in sheet.rows:
    excel_data.append([
        row[0].value,
        row[1].value,
        row[2].value,
        row[3].value
    ])

print(excel_data)
print()
print()
print()

# 필요없는행(헤더) 제거하기
#del excel_data[0]

for data in excel_data:
    print(data)