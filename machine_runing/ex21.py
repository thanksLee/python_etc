import codecs

fileNm = "prod_list.csv"
csv = codecs.open(fileNm, "r", encoding="utf-8").read()

data = []
records = csv.split("\r\n") #\r:CR \n:LF(new line)

for rec in records:
    if rec == "": continue
    fields = rec.split(",")
    data.append(fields)

for field in data:
    print(field[1], field[2])