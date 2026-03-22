import time
import random
import matplotlib.pyplot as plt
t1,t2=0,0
t1=time.time()
y_inbuilt=[]
y_myfunc=[]
x=[]
n=10000
for i in range(n):
  x.append(i)

def mysort(l):
  for i in range(len(l)):
    for j in range(i,len(l)):
      if l[i] > l[j]:
        l[i],l[j]=l[j],l[i]
  return l


def median_inbuilt(l):
  l.sort()
  if len(l) % 2 == 1:
    return l[int((len(l) - 1) / 2)]
  else:
    return (l[int(len(l) / 2)] + l[int(len(l) / 2) - 1]) / 2

def median_myfunc(l):
  l=mysort(l)
  if len(l) % 2 == 1:
    return l[int((len(l) - 1) / 2)]
  else:
    return (l[int(len(l) / 2)] + l[int(len(l) / 2) - 1]) / 2
 
for i in range(n):
  lis=[random.randint(1, 1000) for _ in range(1000)]
  t1=time.time()
  median_inbuilt(lis)
  t2=time.time()
  y_inbuilt.append(t2-t1)
for i in range(n):
  lis=[random.randint(1, 1000) for _ in range(1000)]
  t1=time.time()
  median_myfunc(lis)
  t2=time.time()
  y_myfunc.append(t2-t1)
plt.plot(x,y_inbuilt,label='inbuilt')
plt.plot(x,y_myfunc,label='myfunc')
plt.legend()
plt.show()
