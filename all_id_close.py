#计算复权因子，并且计算复权后的各个品种收盘建
import rqdatac as rq
from rqdatac import *
import pandas as pd
import numpy as np
from datetime import datetime , timedelta
rq.init()

startdate=pd.to_datetime('20050104')
enddate=pd.to_datetime('20170120')
#获取所有品种
cat_list=pd.read_csv("cat_list.csv",header=None,index_col=0)
cat_list=pd.Series(cat_list.groupby(cat_list.iloc[:,0]).count().index)
cat_all_price=pd.DataFrame()

for n in range(0,len(cat_list)):
    # a表示同一品种主力合约的时间序列
    a = get_dominant_future(cat_list[n], startdate, enddate)
    a = a.to_frame()
    # b表示同一品种的所有主力合约
    b = a.groupby(a.ix[:, 'dominant']).count().index
    b = pd.Series(b)
    #初始化cat,cat用以保存所有主力合约在所有时间点的收盘价
    cat=a
    # 获取单个合约信息
    for i in range(0, len(b)):
        # b_history1表示单个合约历史收盘价df
        b_history1 = get_price(b[i], startdate, enddate)
        b_history1 = b_history1.ix[:, 'close']
        b_history1 = b_history1.to_frame()
        # 列重命名为合约名称
        b_history1.columns = [b[i]]
        # cat和b_history1合并
        cat = cat.join(b_history1, how='outer')

    # 判断是否存在主力切换
    #新建一个数据框cat_switch，用以计算切换后的收盘价
    cat_switch = cat
    cat_switch['switch'] = None
    #如果第j天结束的时候存在切换，把第j+1天记为True，表示已经切换过了
    for j in range(0, len(cat_switch) - 1):
        if (cat_switch.ix[j, 'dominant'] == cat_switch.ix[j + 1, 'dominant']):
            cat_switch.ix[j + 1, ['switch']] = False
        else:
            cat_switch.ix[j + 1, ['switch']] = True
    # 标记第1天
    cat_switch.ix[0, 'switch'] = False

    # 增加两列用于记录主力收盘价
    cat_switch['price1'] = None
    cat_switch['price2'] = None
    # price1表示正常价格
    for k in range(0, len(cat_switch)):
        dominant_name1 = cat_switch.ix[k, 'dominant']
        cat_switch.ix[k, 'price1'] = float(cat_switch.ix[k, dominant_name1])
    # price2表示往前复权一天的价格
    for m in range(0, len(cat_switch)):
        if (cat_switch.ix[m, 'switch']):
            #创建一个中间变量，用以记录切换时的主力合约id
            dominant_name2 = cat_switch.ix[m, 'dominant']
            cat_switch.ix[m - 1, 'price2'] = float(cat_switch.ix[m - 1, dominant_name2])
            cat_switch.ix[m, 'price2'] = float(cat_switch.ix[m, dominant_name2])
        else:
            dominant_name2 = cat_switch.ix[m, 'dominant']
            cat_switch.ix[m, 'price2'] = float(cat_switch.ix[m, dominant_name2])
    # 计算复权因子
    # 把price1price2转化为数值型
    cat_switch.ix[:, ['price1']] = cat_switch.ix[:, ['price1']].values
    cat_switch.ix[:, ['price2']] = cat_switch.ix[:, ['price2']].values

    # 计算
    cat_switch['restore_factor1'] = cat_switch.apply(lambda x: x['price1'] / x['price2'], axis=1)
    test = cat_switch['restore_factor1'].cumprod().values
    test1 = np.array([1])
    test = np.append(test1, test)
    test = np.delete(test, len(test)-1)
    test = pd.Series(data=test, index=cat_switch.index)
    test = test.to_frame()
    test.columns = ['restore_factor2']
    cat_switch = cat_switch.join(test, how='outer')

    # 计算复权后的价格
    cat_switch['price_restored'] = cat_switch.apply(lambda x: x['restore_factor2'] * x['price1'], axis=1)
    cat_single = cat_switch.ix[:, ['dominant', 'price_restored']]
    #保存每个品种的主力合约、收盘价时间序列
    cat_single.to_csv(cat_list[n]+".csv")
    cat_single1=cat_switch.ix[:,['price_restored']]
    cat_all_price=cat_all_price.join(cat_single1, how='outer', rsuffix=cat_list[n])

cat_all_price.rename(columns={'price_restored':'price_restoredA'})
#将所有品种复权后的收盘价保存
cat_all_price.to_csv("cat_all_price.csv")