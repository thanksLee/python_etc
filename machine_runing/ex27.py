import pandas as pd

fileNm = "stat_100701.xlsx"
sheet_name = "Sheet0"

book = pd.read_excel(fileNm, sheet_name=sheet_name, header=3)
book = book.sort_values(by="인구", ascending=False)

print(book)

