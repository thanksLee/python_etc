a = 10
print(type(a))


aa = [100, 200, 300]

print(aa)

print(len(aa))

ss = [ '하이assdfas', '헬로', '안녕']
print(ss[2])

print(ss[0:1])
print(ss[:-1])  # 처음부터 마지막 원소의 1개 앞까지

print(ss[-1]) # 뒤에서 부터 가져온다.
# print(ss[3]) 없는 것을 가져오려면 오류 발생
ss.append("몰라")
print(ss)

print(ss[3])

# ss.insert("땡큐") 오류 발생
ss.insert(2, "땡큐")
print(ss)

ss.insert(5, "방가")
print(ss)

ss.insert(10, "에에") # 인덱스가 없다면 맨 뒤에 추가
print(ss)

##### 튜플 #####
tt = 1, 2, 3, 4
print(tt)

##### dictionary ######

dit = {"name":"홍길동", "주소":"서울특별시", "성별":"남성"}
print(dit)
dit["tel"] = "010-111-1111"

print(dit)

del dit["주소"]
print(dit)

print("## 키 값만 구하고 싶을 때 ##")
print(dit.keys())
ditList = list(dit.keys())
print(ditList)

for i in dit.keys():
    print(dit[i])

