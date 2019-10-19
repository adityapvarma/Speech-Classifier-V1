#Tester
#Freq Dist Plot

from pickle import *
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

d_p=load(open("sample1_pick.p","rb"))

l_fd={}
l_fdl=[]

x,y=[],[]

for i in d_p:
    l_fdl.append((i,d_p[i][0]))
    l_fd[i]=d_p[i][0]
    x.append(i)
    y.append(d_p[i][0])


