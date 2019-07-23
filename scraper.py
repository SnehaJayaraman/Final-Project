#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
from bs4 import BeautifulSoup 
URL= "URL_files.txt"
with open(URL, "r") as f:
  url_pages = f.read()
pages = url_pages.split("\n") 
records = []


# In[2]:


for single_page in pages:
    #print(single_page)
    page = requests.get(single_page)
    soup = BeautifulSoup(page.text, 'html.parser')
    results = soup.find_all('td')
    
    for k in range(0,len(results),24):
        Date=results[k].text
        Location=results[k+1].text
        MinTemp=results[k+2].text
        MaxTemp=results[k+3].text
        Rainfall=results[k+4].text
        Evapouration=results[k+5].text
        Sunshine=results[k+6].text
        WindGustDir=results[k+7].text
        WindGustSpeed=results[k+8].text
        WindDir9am=results[k+9].text
        WindDir3pm=results[k+10].text
        WindSpeed9am=results[k+11].text
        WindSpeed3pm=results[k+12].text
        Humidity9am=results[k+13].text
        Humidity3pm=results[k+14].text
        Pressure9am=results[k+15].text
        Pressure3pm=results[k+16].text
        Cloud9am=results[k+17].text
        Cloud3pm=results[k+18].text
        Temp9am=results[k+19].text
        Temp3pm=results[k+20].text
        RainToday=results[k+21].text
        RISK_MM=results[k+22].text
        RainTomorrow=results[k+23].text
        records.append((Date,Location,MinTemp,MaxTemp,Rainfall,Evapouration,Sunshine,WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,WindSpeed9am,
                   WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,RainToday,RISK_MM,RainTomorrow))


# In[3]:


import pandas as pd
df = pd.DataFrame(records, columns=['Date','Location','MinTemp','MaxTemp','Rainfall','Evapouration','Sunshine','WindGustDir','WindGustSpeed','WindDir9am','WindDir3pm','WindSpeed9am',
                   'WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm','RainToday','RISK_MM','RainTomorrow'])


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.to_csv('dataset.csv', index=False, encoding='utf-8')


# In[ ]:




