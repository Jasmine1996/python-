import requests
import json
import pandas as pd


def lotus_filscout_browser_block_output(miner_id='f0396751', date="24h"):
    """filscout.com 飞驰浏览器的产出统计 模块"""
    url = f"https://api2.filscout.com/api/v2/miner/{miner_id}/mining-data"
    headers = {'Content-Type': 'application/json'}
    data = f"{{\"statsType\": \"{date}\"}}"
    # print(url, headers, data)
    r = requests.post(url, headers=headers, data=data)
    # print(f"Status code {r.status_code}")
    # 将API响应值赋值给一个变量
    response_dict = r.json()
    # print(f"{response_dict.keys()}")
    # print(f"{response_dict.values()}")
    miner_dicts = response_dict['data']
    # print(f"miner {miner_dicts['miner']}")
    # print(f"{date} 算力增量 {miner_dicts['qualityPowerGrowthStr']}")
    # print(f"{date} 算力增速 {miner_dicts['provingPowerStr']}")
    # print(f"{date} 出块数量 {miner_dicts['blocks']}")
    # print(f"{date} 出块奖励 {miner_dicts['blockRewardStr']}")
    # print(f"{date} 幸运值为 {miner_dicts['luckyValue']}")
    # print(f"{date} 矿机当量为 {miner_dicts['machinesNum']}")
    # for key, value in miner_dicts.items():
    #     print(key, value)
    return miner_dicts



def lotus_filscout_browser_miner_info(miner_id="f0396751"):
    """filscout.com 飞驰浏览器的节点概况 + 算力概况 + 账户概览的api返回值的处理"""
    url2 = f"https://api2.filscout.com/api/v2/miner/{miner_id}"
    r2 = requests.post(url2)
    # print(f"Status code {r2.status_code}")
    requests_dict = r2.json()
    # 测试打印 这个字典
    # print(requests_dict.keys())
    # print(requests_dict.values())
    # 取出字典中的 data字段，赋值给另一个字典
    miner_dicts = requests_dict['data']
    # print(miner_dicts.keys())
    # print(miner_dicts.values())
    # 打印miner_dicts这个字典中需要的值
    # print(f"节点有效算力为 {miner_dicts['rawPowerStr']}")
    # print(f"节点扇区类型为 {miner_dicts['sectorSizeStr']}")
    # print(f"节点扇区个数统计 全部个数{miner_dicts['sectorCount']} "
    #       f"有效个数{miner_dicts['activeCount']} 错误个数{miner_dicts['faultCount']}"
    #       f"恢复中的扇区个数 {miner_dicts['recoveryCount']}")
    # print(f"全网排名{miner_dicts['powerRank']} 节点创建时间 {miner_dicts['createTime']}")
    return miner_dicts

def open_miner_execel(filename, sheet_name):
    """ 打开execel表格读取相关信息的函数。"""
    df = pd.read_excel(filename, sheet_name=sheet_name, index_col='miner')
    return df


def change_t_unit():
    """统一算力单位 P T G Bytes"""
    pass

