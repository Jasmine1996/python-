a = [
    {
        "value": "用途",
        "name": "t4"
    },
    {
        "value": "期初累计摊额",
        "name": "t10"
    },
    {
        "value": "原值",
        "name": "t5"
    },
    {
        "value": "增加日期",
        "name": "t3"
    },
    {
        "value": "摊销期数",
        "name": "t7"
    },
    {
        "value": "净残值",
        "name": "t6"
    },
    {
        "value": "本月摊销额",
        "name": "t9"
    },
    {
        "value": "减值准备累计",
        "name": "t8"
    },
    {
        "value": "期末累计摊销额",
        "name": "t11"
    },
    {
        "value": "无形资产名称",
        "name": "t2"
    },
    {
        "value": "序号",
        "name": "t1"
    }
]

# 对a按照t的下标大小进行排序
a.sort(key=lambda s: s["value"][0:])
# b = a.sorted(key=lambda s: int(s["value"][1:]))
# print(b)
print(a)
a.s
