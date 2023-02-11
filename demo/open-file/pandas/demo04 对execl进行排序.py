import pandas as pd
# 参考链接https://zhuanlan.zhihu.com/p/331783338
# https://www.jianshu.com/p/f0ed06cd5003
filename = '../../images/test.xlsx'
sheet_name = 'Sheet2'

# shop = pd.read_csv(filename, index_col=0, encoding='unicode_escape', error_bad_lines=False)
# shop.sort_values(by='location', inplace=True)
stexcel = pd.read_excel(filename)
stexcel.sort_values(by='机房', inplace=True, ascending=False)
stexcel.to_excel(filename, index=False)
print(stexcel)