def write_miner_execl(filename, sheet_name, data):
    locations, miner_ids, power_targets, qualityPowers, qualityPowerGrowth_7ds, qualityPowerGrowth_24hs,\
    expect_speeds, sectorSizeStrs, sectorCounts, luckyValue_24hs, luckyValue_7ds, luckyValue_30ds, blocks_7ds,\
    blockRewardStr_7ds, blocks_24hs, blockRewardStr_24hs = ([] for i in range(16))
    for i in range(len(data)):
        locations.append(data[i]['机房'])
        miner_ids.append(data[i]['节点号'])
        power_targets.append(data[i]['目标算力'])
        qualityPowers.append(data[i]['有效算力(TiB)'])
        qualityPowerGrowth_7ds.append(data[i]['周算力增长量(TiB)'])
        qualityPowerGrowth_24hs.append(data[i]['算力增长速度(TiB/day)'])
        expect_speeds.append(data[i]['客户要求算力增速'])
        sectorSizeStrs.append(data[i]['扇区大小'])
        sectorCounts.append(data[i]['当前扇区总数(个)'])
        luckyValue_24hs.append(data[i]['24h幸运值(%)'])
        luckyValue_7ds.append(data[i]['周幸运值(%)'])
        luckyValue_30ds.append(data[i]['30d幸运值(%)'])
        blocks_7ds.append(data[i]['周爆块数'])
        blockRewardStr_7ds.append(data[i]['周收益(Fil)'])
        blocks_24hs.append(data[i]['日爆块数'])
        blockRewardStr_24hs.append(data[i]['日收益(Fil)'])

        dfData = {
            '机房': locations,
            '节点号': miner_ids,
            '目标算力': power_targets,
            '有效算力(TiB)': qualityPowers,
            '周算力增长量(TiB)': qualityPowerGrowth_7ds,
            '算力增长速度(TiB/day)': qualityPowerGrowth_24hs,
            '客户要求算力增速': expect_speeds,
            '扇区大小': sectorSizeStrs,
            '当前扇区总数(个)': sectorCounts,
            '24h幸运值(%)': luckyValue_24hs,
            '周幸运值(%)': luckyValue_7ds,
            '30d幸运值(%)': luckyValue_30ds,
            '周爆块数': blocks_7ds,
            '周收益(Fil)': blockRewardStr_7ds,
            '日爆块数': blocks_24hs,
            '日收益(Fil)': blockRewardStr_24hs,
        }
        df = pd.DataFrame(dfData)
        # df.to_excel(filename, sheet_name=sheet_name, index=False, mode='a', engine='openpyxl')
        df.to_excel(filename, sheet_name=sheet_name, index=False)
        shop = pd.read_excel(filename, index_col='机房')
        shop.sort_values(by='机房', inplace=True)

date_list = ["24h", "7d", "30d"]
# lotus_filscout_browser_block_output() 函数需要传参，三个固定的时间值
# 测试函数
# open_miner_execel('../../../images/miner.xlsx', "lotus-miner钱包地址-汇总")
# post_api("f0396751", date_list[0])
# post_api("f0396751", date_list[1])
# post_api("f0396751", date_list[2])
# api_post_miner_info()
# execel文件路径和sheet名称定义
filename = '../../../images/miner.xlsx'
sheet_name = "lotus-miner钱包地址-汇总"
# sheet_name = 'Sheet1'

# execl中的字段定义变量
location = "机房"
power_target = "最终封装总算力"
name = "客户名称"

# 飞驰浏览器的api字段用中文替代，方便后续更改
# 有效算力 = 'qualityPowerStr'
有效算力 = 'qualityPower'
周算力增长量 = 'provingPower'
算力增长速度 = 'provingPower'
客户要求算力增速 = ''
扇区大小 = 'sectorSizeStr'
当前扇区总数 = 'sectorCount'
_24h幸运值 = 'luckyValue'
_7d幸运值 = 'luckyValue'
_30d幸运值 = 'luckyValue'
周爆块数 = 'blocks'
周收益 = 'blockRewardStr'
日爆块数 = 'blocks'
日收益 = 'blockRewardStr'
矿机当量 = 'machinesNum'
# 定义一个 空的字典和列表
dict_data = {}
list_data = []
# 读取节点信息的execl
dict_miner_xlsx = open_miner_execel(filename, sheet_name)
# 批量获取各个节点的浏览器信息，存储字典和列表
for miner_id in dict_miner_xlsx.index:

    # print(dict_miner_xlsx.loc[miner_id][location], miner_id, dict_miner_xlsx.loc[miner_id][power_target])
    dict_miner_info = lotus_filscout_browser_miner_info(miner_id)
    dict_block_output_24h = lotus_filscout_browser_block_output(miner_id, date_list[0])
    dict_block_output_7d = lotus_filscout_browser_block_output(miner_id, date_list[1])
    dict_block_output_30d = lotus_filscout_browser_block_output(miner_id, date_list[2])
    # print(dict_miner_xlsx, dict_miner_info, dict_block_output_24h, dict_block_output_7d, dict_block_output_30d)

    try:
        if dict_block_output_24h[矿机当量] == 0:
            客户要求算力增速 = "已暂停"
        else:
            客户要求算力增速 = "增速无要求"
        print(f"{dict_miner_xlsx.loc[miner_id][location]}\t{miner_id}\t{dict_miner_xlsx.loc[miner_id][power_target]}\t"
              f"{dict_miner_info[有效算力]/(1024**4):8.2f}\t{dict_block_output_7d[周算力增长量]/(1024**4):8.2f}\t{dict_block_output_24h[算力增长速度]/(1024**4):8.2f}\t"
              f"{客户要求算力增速}\t{dict_miner_info[扇区大小]}\t{dict_miner_info[当前扇区总数]}\t"
              f"{dict_block_output_24h[_24h幸运值]:8.2%}\t{dict_block_output_7d[_7d幸运值]:8.2%}\t{dict_block_output_30d[_30d幸运值]:8.2%}\t"
              f"{dict_block_output_7d[周爆块数]}\t{dict_block_output_7d[周收益].split()[0]}\t{dict_block_output_24h[日爆块数]}\t"
              f"{dict_block_output_24h[日收益].split()[0]}")
        dict_data['机房'] = dict_miner_xlsx.loc[miner_id][location]
        dict_data['节点号'] = miner_id
        dict_data['目标算力'] = dict_miner_xlsx.loc[miner_id][power_target]
        dict_data['有效算力(TiB)'] = f"{dict_miner_info[有效算力]/(1024**4):8.2f}"
        dict_data['周算力增长量(TiB)'] = f"{dict_block_output_7d[周算力增长量]/(1024**4):8.2f}"
        dict_data['算力增长速度(TiB/day)'] = f"{dict_block_output_24h[算力增长速度]/(1024**4):8.2f}"
        dict_data['客户要求算力增速'] = 客户要求算力增速
        dict_data['扇区大小'] = dict_miner_info[扇区大小]
        dict_data['当前扇区总数(个)'] = dict_miner_info[当前扇区总数]
        dict_data['24h幸运值(%)'] = f"{dict_block_output_24h[_24h幸运值]:8.2%}".split("%")[0]
        dict_data['周幸运值(%)'] = f"{dict_block_output_7d[_7d幸运值]:8.2%}".split("%")[0]
        dict_data['30d幸运值(%)'] = f"{dict_block_output_30d[_30d幸运值]:8.2%}".split("%")[0]
        dict_data['周爆块数'] = dict_block_output_7d[周爆块数]
        dict_data['周收益(Fil)'] = dict_block_output_7d[周收益].split()[0]
        dict_data['日爆块数'] = dict_block_output_24h[日爆块数]
        dict_data['日收益(Fil)'] = dict_block_output_24h[日收益].split()[0]
        # 注意此处字典在for循环里append到一个列表里，需要使用dict().copy() 方法来添加，不然使用的都是同一个内存地址，
        # 存储到列表里都是同一个字典项，均为最后一个字典的内存从地址。(类似于切片的原理)
        list_data.append(dict_data.copy())

    except TypeError:
        print(f"{miner_id} 是还未启动的节点，只能查询到miner信息，产出统计的data字段为空")
        # print(dict_miner_xlsx, dict_miner_info, dict_block_output_24h, dict_block_output_7d, dict_block_output_30d)
        pass

# 写入新的execl表格
write_filename = '../../../images/test.xlsx'
write_sheet_name = 'test'
# 按照机房对list_data列表进行排序。
list_data.sort(key=lambda s: s['机房'][0:])
write_miner_execl(write_filename, write_sheet_name, list_data)

