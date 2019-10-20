#!/bin/python3

import math
import os
import random
import re
import sys

def valid(a,b,n):
    if 0<=a<n and 0<=b<n:
        return True
    return False

def bfs(n,q,ei,ej):
    vis = [['0' for j in range(n)] for i in range(n)]
    while len(q)!=0:
        ni,nj,c,p = q.pop()
        if valid(ni,nj,n):
            if vis[ni][nj] == '0':
                vis[ni][nj] = p
                if ni==ei and nj==ej:
                    print(c)
                    break
                q.insert(0,(ni-2,nj-1,c+1,'UL'))
                q.insert(0,(ni-2,nj+1,c+1,'UR'))
                q.insert(0,(ni,nj+2,c+1,'R'))      
                q.insert(0,(ni+2,nj+1,c+1,'LR'))
                q.insert(0,(ni+2,nj-1,c+1,'LL'))
                q.insert(0,(ni,nj-2,c+1,'L'))
            else:
                continue
        else:
            continue
    if len(q)==0 and vis[ei][ej] == '0':     
        print('Impossible')
    else:
        trav = []
        s = vis[ei][ej]
        while s!='ST':
            trav.append(vis[ei][ej])
            s = vis[ei][ej]
            if vis[ei][ej] == 'UL':
                ei,ej = ei+2,ej+1
            elif vis[ei][ej] == 'UR':
                ei,ej = ei+2,ej-1
            elif vis[ei][ej] == 'R':       
                ei,ej = ei,ej-2
            elif vis[ei][ej] == 'LR':
                ei,ej = ei-2,ej-1
            elif vis[ei][ej] == 'LL':
                ei,ej = ei-2,ej+1
            elif vis[ei][ej] == 'L':
                ei,ej = ei,ej+2
        print(' '.join(trav[:-1][::-1]))   
            
n = int(input())
si,sj,ei,ej = map(int,input().split())
q = [(si,sj,0,'ST')]
bfs(n,q,ei,ej)
