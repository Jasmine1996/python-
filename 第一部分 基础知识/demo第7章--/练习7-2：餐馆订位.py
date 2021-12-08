"""
练习7-2：餐馆订位 　编写一个程序，询问用户有多少人用餐。如果超过8位，
就打印一条消息，指出没有空桌；否则指出有空桌。
"""
people = input("请问有多少人用餐？")
people = int(people)
if people > 8:
    print("不好意思，没有空位置了")
elif 8 >= people > 0:
    print("有空卓")