import pandas as pd

filename = '../../images/miner.xlsx'
sheetname = "lotus-miner钱包地址-汇总"

df = pd.read_excel(filename, sheet_name=sheetname)
print(df)
# 3.读取excel的某一个sheet
df = pd.read_excel(filename, sheet_name=sheetname)
print(df)
# 4.获取列标题
print(df.columns)
# 5.获取列行标题
print(df.index)
# 6.制定打印某一列
print(df["miner"])
# 7.描述数据
print(df.describe())

# 8. 已miner为索引(index_col)
# df = pd.read_excel(filename, sheet_name=sheetname, index_col='miner')
# 打印指定的索引，数据格式为一个列表
# print(df.index)
