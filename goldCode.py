#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
import urllib.request
from urllib.parse import urlencode
import pmysql as pq
import time

p = pq.pmysql()
# ----------------------------------
# 黄金数据调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/29
# ----------------------------------

# 配置您申请的APPKey
appkey = "7e71ac026772617efa281376815d1696"

# 上海期货交易所
url1 = "http://web.juhe.cn:8080/finance/gold/shfuture"

# 银行账户黄金
url2 = "http://web.juhe.cn:8080/finance/gold/bankgold"

# 上海黄金交易所
url3 = "http://web.juhe.cn:8080/finance/gold/shgold"

'''"resultcode": "200",
"reason": "SUCCESSED!",
"result": [
    {
        "1": {
             "variety": "Ag(T+D)", / * 品种 * /
             "latestpri":"6585.00", / *最新价 * /
             "openpri": "6712.00", / *开盘价 * /
             "maxpri": "6721.00", / *最高价 * /
             "minpri": "6581.00", / *最低价 * /
             "limit": "-1.98%", / *涨跌幅 * /
             "yespri": "6718.00", / *昨收价 * /
             "totalvol": "1564524.0000", / *总成交量 * /
             "time": "2012-12-19 15:29:59" / * 更新时间 * /
}'''


def request(appkey=appkey, m="GET"):
    params = {
        "key": appkey,  # APP Key
        "v": "",  # JSON格式版本(0或1)默认为0
    }
    params = urlencode(params)
    f = urllib.request.urlopen(url3 + '?' + params)
    content = f.read()
    res = json.loads(content)
    # return res
    if res['error_code'] == 0: #and time.mktime(time.strptime(res['result'][0]['1']['time'],'%Y-%m-%d %H:%M:%S')) not in p.msql('select upTime from goldData where upTime=\'%f\';'%(time.mktime(time.mktime(time.strptime(res['result'][0]['1']['time'],'%Y-%m-%d %H:%M:%S'))))):
        for key in res['result'][0]:
            p.msql(
                'insert into goldData(code,variety,latestpri,openpri,maxpri,minpri,linit,yespri,totalvol,upTime,t) values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');'
                % ('黄金', res['result'][0][key]['variety'], res['result'][0][key]['latestpri'],
                   res['result'][0][key]['openpri'], res['result'][0][key]['maxpri'],
                   res['result'][0][key]['minpri'], res['result'][0][key]['limit'],
                   res['result'][0][key]['yespri'], res['result'][0][key]['totalvol'],
                   res['result'][0][key]['time'],float(time.time())
                   )
            )
