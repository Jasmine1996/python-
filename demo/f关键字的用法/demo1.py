"""
https://blog.csdn.net/lizhaoyi123/article/details/102731501
>>> a = 123.456
>>> f'a is {a:8.2f}'
'a is   123.46'
>>> f'a is {a:08.2f}'
'a is 00123.46'
>>> f'a is {a:8.2e}'
'a is 1.23e+02'
>>> f'a is {a:8.2%}'
'a is 12345.60%'
>>> f'a is {a:8.2g}'
'a is  1.2e+02'

>>> s = 'hello'
>>> f's is {s:8s}'
's is hello   '
>>> f's is {s:8.3s}'
's is hel
"""
a = "72 Fil"
print(f"{a.split()[0]}")

data_list= []
for i in range(10):
    data_list.append(f"{i}在不在")
print(data_list)