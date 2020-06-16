#!/usr/bin/env python
# coding: utf-8

# In[22]:


'''
Action2: 统计全班的成绩
统计班里5名同学在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
'''

import pandas as pd
from pandas import Series, DataFrame
data = {'Chinese': [68, 95, 98, 90,80],'Math': [65, 76, 86, 88, 90],'English': [30, 98, 88, 77, 90]}
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])
print (df2)

df3 = DataFrame([df2.mean(),df2.min(),df2.max(),df2.std(),df2.var()],index=['mean','min','max','std','var'],
                columns=['Chinese', 'Math', 'English'])
print(df3)

df2['Sum'] = df2['Chinese'] + df2['Math'] + df2['English']

df2 = df2.sort_values(by='Sum',ascending=False)
print(df2)


# In[ ]:





# In[ ]:




