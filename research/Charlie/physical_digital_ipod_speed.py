#!/usr/bin/env python
# coding: utf-8

# In[100]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[101]:


# Store filepath in a variable
tran = "C:/Users/charl/OneDrive/Desktop/team_project/revenue_by_format.csv"


# In[102]:


# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
tran_df = pd.read_csv(tran)


# In[103]:


tran_df.head()


# In[104]:


tran_df['Physical'] = tran_df['CD Revenue'] + tran_df['CD Single Revenue'] + tran_df['Cassette Revenue'] + tran_df['Cassette Single Revenue'] + tran_df['DVD Audio Revenue']


# In[105]:


tran_df['Digital'] = tran_df['On-Demand Streaming (Ad-Supported) Revenue'] + tran_df['Other Digital Revenue'] + tran_df['Paid Subscription Revenue']


# In[106]:


tran_df['PhoneSpeed'] = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','2679','3042','3453','3920','4449','5733','6507']


# In[129]:


tran_df['Ipod'] = ['','','','','','','','','','','','','','','','','','3941.0','5163.0','5483.0','5413.0','5031.0','4262.0','3517.0','2638.0', '1438.0','','','','','','','','']


# In[130]:


combine_df = tran_df['sum'] = tran_df['CD Revenue'] + tran_df['CD Single Revenue'] + tran_df['Cassette Revenue'] + tran_df['Cassette Single Revenue'] + tran_df['DVD Audio Revenue']


# In[131]:


tran_df.dtypes


# In[132]:


tran_df["Physical"] = pd.to_numeric(tran_df["Physical"])
tran_df["Digital"] = pd.to_numeric(tran_df["Digital"])


# In[ ]:





# In[133]:


tran_df["Ipod"] = pd.to_numeric(tran_df["Ipod"])
tran_df["PhoneSpeed"] = pd.to_numeric(tran_df["PhoneSpeed"])


# In[134]:


print(tran_df)


# In[135]:


tran_df.plot(x="Year", y=["Digital", "Physical","Ipod","PhoneSpeed"])


# In[128]:


print(tran_df)


# In[99]:


tran_df.dtypes


# In[83]:


tran_df.plot(x="Year", y=["Digital", "Physical"])


# In[ ]:




