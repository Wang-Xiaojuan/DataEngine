#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from fbprophet import Prophet

#数据加载
train = pd.read_csv('D:\Data Engine\Python\Lesson 6/train.csv')

#转化为pandas的日期格式
train['Datetime'] = pd.to_datetime(train.Datetime, format='%d-%m-%Y %H:%M')

#将Datetime作为train的索引
train.index = train.Datetime

#去掉ID, Datetime字段
train.drop(['ID','Datetime'],axis=1,inplace=True)

#按照天进行采样
daily_train = train.resample('D').sum()
daily_train['ds'] = daily_train.index
daily_train['y'] = daily_train.Count
daily_train.drop(['Count'],axis=1,inplace=True)

#拟合Prophet函数模型
m = Prophet(yearly_seasonality=True,seasonality_prior_scale=0.1)
m.fit(daily_train)

#预测未来7个月，213天
future = m.make_future_dataframe(periods=213)
forecast = m.predict(future)
print(forecast)

m.plot(forecast)
m.plot_components(forecast)


# In[ ]:




