#!/usr/bin/env python
# coding: utf-8

# In[49]:


#!/usr/bin/env python
# coding: utf-8

# In[11]:

'''
Action3: 对汽车质量数据进行统计
数据集：car_complain.csv，600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数，哪个品牌的平均车型投诉最多
'''
import pandas as pd

result = pd.read_csv('D:\Data Engine\Python\car_complain.csv')

#对 Problem 进行One-Hot编码,分类变量作为二进制向量
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))

df= result.groupby('brand')['id'].agg(['count'])
print("品牌投诉总数\n",df.sort_values('count', ascending=False))


df= result.groupby('car_model')['id'].agg(['count'])
print("车型投诉总数\n",df.sort_values('count', ascending=False))

df= result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean()
print("平均车型投诉最多的品牌",df.sort_values('count', ascending=False))


# In[25]:


import pandas as pd

data=pd.DataFrame({'a':['x','y','x'],'b':[4,2,3]})
df= data.groupby('a')
print (df)
#data.a.str.get_dummies((','))


# In[29]:



df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                  'Max Speed': [380., 370., 24., 26.]})

df.groupby(['Animal'])


# In[ ]:




