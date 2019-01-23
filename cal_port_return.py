import numpy as np
import pandas as pd
import datetime
from datetime import datetime , timedelta
import matplotlib.pyplot as plt
benchmark='NH0100'
benchmark_history=pd.read_csv("NH.csv",index_col=0)
cat_list=pd.read_csv("cat_list.csv",header=None,index_col=0)
cat_list=pd.Series(cat_list.groupby(cat_list.iloc[:,0]).count().index)
startdate=pd.to_datetime('20050104')
enddate=pd.to_datetime('20170120')
#计算benchmark持有期收益
yearly_rt=(benchmark_history.ix[len(benchmark_history)-1,'close']/benchmark_history.ix[0,'close'])**(365 / 4399)
#建立函数，计算收益率
#多头组合
def calculate_long_rt(R,H):
    #读入数据
    cat_all_price=pd.read_csv("cat_all_price.csv",index_col=0)
    port_info=pd.read_csv("R"+str(R)+"_H"+str(H)+"_port_info.csv",index_col=0)
    cat_all_price=pd.DataFrame(data=cat_all_price.values,index=cat_all_price.index,columns=cat_list)
    #建立账户
    accounts_balance=pd.DataFrame(index=cat_all_price.index,columns={'balance'},data=0)
    #遍历每个日期
    for i in range(R, len(port_info) - H, H):
        # 遍历每个品种
        a = 0
        b = 0
        for j in range(0, port_info.shape[1]):
            # 把旧合约卖掉的收益率
            if (port_info.ix[i, j] == 1):
                a += cat_all_price.ix[i + H, j]
                b += cat_all_price.ix[i, j]
            if (j == port_info.shape[1] - 1):
                accounts_balance.ix[i + H, 'balance'] = (a - b) / b
    for i in range(0,len(accounts_balance)):
        if(accounts_balance.ix[i,'balance']==float(0)):
            accounts_balance.ix[i,'balance']=None
    accounts_balance = accounts_balance.dropna()
    accounts_balance['rt1'] = accounts_balance.add(1)
    holding_rt=accounts_balance.ix[:,'rt1'].cumprod().tail(1).values
    #计算平均收益率
    expected_rt=accounts_balance.ix[:,'balance'].mean()
    #计算标准差
    std_rt=accounts_balance.ix[:,'balance'].std()
    #计算年化收益率
    yearly_rt=(holding_rt)**(365/4399)-1
    #计算持仓胜率
    positive_rt_count=0
    negative_rt_count=0
    for k in range(0,len(accounts_balance)):
        if(accounts_balance.ix[k,'balance']>0):
            positive_rt_count =positive_rt_count+1
        else:
            negative_rt_count=negative_rt_count+1
    win_rate=positive_rt_count/len(accounts_balance)
    #计算风险收益比
    risk_rt=yearly_rt/((std_rt*(240/H))**0.5)
    performance= pd.DataFrame(data=[expected_rt,yearly_rt[0],risk_rt[0],win_rate])
    return accounts_balance.ix[:,'balance']

#空头组合
def calculate_short_rt(R,H):
    # 读入数据
    cat_all_price = pd.read_csv("cat_all_price.csv", index_col=0)
    port_info = pd.read_csv("R" + str(R) + "_H" + str(H) + "_port_info.csv", index_col=0)
    cat_all_price = pd.DataFrame(data=cat_all_price.values, index=cat_all_price.index, columns=cat_list)
    # 建立账户
    accounts_balance = pd.DataFrame(index=cat_all_price.index, columns={'balance'}, data=0)
    # 遍历每个日期
    for i in range(R, len(port_info) - H, H):
        # 遍历每个品种
        a = 0
        b = 0
        for j in range(0, port_info.shape[1]):
            # 把旧合约卖掉的收益率
            if (port_info.ix[i, j] == -1):
                a += cat_all_price.ix[i + H, j]
                b += cat_all_price.ix[i, j]
            if (j == port_info.shape[1] - 1):
                accounts_balance.ix[i + H, 'balance'] = (a - b) / b
    for i in range(0, len(accounts_balance)):
        if (accounts_balance.ix[i, 'balance'] == float(0)):
            accounts_balance.ix[i, 'balance'] = None
    accounts_balance = accounts_balance.dropna()
    accounts_balance['rt1'] = accounts_balance.add(1)
    holding_rt = accounts_balance.ix[:, 'rt1'].cumprod().tail(1).values
    # 计算平均收益率
    expected_rt = accounts_balance.ix[:, 'balance'].mean()
    # 计算标准差
    std_rt = accounts_balance.ix[:, 'balance'].std()
    # 计算年化收益率
    yearly_rt = (holding_rt) ** (365 / 4399) - 1
    # 计算持仓胜率
    positive_rt_count = 0
    negative_rt_count = 0
    for k in range(0, len(accounts_balance)):
        if (accounts_balance.ix[k, 'balance'] > 0):
            positive_rt_count = positive_rt_count + 1
        else:
            negative_rt_count = negative_rt_count + 1
    win_rate = positive_rt_count / len(accounts_balance)
    # 计算风险收益比
    risk_rt = yearly_rt / ((std_rt * (240 / H)) ** 0.5)
    performance = pd.DataFrame(data=[expected_rt, yearly_rt[0], risk_rt[0], win_rate])
    return accounts_balance.ix[:, 'balance']

