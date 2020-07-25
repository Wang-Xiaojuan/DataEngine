#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
from efficient_apriori import apriori

#heard=none 不将第一行作为head
dataset = pd.read_csv('D:\Data Engine\Python\Lesson 4\Market_Basket_Optimisation.csv',header=None)
print(dataset.shape)

#将数据放到transactions中
transactions = []
for i in range(0,dataset.shape[0]):
    temp=[]
    for j in range(0,20):
        if str(dataset.values[i,j]) != 'nan':
            temp.append(str(dataset.values[i,j]))
    transactions.append(temp)
    
#挖掘频繁项集与关联规则
itemset, rules = apriori(transactions, min_support=0.05, min_confidence=0.2)
print("频繁项集：", itemset)
print("关联规则：", rules)    


# In[ ]:




