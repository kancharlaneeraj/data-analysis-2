#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
data=pd.read_csv("E:\cleaned_all_phones.csv")
datac=data
datac
datac.head()


# In[12]:


datac.info()


# In[25]:


#How many unique  mobile brands are there in the data provided
len(datac["brand"].unique())


# In[ ]:


#By using unique() metgod we get to know there are 13 types of brands are there in our dataset 


# In[27]:


#What is the average ram size of all the collected data
datac["ram(GB)"].mean()


# In[ ]:


#By using mean method we get the average of ram column i.e 6.6838624338624335


# In[28]:


#Which phone is having the maximum and minimum battery capacity
datac["battery"].max()


# In[31]:


datac.loc[datac["battery"]==7250]


# In[33]:


datac["battery"].min()


# In[34]:


datac.loc[datac["battery"]==1821]


# In[ ]:


#v6 of honor brand is having maximum battery i.e 7250 and iphone 8 and iphone SE(2020) are having least battery i.e 1821 


# In[36]:


#What is the maximum battery capacity provided by Huawei Company
g=datac.groupby("brand")
g.agg({'battery':[min,max],"ram(GB)":[min,max]})


# In[ ]:


#7000 is the maximum battery provided by Huawei company


# In[41]:


#Which Phone brand is providing the highest and lowest ram
datac["ram(GB)"].max()
datac.loc[datac['ram(GB)']==24]


# In[44]:


datac["ram(GB)"].min()
datac.loc[datac['ram(GB)']==1]


# In[ ]:


#Redmi k60 ultra,Ace 2 pro,Gt5 240 are having the maximum ram and y3(2017),z4,Galaxy z2(2017) etc are having the minimun ram


# In[48]:


#How many phones has android 7.0 as there operating system
len(datac.loc[datac["os"]=="Android 7.0"])


# In[ ]:


#33 phones are having os android 7.0


# In[49]:


#Which phine is the oldest
datac["announcement_date"].min()


# In[56]:


datac.loc[datac['announcement_date']=='2016-09-01']


# In[ ]:


#Y6II compact is the oldest phone


# In[64]:


#hich brand produced maximum number of phone in the given data
a=datac.groupby("brand")
a["brand"].count()


# In[ ]:


#xiaomi has the highest no of phones


# In[ ]:


#Give the count of phones supporting


# In[65]:


#4k video
datac['video_4K'].value_counts()


# In[66]:


#8k video
datac['video_8K'].value_counts()


# In[69]:


#2k video
datac['video_1080p'].value_counts()


# In[ ]:


# There are 801 phones having 4k video,86 phones having 8k videos,1503 phones have 2k video


# In[70]:


#10. How many phones supports Li-Po and Li-ion Battery
a=datac.groupby("battery_type")
a["battery_type"].count()


# In[ ]:


#270 phones support Li-Ion,1242 supports Li-Po


# In[101]:


# How many sony phones supports 720x1280 resolution
b=(datac["resolution"]=="720x1280")&(datac["brand"]=='Sony')
datac[b]["phone_name"].count()


# In[ ]:


# There are 5 phones from sony that supports 720x1280 resolution


# In[ ]:





# In[109]:


#12. Print a pivot table for finding the average weights ,total weights,based on brand and battery type
a=pd.pivot_table(datac,index='brand',columns='battery_type',values="weight(g)",margins=True)
a


# In[ ]:


#above shown is the pivot table showinh the average and all weights for combination of battery type and brand

