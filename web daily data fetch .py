#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import datetime
import requests


# In[8]:


todays_date = datetime.datetime.now()
yesterday_date = todays_date - datetime.timedelta(days = 1)
yesterday_date = datetime.datetime.strftime(yesterday_date,'%d%m%Y')
url = "https://www.nseindia.com/archives/equities/mto/MTO_"+yesterday_date+".DAT"


# In[9]:


print(url)


# In[11]:


#df = pd.read_csv(url)
#print(df.info())
f = requests.get(url)
text = f.text
print(text)


# In[ ]:




