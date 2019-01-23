import numpy as np
import pandas as pd
import datetime
from datetime import datetime , timedelta


cat_list=pd.read_csv("cat_list.csv",header=None,index_col=0)
cat_list=pd.Series(cat_list.groupby(cat_list.iloc[:,0]).count().index)
#最外层大循环
for i in range(0,len(cat_list)):
    A = pd.read_csv(cat_list[i]+".csv", index_col=0)
    # 计算5日收益率
    test = A['price_restored'].values
    test1 = np.array([None, None, None, None, None])
    test = np.append(test1, test)
    test = np.delete(test, [len(test) - 1, len(test) - 2, len(test) - 3, len(test) - 4, len(test) - 5])
    test = pd.Series(data=test, index=A.index)
    test = test.to_frame()
    test.columns = ['price_restored5']
    A = A.join(test, how='outer')
    A.ix[:, ['price_restored5']] = A.ix[:, ['price_restored5']].values
    A['5_day_rt'] = A.apply(lambda x: (x['price_restored'] - x['price_restored5']) / x['price_restored5'], axis=1)
    # R=10
    test = A['price_restored'].values
    test1 = np.array([None, None, None, None, None, None, None, None, None, None])
    test = np.append(test1, test)
    test = np.delete(test, [len(test) - 1, len(test) - 2, len(test) - 3, len(test) - 4, len(test) - 5, len(test) - 6,
                            len(test) - 7, len(test) - 8, len(test) - 9, len(test) - 10])
    test = pd.Series(data=test, index=A.index)
    test = test.to_frame()
    test.columns = ['price_restored10']
    A = A.join(test, how='outer')
    A.ix[:, ['price_restored10']] = A.ix[:, ['price_restored10']].values
    A['10_day_rt'] = A.apply(lambda x: (x['price_restored'] - x['price_restored10']) / x['price_restored10'], axis=1)
    # R=15
    test = A['price_restored'].values
    test1 = np.array([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
    test = np.append(test1, test)
    l = len(test)
    test = np.delete(test,
                     [l - 1, l - 2, l - 3, l - 4, l - 5, l - 6, l - 7, l - 8, l - 9, l - 10, l - 11, l - 12, l - 13,
                      l - 14, l - 15])
    test = pd.Series(data=test, index=A.index)
    test = test.to_frame()
    test.columns = ['price_restored15']
    A = A.join(test, how='outer')
    A.ix[:, ['price_restored15']] = A.ix[:, ['price_restored15']].values
    A['15_day_rt'] = A.apply(lambda x: (x['price_restored'] - x['price_restored15']) / x['price_restored15'], axis=1)
    # R=20
    test = A['price_restored'].values
    test1 = np.array(
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None])
    test = np.append(test1, test)
    l = len(test)
    test = np.delete(test,
                     [l - 1, l - 2, l - 3, l - 4, l - 5, l - 6, l - 7, l - 8, l - 9, l - 10, l - 11, l - 12, l - 13,
                      l - 14, l - 15, l - 16, l - 17, l - 18, l - 19, l - 20])
    test = pd.Series(data=test, index=A.index)
    test = test.to_frame()
    test.columns = ['price_restored20']
    A = A.join(test, how='outer')
    A.ix[:, ['price_restored20']] = A.ix[:, ['price_restored20']].values
    A['20_day_rt'] = A.apply(lambda x: (x['price_restored'] - x['price_restored20']) / x['price_restored20'], axis=1)
    # R=25
    test = A['price_restored'].values
    test1 = np.array(
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None])
    test = np.append(test1, test)
    l = len(test)
    test = np.delete(test,
                     [l - 1, l - 2, l - 3, l - 4, l - 5, l - 6, l - 7, l - 8, l - 9, l - 10, l - 11, l - 12, l - 13,
                      l - 14, l - 15, l - 16, l - 17, l - 18, l - 19, l - 20, l - 21, l - 22, l - 23, l - 24, l - 25])
    test = pd.Series(data=test, index=A.index)
    test = test.to_frame()
    test.columns = ['price_restored25']
    A = A.join(test, how='outer')
    A.ix[:, ['price_restored25']] = A.ix[:, ['price_restored25']].values
    A['25_day_rt'] = A.apply(lambda x: (x['price_restored'] - x['price_restored25']) / x['price_restored25'], axis=1)
    # R=30
    test = A['price_restored'].values
    test1 = np.array(
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None])
    test = np.append(test1, test)
    l = len(test)
    test = np.delete(test,
                     [l - 1, l - 2, l - 3, l - 4, l - 5, l - 6, l - 7, l - 8, l - 9, l - 10, l - 11, l - 12, l - 13,
                      l - 14, l - 15, l - 16, l - 17, l - 18, l - 19, l - 20, l - 21, l - 22, l - 23, l - 24, l - 25,
                      l - 26, l - 27, l - 28, l - 29, l - 30])
    test = pd.Series(data=test, index=A.index)
    test = test.to_frame()
    test.columns = ['price_restored30']
    A = A.join(test, how='outer')
    A.ix[:, ['price_restored30']] = A.ix[:, ['price_restored30']].values
    A['30_day_rt'] = A.apply(lambda x: (x['price_restored'] - x['price_restored30']) / x['price_restored30'], axis=1)
    # R=35
    test = A['price_restored'].values
    test1 = np.array(
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
    test = np.append(test1, test)
    l = len(test)
    test = np.delete(test,
                     [l - 1, l - 2, l - 3, l - 4, l - 5, l - 6, l - 7, l - 8, l - 9, l - 10, l - 11, l - 12, l - 13,
                      l - 14, l - 15, l - 16, l - 17, l - 18, l - 19, l - 20, l - 21, l - 22, l - 23, l - 24, l - 25,
                      l - 26, l - 27, l - 28, l - 29, l - 30, l - 31, l - 32, l - 33, l - 34, l - 35])
    test = pd.Series(data=test, index=A.index)
    test = test.to_frame()
    test.columns = ['price_restored35']
    A = A.join(test, how='outer')
    A.ix[:, ['price_restored35']] = A.ix[:, ['price_restored35']].values
    A['35_day_rt'] = A.apply(lambda x: (x['price_restored'] - x['price_restored35']) / x['price_restored35'], axis=1)
    # R=40
    test = A['price_restored'].values
    test1 = np.array(
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None])
    test = np.append(test1, test)
    l = len(test)
    test = np.delete(test,
                     [l - 1, l - 2, l - 3, l - 4, l - 5, l - 6, l - 7, l - 8, l - 9, l - 10, l - 11, l - 12, l - 13,
                      l - 14, l - 15, l - 16, l - 17, l - 18, l - 19, l - 20, l - 21, l - 22, l - 23, l - 24, l - 25,
                      l - 26, l - 27, l - 28, l - 29, l - 30, l - 31, l - 32, l - 33, l - 34, l - 35, l - 36, l - 37,
                      l - 38, l - 39, l - 40])
    test = pd.Series(data=test, index=A.index)
    test = test.to_frame()
    test.columns = ['price_restored40']
    A = A.join(test, how='outer')
    A.ix[:, ['price_restored40']] = A.ix[:, ['price_restored40']].values
    A['40_day_rt'] = A.apply(lambda x: (x['price_restored'] - x['price_restored40']) / x['price_restored40'], axis=1)

    A.to_csv(cat_list[i]+"_rt.csv")
