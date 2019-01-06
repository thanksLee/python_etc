import collections

dic1 = collections.OrderedDict()

dic1["경기"] = "의정부"

dic1["서울"] = "강남"

dic1["부산"] = "광안리"

dic1["대구"] = "몰라"

dic1["제주"] = "남양주"


print(dic1)
for i, j in dic1.items():

    print(i, j)