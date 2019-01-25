#! encoding:utf-8

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pypinyin import pinyin, lazy_pinyin

from databse import Base,Province,County,City,Street

engine = create_engine('sqlite:///Location4_12.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


f = open('data.json','rb')
jsonstr = f.read()

def createFourLevel(str):
    dict = json.loads(jsonstr)
    province_dict = dict['86']
    for provinde_code in province_dict:
        # 创建省数据
        province_name = province_dict[provinde_code]
        province_pinyin_name = ''.join(lazy_pinyin(province_name))
        # print provinde_code, province_name, province_pinyin_name
        province = Province(province_code=provinde_code, province_name=province_name, province_name_pinyin=province_pinyin_name)
        session.add(province)

        if provinde_code in dict:
            city_dict = dict[provinde_code]
            for city_code in city_dict:
                city_name = city_dict[city_code]
                city_pinyin_name = ''.join(lazy_pinyin(city_name))
                # print city_code, city_name, city_pinyin_name
                city = City(city_code=city_code, city_name= city_name, city_name_pinyin= city_pinyin_name, province_code=provinde_code)
                session.add(city)

                if city_code in dict:
                    county_dict = dict[city_code]
                    for county_code in county_dict:
                        county_name = county_dict[county_code]
                        county_pinyin_name = ''.join(lazy_pinyin(county_name))
                        # print county_code, county_name, county_pinyin_name

                        county = County(county_code=county_code, county_name=county_name,county_name_pinyin=county_pinyin_name,city_code=city_code)
                        session.add(county)

                        # 金门县我们没有下面的街道，
                        if county_code == '350527':
                            continue
                        filename = 'temp/{0}.json'.format(county_code)
                        with open(filename,'rb') as f:
                            towns_string = f.read()
                            if towns_string:
                                towns = json.loads(towns_string)
                                for town_code in towns:
                                    town_name = towns[town_code]
                                    town_pinyin_name = ''.join(lazy_pinyin(town_name))
                                    town = Street(street_code = town_code + "000",street_name=town_name,street_name_pinyin=town_pinyin_name,county_code=county_code)
                                    session.add(town)
                            else:
                                print('country = {0}没有找到',county_code)


    session.commit()

def createThreeLevel(str):
    dict = json.loads(jsonstr)
    province_dict = dict['86']
    for provinde_code in province_dict:
        # 创建省数据
        province_name = province_dict[provinde_code]
        province_pinyin_name = ''.join(lazy_pinyin(province_name))
        # print provinde_code, province_name, province_pinyin_name
        province = Province(province_code=provinde_code, province_name=province_name, province_name_pinyin=province_pinyin_name)
        session.add(province)

        if provinde_code in dict:
            city_dict = dict[provinde_code]
            for city_code in city_dict:
                city_name = city_dict[city_code]
                city_pinyin_name = ''.join(lazy_pinyin(city_name))
                # print city_code, city_name, city_pinyin_name
                city = City(city_code=city_code, city_name= city_name, city_name_pinyin= city_pinyin_name, province_code=provinde_code)
                session.add(city)

                if city_code in dict:
                    county_dict = dict[city_code]
                    for county_code in county_dict:
                        county_name = county_dict[county_code]
                        county_pinyin_name = ''.join(lazy_pinyin(county_name))
                        # print county_code, county_name, county_pinyin_name

                        county = County(county_code=county_code, county_name=county_name,county_name_pinyin=county_pinyin_name,city_code=city_code)
                        session.add(county)


    session.commit()


createFourLevel(jsonstr)
# pro = Province(id=1, province_code='2222')
# session.add(pro)
# session.commit()

