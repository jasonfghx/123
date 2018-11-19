#!/usr/bin/env python
# coding: utf-8

# In[40]:


import os
import pandas as pd
import numpy  as np
#載入需要之套件


# In[41]:


a=os.listdir("Z:\\智慧海運與船舶能源管理之數據分析\\船舶大數據資料\\團明輪\\VDR")
a=a[0:693]#扣除"temp_file_final(SI檔案檢查).csv"這個檔案名


# In[116]:


#暫時不執行 a#檢查內容中，多一個temp_file_final(SI檔案檢查).csv，需要扣掉


# In[58]:


temp=pd.DataFrame()
temp["20180725"]=np.nan
temp["20180726"]=np.nan
temp["20180727"]=np.nan
#以上三欄檔名特別故用手動輸入


# In[47]:


a3=pd.DataFrame(a)#將a存成a3
k=0#
j1=np.zeros(21)
for index in range(0,693):
    
    if a3.iloc[index,0].find("2018-")==5:
        j1[k]=index
        k=k+1


# In[117]:


#暫時不執行 a_new=np.delete(a,j1) ;a_new#刪除類似SI00-2018-07-25.txt 這樣的格式


# In[60]:


j1=np.zeros(85).astype(str)#產生一個含有85個元素的空list

for i in range(0,85):
    te=a_new[i].split(".")[0].split("-")[1]
    j1[i]=str(te)
#將其中的日期字串取出來作為欄位    
for i in range(0,85):
    temp[j1[i]]=None
#temp唯一新的dataframe,將得到的新日期放上去作為欄名


# In[70]:


temp.loc[0]=np.nan
temp.loc[1]=np.nan
temp.loc[2]=np.nan
temp.loc[3]=np.nan
temp.loc[4]=np.nan
temp.loc[5]=np.nan
temp.loc[6]=np.nan
temp.loc[7]=np.nan
#產生空的列，共七個


# In[88]:


temp.iloc[0,0]=a[0]
temp.iloc[0,1]=a[1]
temp.iloc[0,2]=a[2]
temp.iloc[1,0]=a[88]
temp.iloc[1,1]=a[89]
temp.iloc[1,2]=a[90]
temp.iloc[2,0]=a[177]
temp.iloc[2,1]=a[178]
temp.iloc[2,2]=a[179]
temp.iloc[3,0]=a[266]
temp.iloc[3,1]=a[267]
temp.iloc[3,2]=a[268]
temp.iloc[4,1]=a[355]
temp.iloc[4,2]=a[356]
temp.iloc[5,0]=a[441];temp.iloc[5,1]=a[442];temp.iloc[5,2]=a[443]
temp.iloc[6,1]=a[526]
temp.iloc[7,0]=a[604];temp.iloc[7,1]=a[605];temp.iloc[7,2]=a[606]


# In[118]:


#暫時不執行 temp


# In[108]:


columns=list( temp.columns   )#將temp欄名存在columns
columns_t=columns[3:88]#我們選取其中20180728~
for i in columns_t:
    print(i)#檢視欄名是否為我們所需的，若不是則更改[3:88]內的數值，此處不執行3~4行的程式


# In[106]:


temp=temp.drop([4,5,6,7],axis=1)#若是欄位有多打，可以利用該函式做刪除


# In[110]:


temp_file=temp


# In[111]:


for j in columns_t:
    for i in range(0,8):
        k=0
        ind_te=np.zeros(8)
        for ii in range(0,693):
            if a[ii][5:13]==j:
                ind_te[k]=int(ii);
                k=k+1
            
        if(int(ind_te[i]!=0)):
            print(a[int(ind_te[i])  ])
            if a[int(ind_te[i])][2:4]=="00":
                temp_file[j][0]=a[int(ind_te[i])]
            elif a[int(ind_te[i])][2:4]=="01":
                temp_file[j][1]=a[int(ind_te[i])]
            elif a[int(ind_te[i])][2:4]=="02":
                temp_file[j][2]=a[int(ind_te[i])]
            elif a[int(ind_te[i])][2:4]=="03":
                temp_file[j][3]=a[int(ind_te[i])]
            elif a[int(ind_te[i])][2:4]=="04":
                temp_file[j][4]=a[int(ind_te[i])]
            elif a[int(ind_te[i])][2:4]=="05":
                temp_file[j][5]=a[int(ind_te[i])]
            elif a[int(ind_te[i])][2:4]=="06":
                temp_file[j][6]=a[int(ind_te[i])]
            elif a[int(ind_te[i])][2:4]=="07":
                temp_file[j][7]=a[int(ind_te[i])]


# In[ ]:




