import pandas as pd

filename = '../../images/miner.xlsx'
# sheetname = "lotus-miner钱包地址-汇总"
sheetname = 'Sheet1'
location = "机房"
power_target = "最终封装总算力"
name = "客户名称"
df = pd.read_excel(filename, sheet_name=sheetname, index_col='miner')
print(df.index)
for miner in df.index:
    print(df.loc[miner][location], miner, df.loc[miner][power_target])
a = False
