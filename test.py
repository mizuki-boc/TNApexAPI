from pprint import pprint
import os
import sys
import json
import requests

base_url = "https://public-api.tracker.gg/v2/apex/standard/"

import key

params = {"TRN-Api-Key": key.API_KEY}

user_name = "m1zuki96"

endpoint = "profile/origin/" + user_name
session = requests.Session()
req = session.get(base_url+endpoint, params=params)
print("ステータスコード: " + str(req.status_code))
req.close()
res = json.loads(req.text)
# pprint(res)

'''
上記コードで動作確認済み (Python 3.8.5)
- 存在しないユーザIDを入力した場合，ステータスコード 404 で，エラーメッセージがかえってくる

'''

# ランク，アクティブなレジェンド，アクティブなレジェンドでのキル数 を表示する
'''
ランク表示
displayValue がカンマありの str 型
value は float 型
'''
rank_value = res["data"]["segments"][0]["stats"]["rankScore"]["value"]
rank_name = res["data"]["segments"][0]["stats"]["rankScore"]["metadata"]["rankName"]
print("ユーザ名: ", user_name)
print("ランク: " + rank_name + " (", rank_value,  ")")

'''
アクティブなレジェンドとそのレジェンドでのキル数 の表示
'''
active_legends = res["data"]["metadata"]["activeLegendName"]
active_legends_kills = res["data"]["segments"][1]["stats"]["kills"]["value"]
print("使用したレジェンド: " + active_legends)
print("使用レジェンドのキル数: ", active_legends_kills)

'''
ここまでで，

ステータスコード: 200
ユーザ名:  m1zuki96
ランク: Gold 2 ( 3900.0 )
使用したレジェンド: Bangalore
使用レジェンドのキル数:  30.0

こんな感じで出力される．
'''