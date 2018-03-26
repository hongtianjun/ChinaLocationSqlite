#! encoding:utf-8

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pypinyin import pinyin, lazy_pinyin

from databse import Base,Province,County,City

engine = create_engine('sqlite:///Location.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


f = open('data.json','r')
jsonstr = f.read()

dict = json.loads(jsonstr)
province_dict = dict['86']
for provinde_code in province_dict:
    # 创建省数据
    province_name = province_dict[provinde_code]
    province_pinyin_name = ''.join(lazy_pinyin(province_name))
    print provinde_code, province_name, province_pinyin_name
    province = Province(province_code=provinde_code, province_name=province_name, province_name_pinyin=province_pinyin_name)
    session.add(province)

    if provinde_code in dict:
        city_dict = dict[provinde_code]
        for city_code in city_dict:
            city_name = city_dict[city_code]
            city_pinyin_name = ''.join(lazy_pinyin(city_name))
            print city_code, city_name, city_pinyin_name
            city = City(city_code=city_code, city_name= city_name, city_name_pinyin= city_pinyin_name, province_code=provinde_code)
            session.add(city)

            if city_code in dict:
                county_dict = dict[city_code]
                for county_code in county_dict:
                    county_name = county_dict[county_code]
                    county_pinyin_name = ''.join(lazy_pinyin(county_name))
                    print county_code, county_name, county_pinyin_name

                    county = County(county_code=county_code, county_name=county_name,county_name_pinyin=county_pinyin_name,city_code=city_code)
                    session.add(county)


session.commit()



# pro = Province(id=1, province_code='2222')
# session.add(pro)
# session.commit()

