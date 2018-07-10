#! encoding:utf-8

from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# CREATE TABLE IF NOT EXISTS "sysconf_province" (
#   "id" bigint(20) PRIMARY KEY NOT NULL,
#   "createAt" datetime DEFAULT(NULL),
#   "status" int(11) DEFAULT(NULL),
#   "updateAt" datetime DEFAULT(NULL),
#   "version" int(11) DEFAULT(NULL),
#   "country_code" varchar(255) DEFAULT(NULL),
#   "province_code" varchar(255) DEFAULT(NULL),
#   "province_name" varchar(255) DEFAULT(NULL),
#   "province_name_pinyin" varchar(255) DEFAULT(NULL),
#   "province_type" varchar(255) DEFAULT(NULL)
# );
class Province(Base):
    __tablename__ = 'sysconf_province'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Integer, default=0)
    province_code = Column(String)
    province_name = Column(String)
    province_name_pinyin = Column(String)
    province_type = Column(Integer,default=1)

# CREATE TABLE IF NOT EXISTS "sysconf_city" (
#   "id" bigint(20) PRIMARY KEY NOT NULL,
#   "createAt" datetime DEFAULT(NULL),
#   "status" int(11) DEFAULT(NULL),
#   "updateAt" datetime DEFAULT(NULL),
#   "version" int(11) DEFAULT(NULL),
#   "city_code" varchar(255) DEFAULT(NULL),
#   "city_name" varchar(255) DEFAULT(NULL),
#   "city_name_pinyin" varchar(255) DEFAULT(NULL),
#   "province_code" varchar(255) DEFAULT(NULL)
# );
class City(Base):
    __tablename__ = 'sysconf_city'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Integer, default=0)
    city_code = Column(String)
    city_name = Column(String)
    city_name_pinyin = Column(String)
    province_code = Column(String)

# CREATE TABLE IF NOT EXISTS "sysconf_county" (
#   "id" bigint(20) PRIMARY KEY NOT NULL,
#   "createAt" datetime DEFAULT(NULL),
#   "status" int(11) DEFAULT(NULL),
#   "updateAt" datetime DEFAULT(NULL),
#   "version" int(11) DEFAULT(NULL),
#   "city_code" varchar(255) DEFAULT(NULL),
#   "county_code" varchar(255) DEFAULT(NULL),
#   "county_name" varchar(255) DEFAULT(NULL),
#   "county_name_pinyin" varchar(255) DEFAULT(NULL)
# );
class County(Base):
    __tablename__ = 'sysconf_county'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Integer, default=0)
    county_code = Column(String)
    county_name = Column(String)
    county_name_pinyin = Column(String)
    city_code = Column(String)

# 这是街道哟
class Street(Base):
    __tablename__ = 'sysconf_street'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Integer, default=0)
    street_code = Column(String)
    street_name = Column(String)
    street_name_pinyin = Column(String)
    county_code = Column(String)
