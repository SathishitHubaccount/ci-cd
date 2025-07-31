def no_of_island(grid):
    n,m=len(grid),len(grid[0])
    visited=[[False]*m for i in range(n)]
    c=0
    def dfs(r,c):
        if r<0 or c<0 or r>=n or c>=m:
            return 
        visited[r][c]=True
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
        return 1
    
    for i in range(n):
        for j in range(m):
            if dfs(i,j) and grid[i][j]!=0:
                c+=1
    return c

def anagram(s,t):
    dec1={}
    dec2={}
    for i in s:
        if i in dec1:
            dec1[i]+=1
        else:
            dec1[i]=1
    for i in t:
        if i in dec2:
            dec2[i]+=1
        else:
            dec2[i]=1
    try:
        for i in dec1:
            if dec1[i]!=dec2[i]:
                return False
    except:
        return False
    return True


import math
def length(nums):
    c=0
    for i in nums:
        c+=1
    return c

def nothing():
    return None

def add(a,b):
    temp=a+b
    return temp if temp==a+b else a+b

def sub(a,b):
    temp=a-b
    return abs(a-b)

def mul(a,b):
    if a==0 or b==0:
        return 0
    return a*b
def div(a,b):
    if b==0:
        return None
    if a==0:
        return 0
    return a/b

def percentage(cur,tot):
    retrun (cur/tot)*100

def power(a,b):
    if b==0:
        return 1
    return a**b

def pi():
    return math.pi

def squar_root(a):
    return a**.5

def fact(a):
    if a<2:
        return 1
    tot=1
    for i in range(2,a+1):
        tot*=i
    return tot
           