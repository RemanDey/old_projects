import random
import time
import matplotlib.pyplot as plt
entities=[]

def generate_entities(n):
    entities=[]
    for i in range(n):
        entities.append([random.randint(0,1000),random.randint(0,1000)])
    return entities


def distance(e1,e2):
     return ((e1[0]-e2[0])**2+(e1[1]-e2[1])**2)**0.5
def closest_pair(entities):
    min_dist=200000000.00
    pair=None
    for i in range(len(entities)):
        for j in range(i+1,len(entities)):
            dist=distance(entities[i],entities[j])
            if dist<min_dist:
                min_dist=dist
                pair=(entities[i],entities[j])
    return pair,min_dist

x=[]
a=100
while a<=1000:
    x.append(a)
    a+=25
    
y_1=[]
for i in x:
    entities=generate_entities(i)
    start=time.time()
    closest_pair(entities)
    end=time.time()
    y_1.append(end-start)
y_2=[]
for i in x:
    entities=generate_entities(i)
    start=time.time()
    closest_pair(entities)
    end=time.time()
    y_2.append(end-start)
y_3=[]
for i in x:
    entities=generate_entities(i)
    start=time.time()
    closest_pair(entities)
    end=time.time()
    y_3.append(end-start)
y_4=[]
for i in x:
    entities=generate_entities(i)
    start=time.time()
    closest_pair(entities)
    end=time.time()
    y_4.append(end-start)
y_5=[]
for i in x:
    entities=generate_entities(i)
    start=time.time()
    closest_pair(entities)
    end=time.time()
    y_5.append(end-start)
    
y_theoretical=[(i*(i-1)*0.5*10**-6)/2 for i in x]

plt.plot(x,y_1)
plt.plot(x,y_2)
plt.plot(x,y_3)
plt.plot(x,y_4)
plt.plot(x,y_5)
plt.plot(x,y_theoretical,linestyle='dashed')
plt.legend(['Empirical 1','Empirical 2','Empirical 3','Empirical 4','Empirical 5','Theoretical O(n^2)'])
plt.xlabel('Number of Entities')
plt.ylabel('Time (seconds)')
plt.title('Closest Pair Algorithm Time Complexity')
plt.grid()
plt.show()
    