#把所有的表拼起来，按照R的不同分类
#R=5


all_5day_rt=pd.DataFrame()
for i in range(0,len(cat_list)):
    rt_5day=pd.read_csv(cat_list[i]+"_rt.csv",index_col=0)
    rt_5day_1 = rt_5day.ix[:, [ '5_day_rt']]
    all_5day_rt= all_5day_rt.join(rt_5day_1, how='outer', rsuffix=cat_list[i])
all_5day_rt=all_5day_rt.rename(columns={'5_day_rt':'5_day_rtA'})
all_5day_rt.to_csv("all_5day_rt.csv")
#R=10
all_10day_rt=pd.DataFrame()
for i in range(0,len(cat_list)):
    rt_10day=pd.read_csv(cat_list[i]+"_rt.csv",index_col=0)
    rt_10day_1=rt_10day.ix[:,['10_day_rt']]
    all_10day_rt=all_10day_rt.join(rt_10day_1,how='outer',rsuffix=cat_list[i])
all_10day_rt=all_10day_rt.rename(columns={'10_day_rt':'10_day_rtA'})
all_10day_rt.to_csv("all_10day_rt.csv")

#R=15
all_15day_rt=pd.DataFrame()
for i in range(0,len(cat_list)):
    rt_15day=pd.read_csv(cat_list[i]+"_rt.csv",index_col=0)
    rt_15day_1=rt_15day.ix[:,['15_day_rt']]
    all_15day_rt=all_15day_rt.join(rt_15day_1,how='outer',rsuffix=cat_list[i])
