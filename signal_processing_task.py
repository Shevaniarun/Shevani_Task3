import numpy as np
import pandas as pd
data= pd.read_csv('C:/Users/sheva/OneDrive/Desktop/input_data_sheva.csv',header=50)
data.head(5)
cname=data.loc[0]
colname=list(cname)
data.columns =colname
data.head()
data=data.drop(labels=0,axis=0)
data.head()
data.info()
data['Artifact corrected heart rate']=pd.to_numeric(data['Artifact corrected heart rate'])
data.info()
data['%VO2max']=pd.to_numeric(data['%VO2max'])
data.info()
data['%VO2max']=data['%VO2max'].astype(int)
data.info()
v=data['%VO2max']
vo=list(v)
vo2=[]
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
for i in vo:
    if 0<= i <=20:
        vo2.append('green')
    elif 21<= i <=30:
        vo2.append('blue')
    elif 31<= i <=40:
        vo2.append('red')
    elif i>40:
        vo2.append('black')
data['%VO2max']=np.array(vo2)
data.head()
# 2nd Question
import matplotlib.pyplot as plt
data['%VO2max'].value_counts()
s = [[6042,'green'],[3841,'black'],[1073,'blue'],[620,'red']]
count_vo2 = pd.DataFrame(s, columns=['vals', 'col'])
# plt.plot(count_vo2['col'], count_vo2['vals'], color='red')
plt.pie(count_vo2["vals"], labels = count_vo2["col"])
#Line graph
data['%VO2max']
data.info()
Vo2max=data['%VO2max'].to_list()
arti_hr=data['Artifact corrected heart rate'].to_list()
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
cum_time=data['Cumulative time'].to_list()
arti_hr=data['Artifact corrected heart rate'].to_list()
plt.plot(cum_time,arti_hr,linewidth=0.5)
plt.title('Heart rate Signal')
plt.xlabel('time')
plt.ylabel('heart rate')
plt.figure(figsize=(1,1))
plt.show()
off=0
rms_noise=6
noise=np.random.normal(loc=off,scale=rms_noise,size=11576)
measured=np.std(noise)
print(measured)
hrnoise=noise.tolist()
plt.plot(cum_time,hrnoise,linewidth=0.5)
plt.title('Noise Signal')
plt.xlabel('time')
plt.ylabel('Noise')
plt.figure(figsize=(1,1))
plt.show()
hr_arr=np.array(arti_hr)
no_arr=np.array(hrnoise)
print(hr_arr)
print(no_arr)
sig=hr_arr + no_arr
print(sig)
plt.plot(cum_time,sig,linewidth=0.5)
plt.title('Noise added Signal')
plt.xlabel('time')
plt.ylabel('HR')
plt.figure(figsize=(1,1))
plt.show()
plt.title('Noise added Signal')
plt.xlabel('time')
plt.ylabel('HR')
plt.plot(cum_time, sig, label = "Noise added Signal",linewidth=0.4)
plt.plot(cum_time, arti_hr, label = "filtered Signal",linewidth=0.9)
plt.legend()
plt.show()
def signaltonoise(Arr, axis=0, ddof=0):
    Arr = np.asanyarray(Arr)
    me = Arr.mean(axis)
    sd = Arr.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, me/sd)
Arr=[hr_arr,no_arr]
print(signaltonoise(Arr,axis=0,ddof=0))



