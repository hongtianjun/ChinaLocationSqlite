#! coding:utf-8
import os
import json
import random
import time
import requests

def getStreet(code):
	url = 'http://passer-by.com/data_location/town/{0}.json'.format(code)
	res = requests.get(url)
	if res.status_code == 200:
		return res.json()
	else:

		print('{0}返回了{1}'.format(code,res.status_code))
		raise 

f = open('data.json','rb')
jsonstr = f.read()
dict = json.loads(jsonstr)
province_dict = dict['86']
for provinde_code in province_dict:
    if provinde_code in dict:
        city_dict = dict[provinde_code]
        for city_code in city_dict:
            if city_code in dict:
                county_dict = dict[city_code]
                for county_code in county_dict:
                    path = 'temp/{0}.json'.format(county_code)
                    # 如果已经下载就不下载了，有时会中断，下次会从新开始
                    if os.path.exists(path):
                    	print('{0}已存在!'.format(path))
                    	continue

                    # if county_code == '350527':
                    # 	continue

                    streets = getStreet(county_code)
                    with open(path, 'w+') as f:
                    	print(type(streets))
                    	print(json.dumps(streets))
                    	f.write(json.dumps(streets))
                    # time.sleep(random.randint(3,10))

