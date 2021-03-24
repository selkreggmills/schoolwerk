#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


filename = 'table_i702t60.csv'
df = pd.read_csv("~/Desktop/table_i702t60.csv")


# In[5]:


df.info()


# In[6]:


month_number = df.loc[:, 'month'].values
interest_paid = df.loc[:, 'interest_paid'].values
principal_paid = df.loc[:, 'principal_paid'].values


# In[7]:


plt.plot(month_number, interest_paid)


# In[9]:


plt.plot(month_number, interest_paid)
plt.plot(month_number, principal_paid)


# In[13]:


plt.style.use('fivethirtyeight')
plt.plot(month_number, interest_paid)
plt.plot(month_number, principal_paid)


# In[15]:


plt.plot(month_number, interest_paid, c = 'k', marker = '.', markersize = 10)
plt.plot(month_number, principal_paid, c = 'b', marker = '.', markersize = 10)


# In[29]:


plt.plot(month_number, interest_paid, c = 'k', marker = '.', markersize = 10)
plt.plot(month_number, principal_paid, c = 'b', marker = '.', markersize = 10)
plt.xlim(left = 0, right = 65)
plt.ylim(bottom = 0, top = 700)
plt.xlabel('Month', fontsize = 20)
plt.ylabel('Dollars', fontsize = 20)
plt.title('Interest and Principal Paid Each Month', fontsize = 20)


# In[34]:


plt.plot(month_number, interest_paid, c = 'k',label = "Interest")
plt.plot(month_number, principal_paid, c = 'b', label = "Principal")
plt.xlabel('Month', fontsize = 20)
plt.ylabel('Dollars', fontsize = 20)
plt.title('Interest and Principal Paid Each Month', fontsize = 20)
plt.legend(loc = (1.02,0))


# In[39]:


confusion = np.array([[37,0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 39, 0, 0, 0, 0, 1, 0, 2, 1],
                     [0, 0, 41, 3, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 44, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 37, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 46, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 51, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 46, 0, 0],
                     [0, 3, 1, 0, 0, 0, 0, 0, 44, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0, 2, 44]])
plt.figure(figsize =(6,6))
sns.heatmap(confusion,
           annot = True,
           cmap = 'Blues');
plt.xlabel('Actual label');
plt.ylabel('Predicted label');


# In[49]:


df = pd.read_csv("~/Desktop/kingCountyHouseData.csv")
df['price'].hist(bins = 30)


# In[51]:


price_filter = df.loc[:, 'price']<=3000000
df.loc[price_filter,'price'].hist(bins = 30,
                                 edgecolor = 'black')


# In[ ]:




