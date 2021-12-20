import requests

def post_api(miner_id='f0396751',date="24h" ):
    # 飞驰浏览器的api
    url = f"https://api2.filscout.com/api/v2/miner/{miner_id}/mining-data"
    headers = {'Content-Type': 'application/json'}
    data = f"{{\"statsType\": \"{date}\"}}"
    # print(url, headers, data)
    r = requests.post(url, headers=headers, data=data)
    print(f"Status code {r.status_code}")

    # 将API响应值赋值给一个变量
    response_dict = r.json()

    print(f"{response_dict.keys()}")
    print(f"{response_dict.values()}")

    miner_dicts = response_dict['data']
    # print(f"miner {miner_dicts['miner']}")
    # print(f"算力增量 {miner_dicts['qualityPowerGrowthStr']}")
    # print(f"算力增速 {miner_dicts['provingPowerStr']}")

    for key, value in miner_dicts.items():
        print(key, value)

post_api("f054412","7d")