#多空组合
def calculate_longshort_rt(R,H):
    # 读入数据
    cat_all_price = pd.read_csv("cat_all_price.csv", index_col=0)
    port_info = pd.read_csv("R" + str(R) + "_H" + str(H) + "_port_info.csv", index_col=0)
    cat_all_price = pd.DataFrame(data=cat_all_price.values, index=cat_all_price.index, columns=cat_list)
    # 建立账户
    accounts_balance = pd.DataFrame(index=cat_all_price.index, columns={'balance'}, data=0)
    # 遍历每个日期
    for i in range(R, len(port_info)-H, H):
        # 遍历每个品种
        a = 0
        b = 0
        c = 0
        d = 0
        for j in range(0, port_info.shape[1]):
            # 前一期做空的收益率
            if (port_info.ix[i, j] == 1):
                a += cat_all_price.ix[i+H, j]
                b += cat_all_price.ix[i, j]
            if(port_info.ix[i,j]==-1):
                c+=cat_all_price.ix[i+H, j]
                d+=cat_all_price.ix[i, j]
            if(j==port_info.shape[1]-1):
                accounts_balance.ix[i+H, 'balance'] = (a-b+d-c)/(b+d)
    for i in range(0, len(accounts_balance)):
        if (accounts_balance.ix[i, 'balance'] == float(0)):
            accounts_balance.ix[i, 'balance'] = None
    accounts_balance = accounts_balance.dropna()
    accounts_balance['rt1'] = accounts_balance.add(1)
    holding_rt = accounts_balance.ix[:, 'rt1'].cumprod().tail(1).values
    # 计算平均收益率
    expected_rt = accounts_balance.ix[:, 'balance'].mean()
    # 计算标准差
    std_rt = accounts_balance.ix[:, 'balance'].std()
    # 计算年化收益率
    yearly_rt = (holding_rt) ** (365 / 4399) - 1
    # 计算持仓胜率
    positive_rt_count = 0
    negative_rt_count = 0
    for k in range(0, len(accounts_balance)):
        if (accounts_balance.ix[k, 'balance'] > 0):
            positive_rt_count = positive_rt_count + 1
        else:
            negative_rt_count = negative_rt_count + 1
    win_rate = positive_rt_count / len(accounts_balance)
    # 计算风险收益比
    risk_rt = yearly_rt / ((std_rt * (240 / H)) ** 0.5)
    performance = pd.DataFrame(data=[expected_rt, yearly_rt[0], risk_rt[0], win_rate])
    return accounts_balance.ix[:, 'balance']

#计算benchmark的表现
def calculate_benchmark_rt(R,H):
    colname = "H=" + str(H)
    for i in range(R, len(benchmark_history) - H, H):
        benchmark_history.ix[i + H, colname] = (benchmark_history.ix[i + H, 'close'] - benchmark_history.ix[i, 'close']) / benchmark_history.ix[i, 'close']
    rt = benchmark_history.ix[:, colname].dropna()
    rt = rt.to_frame()
    rt['rt1'] = rt[colname].add(1)
    holding_rt = rt['rt1'].cumprod()
    return rt.ix[:,colname]

#df_long=pd.DataFrame(columns={'H=5','H=10','H=15','H=20'},index=['R=5','R=10','R=15','R=20','R=25','R=30','R=35','R=40'])
#for i in  range(1,5):
#    for j in range(1,9):
#        colname='H='+str(i*5)
#        rowname='R='+str(j*5)
#        df_long.ix[rowname,colname]=calculate_long_rt(j*5,i*5).iloc[1,0]
#df_long.to_csv("long_rt.csv")
#df_short=pd.DataFrame(columns={'H=5','H=10','H=15','H=20'},index=['R=5','R=10','R=15','R=20','R=25','R=30','R=35','R=40'])
#for i in  range(1,5):
#    for j in range(1,9):
#        colname='H='+str(i*5)
#        rowname='R='+str(j*5)
#        df_short.ix[rowname,colname]=calculate_short_rt(j*5,i*5).iloc[1,0]
#df_short.to_csv("short_rt.csv")
#df_longshort=pd.DataFrame(columns={'H=5','H=10','H=15','H=20'},index=['R=5','R=10','R=15','R=20','R=25','R=30','R=35','R=40'])
#for i in  range(1,5):
#    for j in range(1,9):
#        colname='H='+str(i*5)
#        rowname='R='+str(j*5)
#        df_longshort.ix[rowname,colname]=calculate_longshort_rt(j*5,i*5).iloc[1,0]
#df_longshort.to_csv("longshort_rt.csv")


calculate_benchmark_rt(15,10).to_csv("benchmark1.csv")
calculate_long_rt(15,10).to_csv("long1.csv")
calculate_short_rt(15,10).to_csv("short1.csv")
calculate_longshort_rt(15,10).to_csv("longshort1.csv")
