all_15day_rt=all_15day_rt.rename(columns={'15_day_rt':'15_day_rtA'})
all_15day_rt.to_csv("all_15day_rt.csv")
#R=20
all_20day_rt=pd.DataFrame()
for i in range(0,len(cat_list)):
    rt_20day=pd.read_csv(cat_list[i]+"_rt.csv",index_col=0)
    rt_20day_1=rt_20day.ix[:,['20_day_rt']]
    all_20day_rt=all_20day_rt.join(rt_20day_1,how='outer',rsuffix=cat_list[i])
all_20day_rt=all_20day_rt.rename(columns={'20_day_rt':'20_day_rtA'})
all_20day_rt.to_csv("all_20day_rt.csv")
#R=25
all_25day_rt=pd.DataFrame()
for i in range(0,len(cat_list)):
    rt_25day=pd.read_csv(cat_list[i]+"_rt.csv",index_col=0)
    rt_25day_1=rt_25day.ix[:,['25_day_rt']]
    all_25day_rt=all_25day_rt.join(rt_25day_1,how='outer',rsuffix=cat_list[i])
all_25day_rt=all_25day_rt.rename(columns={'25_day_rt':'25_day_rtA'})
all_25day_rt.to_csv("all_25day_rt.csv")

#R=30
all_30day_rt=pd.DataFrame()
for i in range(0,len(cat_list)):
    rt_30day=pd.read_csv(cat_list[i]+"_rt.csv",index_col=0)
    rt_30day_1=rt_30day.ix[:,['30_day_rt']]
    all_30day_rt=all_30day_rt.join(rt_30day_1,how='outer',rsuffix=cat_list[i])
all_30day_rt=all_30day_rt.rename(columns={'30_day_rt':'30_day_rtA'})
all_30day_rt.to_csv("all_30day_rt.csv")

#R=35
all_35day_rt=pd.DataFrame()
for i in range(0,len(cat_list)):
    rt_35day=pd.read_csv(cat_list[i]+"_rt.csv",index_col=0)
    rt_35day_1=rt_35day.ix[:,['35_day_rt']]
    all_35day_rt=all_35day_rt.join(rt_35day_1,how='outer',rsuffix=cat_list[i])
all_35day_rt=all_35day_rt.rename(columns={'35_day_rt':'35_day_rtA'})
all_35day_rt.to_csv("all_35day_rt.csv")

#R=40
all_40day_rt=pd.DataFrame()
for i in range(0,len(cat_list)):
    rt_40day=pd.read_csv(cat_list[i]+"_rt.csv",index_col=0)
    rt_40day_1=rt_40day.ix[:,['40_day_rt']]
    all_40day_rt=all_40day_rt.join(rt_40day_1,how='outer',rsuffix=cat_list[i])
all_40day_rt=all_40day_rt.rename(columns={'40_day_rt':'40_day_rtA'})
all_40day_rt.to_csv("all_40day_rt.csv")

