import numpy as np

# 다차원 배열
data = np.random.randn(2, 3)

print(data)

x = np.array([1.0, 2.0, 3.0])

print(x)

print(type(x))

print()
print()
print()

y = np.array([2.0, 4.0, 6.0])
print(y)
print()
# 연산시 x, y의 원소의 개수가 같아야 한다. 그렇지 않으면 오류 발생
print(x+y, ', ', x-y, ', ', x*y, ', ', x/y)
print()
print()
print()

A = np.array([[1, 2], [3, 4]])
print(A)

print(A.shape)
print(A.dtype)

print()
print()

B = np.array([[3, 0], [0, 6]])
print(B)
print(A+B, ", ", A-B, ", ", A*B, ", ", A/B)

