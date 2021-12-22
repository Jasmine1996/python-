import pandas as pd


def pd_toExcel(data, fileName, sheetname):  # pandas库储存数据到excel
    ids = []
    names = []
    prices = []
    for i in range(len(data)):
        ids.append(data[i]["id"])
        names.append(data[i]["name"])
        prices.append(data[i]["price"])

    dfData = {  # 用字典设置DataFrame所需数据
        '序号': ids,
        '酒店': names,
        '价格': prices
    }
    df = pd.DataFrame(dfData)  # 创建DataFrame
    df.to_excel(fileName, index=False, sheet_name=sheetname)  # 存表，去除原始索引列（0,1,2...）


# "-------------数据用例-------------"
testData = [
    {"id": 1, "name": "立智", "price": 100},
    {"id": 2, "name": "维纳", "price": 200},
    {"id": 3, "name": "如家", "price": 300},
]

fileName = '../../images/test.xlsx'
# sheetname = "lotus-miner钱包地址-汇总"
sheetname = 'Sheet1'
pd_toExcel(testData, fileName, sheetname)