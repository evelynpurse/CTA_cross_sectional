#获取期货品种
import rqdatac as rq
from rqdatac import *
import pandas as pd
import numpy as np
from datetime import datetime , timedelta
rq.init()
#设置开始日期，结束日期
startdate=pd.to_datetime('20050104')
enddate=pd.to_datetime('20170120')

#获取所有期货合约
future_info=all_instruments(type='Future')

#获取详细信息
future_info=future_info[['listed_date','maturity_date','order_book_id','symbol','margin_rate','contract_multiplier','underlying_symbol']]
#剔除期货指数
future_info=future_info[~future_info['listed_date'].isin(['0000-00-00'])]
#转化为日期
future_info['listed_date']=pd.to_datetime(future_info['listed_date'],format='%Y-%m-%d')
future_info['maturity_date']=pd.to_datetime(future_info['maturity_date'],format='%Y-%m-%d')
#计算发行了多久
future_info['day2day']=future_info['listed_date'].apply(lambda x:enddate-x)
#剔除天数小于180的
future_info=future_info[future_info.day2day>timedelta(180)]
#将所有合约根据品种分类，从而获得品种列表
a=future_info.groupby(future_info['underlying_symbol']).count()
b=a.index
b=pd.Series(b)
#另外发现RQ没有S种类的合约，剔除S种类
b=b.drop(42)
#GN品种已经被暂停交易也剔除
b=b.drop(15)
#保存品种列表
b=pd.Series(b.values)
b.to_csv("cat_list.csv",header=None)
cat_list=pd.read_csv("cat_list.csv",header=None,index_col=0)
cat_list=pd.Series(cat_list.groupby(cat_list.iloc[:,0]).count().index)
#剔除金融期货
cat_list=cat_list.drop([17,18,19,45,48])
cat_list.to_csv("cat_list.csv",header=None)



