'''
求单调递减最长路径
'''
graph=[[30,21,17,12],
       [27,18,16,14],
       [31,24,12,27]]
def mcs(graph):
    plen=0
    ppo=[]
    tmp=[]
    res=[]
    m=len(graph)
    n=len(graph[0])
    for x0 in range(0,m):
        for y0 in range(0,n):
            ans={}
            q=[]
            ans[(x0,y0)]=[[(x0,y0)]]
            q.append((x0,y0))
            while q:
                d=q.pop(0)
                x=d[0]
                y=d[1]
                if  x>=1 and graph[x-1][y]<graph[x][y] :
                    q.append((x-1,y))
                    if (x-1,y) not in ans:
                        ans[(x-1,y)]=[]
                        for g in ans[(x,y)]:
                            ans[(x-1,y)].append(g+[(x-1,y)])
                    else:
                        for t in ans[(x,y)]:
                            ans[(x-1,y)].append(t+[(x-1,y)])
                if  x<m-1 and graph[x+1][y]<graph[x][y]:
                    q.append((x+1,y))
                    if (x+1,y) not in ans:
                        ans[(x+1,y)]=[]
                        for g in ans[(x,y)]:
                            ans[(x+1,y)].append(g+[(x+1,y)])
                    else:
                        for t in ans[(x,y)]:
                            ans[(x+1,y)].append(t+[(x+1,y)])
                if y>=1 and graph[x][y-1]<graph[x][y] :
                    q.append((x,y-1))
                    if (x,y-1) not in ans:
                        ans[(x,y-1)]=[]
                        for g in ans[(x,y)]:
                            ans[(x,y-1)].append(g+[(x,y-1)])
                    else:
                        for t in ans[(x,y)]:
                            ans[(x,y-1)].append(t+[(x,y-1)])
                if y<n-1 and graph[x][y+1]<graph[x][y] :
                    q.append((x,y+1))
                    if (x,y+1) not in ans:
                        ans[(x,y+1)]=[]
                        for g in ans[(x,y)]:
                            ans[(x,y+1)].append(g+[(x,y+1)])
                    else:
                        for t in ans[(x,y)]:
                            ans[(x,y+1)].append(t+[(x,y+1)])

            for point in ans.values():
                for pointi in point:
                    if plen<len(pointi):
                        plen=len(pointi)
                        ppo=point
    maxpp=[]
    for pp in ppo:
        if len(pp)==plen and pp not in maxpp:
            maxpp.append(pp)
    #因为q.append可以重复添加，因此去重
    for pri in maxpp:
        for poi in pri:
            print(graph[poi[0]][poi[1]])
    return maxpp

res=mcs(graph)
print(res)