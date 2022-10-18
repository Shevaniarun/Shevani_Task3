#!/usr/bin/env python
# coding: utf-8

# In[350]:


import numpy as np
import pandas as pd


# In[351]:


data= pd.read_csv('C:/Users/sheva/OneDrive/Desktop/input_data_sheva.csv',header=50)


# In[352]:


data.head(5)


# In[353]:


cname=data.loc[0]


# In[354]:


colname=list(cname)


# In[355]:


data.columns =colname


# In[356]:


data.head()


# In[357]:


data=data.drop(labels=0,axis=0)


# In[358]:


data.head()


# In[359]:


data.info()


# In[360]:


data['Artifact corrected heart rate']=pd.to_numeric(data['Artifact corrected heart rate'])


# In[361]:


data.info()


# In[362]:


# data['Artifact corrected heart rate']=data['Artifact corrected heart rate'].astype(int)


# In[363]:


# data.info()


# In[364]:


data['%VO2max']=pd.to_numeric(data['%VO2max'])


# In[365]:


data.info()


# In[366]:


data['%VO2max']=data['%VO2max'].astype(int)


# In[367]:


data.info()


# In[368]:


data.head()


# In[369]:


data.info()


# In[370]:


v=data['%VO2max']


# In[371]:


vo=list(v)
vo2=[]


# In[372]:


# for i in vo:
#     if i >= 0 and i<=20:
#         vo2.append()
#     elif i>=21 and i<=30:
#         vo2.append(i)
#     elif i>=31 and i<=40:
#         vo2.append(i)
#     elif i>40:
#         vo2.append(i)
# print(vo2)


# In[373]:


for i in vo:
    if 0<= i <=20:
        vo2.append('green')
    elif 21<= i <=30:
        vo2.append('blue')
    elif 31<= i <=40:
        vo2.append('red')
    elif i>40:
        vo2.append('black')


# In[374]:


data['%VO2max']=np.array(vo2)


# In[375]:


data.head()


# In[376]:


# 2nd Question


# In[377]:


import matplotlib.pyplot as plt


# In[378]:


data['%VO2max'].value_counts()


# In[379]:


count_vo=data['%VO2max'].value_counts()


# In[380]:


s = [[6042,'green'],[3841,'black'],[1073,'blue'],[620,'red']]


# In[381]:


count_vo2 = pd.DataFrame(s, columns=['vals', 'col'])


# In[382]:


count_vo2


# In[383]:


plt.plot(count_vo2['col'], count_vo2['vals'], color='red')


# In[384]:


plt.pie(count_vo2["vals"], labels = count_vo2["col"])


# In[389]:


#Line graph


# In[ ]:


data['%VO2max']


# In[ ]:


data.info()


# In[388]:


Vo2max=data['%VO2max'].to_list()
arti_hr=data['Artifact corrected heart rate'].to_list()


# In[404]:


import matplotlib.pyplot as plt
for i in range(len(Vo2max)):
    if Vo2max[i] >= 0 and Vo2max[i] <= 20:
        plt.plot(i,arti_hr[i],color='green',marker='.')
#         plt.hold(True)
#         plt.show()
    elif Vo2max[i] >= 21 and Vo2max[i] <=30:
        plt.plot(i,arti_hr[i],color='red',marker='.')
    elif Vo2max[i] >= 31 and Vo2max[i] <=40:
        plt.plot(i,arti_hr[i],color='blue',marker='.')
    elif Vo2max[i] > 40:
        plt.plot(i,arti_hr[i],color='black',marker='.')            
plt.xlabel('Vo2max')
plt.ylabel('heart rate')
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
for i in range(len(arti_hr)):
    if arti_hr[i] >= 80 and arti_hr[i] <= 120:
        plt.plot(i,arti_hr[i],color='red',marker='.')
#         plt.hold(True)
#         plt.show()

    elif arti_hr[i] >= 121 and arti_hr[i] <=200:
        plt.plot(i,arti_hr[i],color='blue',marker='.')
