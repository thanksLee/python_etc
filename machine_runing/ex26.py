import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj = Series([4, 7, -5, 3])

print(obj)
print(obj.values)
print(obj.index)

obj1 = Series([('h', 2), ('m', 3), ('r', 0), ('s', 6), ('p', 5), ('a', 4), ('e', 1)])

print(obj1)

print()
print()
print()
print()

obj2 = Series([10, 1, 8, 3], index=['x', 'y', 'z', 'w'])
print(obj2)
print(obj2.index)
print()
print()
print()

data = {'state' : ['Seoul', 'Deagu', 'Incheon'],
        'year' : [2000, 2010, 2015]
        }
frame = DataFrame(data)
print(frame)

