t=input().split(" ")
t=tuple(map(int,t))
g=[]
for k in range(len(t)):
    g.append([])

for i in range(len(t)):
    for u in range(3601):
        d=u%(2*t[i])
        if d<t[i]-5:
            g[i].append(1)
        else:
            g[i].append(0)
t_min=min(t)
for i in range(t_min+1,3601):
    c=1
    for j in range(len(t)):
        c*=g[j][i]
    if c!=0:
        print(i)
        break

        