#         plt.hold(True)
plt.show()


# In[ ]:


# G=[]
# R=[]
# B=[]
# Bl=[]
# print(len(Vo2max))
# for i in range(len(Vo2max)):
# #     print (i, end = " ")
# #     print (Vo2max[i])
#     if Vo2max[i] >=0 and Vo2max[i]<=20:
#         G.append(i)
#     elif Vo2max[i] >=21 and Vo2max[i]<=30:
#         R.append(i)
#     elif Vo2max[i] >=31 and Vo2max[i]<=40:
#         B.append(i)
#     else:
#         Bl.append(i) 


# In[ ]:


# G=[]
# R=[]
# B=[]
# Bl=[]
# print(len(Vo2max))
# for i in range(len(Vo2max)):
# #     print (i, end = " ")
# #     print (Vo2max[i])
#     if Vo2max[i] == "green":
#         G.append(i)
#     elif Vo2max[i] == "red":
#         R.append(i)
#     elif Vo2max[i] == "blue":
#         B.append(i)
#     else:
#         Bl.append(i)        
# print(len(G))
# print(len(arti_hr))
# print(G)


# In[ ]:


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.collections import LineCollection
# from matplotlib.colors import ListedColormap, BoundaryNorm

# x = Vo2max
# y = arti_hr
# dydx = np.cos(1 * (x[:-1] + x[1:]))  # first derivative

# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
# points = np.array([x, y]).T.reshape(-1, 1, 2)
# segments = np.concatenate([points[:-1], points[1:]], axis=1)

# fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
# norm = plt.Normalize(x,y)
# lc = LineCollection(segments, cmap='viridis')
# Set the values used for colormapping
# lc.set_array(dydx)
# lc.set_linewidth(2)
# line = axs[0].add_collection(lc)
# fig.colorbar(line, ax=axs[0])

# Use a boundary norm instead
# cmap = ListedColormap(['r', 'g', 'b'])
# norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
# lc = LineCollection(segments, cmap=cmap)
# lc.set_array(dydx)
# lc.set_linewidth(2)
# line = axs[1].add_collection(lc)
# fig.colorbar(line, ax=axs[1])

# axs[0].set_xlim(x,y)
# axs[0].set_ylim(-1.1, 1.1)
# plt.show()


# In[ ]:


# import matplotlib.style as style
# style.use('fivethirtyeight')

# plt.figure(figsize=(20,12))

# grid = plt.GridSpec(1,1, wspace = .25, hspace = .25)

# ax1 = plt.subplot(grid[0,0])

# for ax in [ax1]:
#     ax.set_yticks([1.2,1.4,1.6])
#     ax.set_ylim(1,2)
#     ax.set_xlim(Vo2max)
#     ax.set_xticks(data.arti_hr)
#     ax.set_xticklabels(['2001','2009','2017','2021'])

# ax1.plot(G, color='green')
# ax1.plot(R, color='red')    
# ax1.plot(B, color='skyblue')   

# plt.axvline(dt.datetime(2009,1,1), alpha=0.2, linewidth=4, color='grey',linestyle='dotted')
# plt.axvline(dt.datetime(2017,1,1), alpha=0.2, linewidth=4, color='grey',linestyle='dotted')
# plt.axvline(dt.datetime(2021,1,1), alpha=0.2, linewidth=4, color='grey',linestyle='dotted') 
# plt.axvline(dt.datetime(2001,1,1), alpha=0.2, linewidth=4, color='grey',linestyle='dotted')
#plt.axhline(1.22, linewidth=2, color='black',linestyle='dashed', xmin=0.01, xmax=0.99)

# ax.text(dt.datetime(2004,3,1),1.55,s="BUSH",size=15, color= 'lightgreen', weight='bold')
# ax.text(dt.datetime(2012,1,1),1.55,s="OBAMA",size=15, color= 'lightsalmon', weight='bold')
# ax.text(dt.datetime(2018,5,1),1.55,s="TRUMP",size=15, color= 'skyblue', weight='bold')
# ax.text(dt.datetime(2000,2,1),1.7,s="EUR-USD rate averaged 1.22 under the last 3 US presidents", size=20, weight='bold')
# ax.text(dt.datetime(2000,2,1),1.65,s="Some subtitle", size=20)
# ax.text(dt.datetime(2000,1,1),0.65,s="DATAQUEST" + ' '*115+ 'Léon Hekkert',backgroundcolor='#4d4d4d', color='#f0f0f0', size=16)
# ax.grid(axis='x')

# plt.show()


# In[ ]:


# from itertools import islice
 
# # Input list initialization
# Input = G
 
# # list of length in which we have to split
# length_to_split = [81,1398]
 
# # Using islice
# Inputt = iter(Input)
# Output = [list(islice(Inputt, elem))
#         for elem in length_to_split]
 
# # Printing Output

# print("Split length list: ", length_to_split)
# print("List after splitting", Output)


# In[385]:


#3rd Question


# In[386]:


cum_time=data['Cumulative time'].to_list()
arti_hr=data['Artifact corrected heart rate'].to_list()


# In[387]:


plt.plot(cum_time,arti_hr,linewidth=0.5)
plt.title('Heart rate Signal')
plt.xlabel('time')
plt.ylabel('heart rate')
plt.figure(figsize=(1,1))
plt.show()


# In[ ]:


# import numpy as np
# import matplotlib.pyplot as plt
# # start=11575
# # stop=11576
# def uniqueish_color():
#     return plt.cm.gist_ncar(G())
# xy = G,arti_hr
# fig, ax = plt.subplots()
# for start, stop in zip(xy[:-1], xy[1:]):
#     x, y = zip(start, stop)
    
#     ax.plot(x, y, color=uniqueish_color())
# plt.show()


# In[ ]:


# plt.plot(Vo2max,arti_hr,linewidth=0.5)
# plt.title('Heart rate Signal')
# plt.xlabel('%VO2max')
# plt.ylabel('heart rate')
# fig, ax = plt.subplots()
# for start, stop in (G[:-1], G[1:]):
#     x,y = (start, stop)
#     ax.plot(x,y, color='green')
# plt.show()
# # plt.figure(figsize=(1,1))
# # plt.show()


# In[ ]:


off=0
rms_noise=6
noise=np.random.normal(loc=off,scale=rms_noise,size=11576)
measured=np.std(noise)
print(measured)


# In[ ]:


hrnoise=noise.tolist()


# In[ ]:


plt.plot(cum_time,hrnoise,linewidth=0.5)
plt.title('Noise Signal')
plt.xlabel('time')
plt.ylabel('Noise')
plt.figure(figsize=(1,1))
plt.show()


# In[ ]:


hr_arr=np.array(arti_hr)
no_arr=np.array(hrnoise)
print(hr_arr)
print(no_arr)


# In[ ]:


sig=hr_arr + no_arr
print(sig)


# In[ ]:


plt.plot(cum_time,sig,linewidth=0.5)
plt.title('Noise added Signal')
plt.xlabel('time')
plt.ylabel('HR')
plt.figure(figsize=(1,1))
plt.show()


# In[ ]:


plt.title('Noise added Signal')
plt.xlabel('time')
plt.ylabel('HR')
plt.plot(cum_time, sig, label = "Noise added Signal",linewidth=0.4)
plt.plot(cum_time, arti_hr, label = "filtered Signal",linewidth=0.9)
plt.legend()
plt.show()


# In[ ]:


import numpy as np


# In[ ]:


def signaltonoise(Arr, axis=0, ddof=0):
    Arr = np.asanyarray(Arr)
    me = Arr.mean(axis)
    sd = Arr.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, me/sd)
Arr=[hr_arr,no_arr]
print(signaltonoise(Arr,axis=0,ddof=0))

