import numpy as np
import pandas as pd
import datetime
from datetime import datetime , timedelta

startdate=pd.to_datetime('20050104')
enddate=pd.to_datetime('20170120')

cat_list=pd.read_csv("cat_list.csv",header=None,index_col=0)
cat_list=pd.Series(cat_list.groupby(cat_list.iloc[:,0]).count().index)
def ranking(R,H):
    #读入数据
    if(R==5):
        all_rt=pd.read_csv("all_5day_rt.csv",index_col=0)
    elif(R==10):
        all_rt=pd.read_csv("all_10day_rt.csv",index_col=0)
    elif(R==15):
        all_rt=pd.read_csv("all_15day_rt.csv",index_col=0)
    elif(R==20):
        all_rt = pd.read_csv("all_20day_rt.csv",index_col=0)
    elif(R==25):
        all_rt = pd.read_csv("all_25day_rt.csv",index_col=0)
    elif(R==30):
        all_rt = pd.read_csv("all_30day_rt.csv",index_col=0)
    elif(R==35):
        all_rt = pd.read_csv("all_35day_rt.csv",index_col=0)
    elif(R==40):
        all_rt=pd.read_csv("all_40day_rt.csv",index_col=0)
    #遍历每个回测期,生成新df
    port_info = pd.DataFrame(index=all_rt.index, columns=cat_list, data=0)
    for i in range(R,len(all_rt),H):
        # 每个时间点的收益率去空，排序
        size1 = all_rt.iloc[i, :].dropna().size
        tail1 = round(size1 * 0.2)
        # 空头组合
        short_port = all_rt.iloc[i, :].dropna().sort_values(ascending=True).head(tail1).index.tolist()
        # 多头组合
        long_port = all_rt.iloc[i, :].dropna().sort_values(ascending=False).head(tail1).index.tolist()
        # list重命名
        for j in range(0, len(short_port)):
            short_port[j] = short_port[j].strip(str(R)+"_day_rt")
            long_port[j] = long_port[j].strip(str(R)+"_day_rt")
        # 放在同一个df里面
        # 做空的组合记为-1
        for k in range(0, len(short_port)):
            port_info.ix[i, short_port[k]] = -1
        # 做多的组合记为1
        for k in range(0, len(long_port)):
            port_info.ix[i, long_port[k]] = 1
    port_info.to_csv("R"+str(R)+"_H"+str(H)+"_port_info.csv")
ranking(5,5)
ranking(5,10)
ranking(5,15)
ranking(5,20)
ranking(10,5)
ranking(10,10)
ranking(10,15)
ranking(10,20)
ranking(15,5)
ranking(15,10)
ranking(15,15)
ranking(15,20)
ranking(20,5)
ranking(20,10)
ranking(20,15)
ranking(20,20)
ranking(25,5)
ranking(25,10)
ranking(25,15)
ranking(25,20)
ranking(30,5)
ranking(30,10)
ranking(30,15)
ranking(30,20)
ranking(35,5)
ranking(35,10)
ranking(35,15)
ranking(35,20)
ranking(40,5)
ranking(40,10)
ranking(40,15)
ranking(40,20)








