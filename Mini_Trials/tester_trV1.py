#Tester
#No Negative Weights introduced

from pickle import *

d_p=load(open("sample1_pick.p","rb"))
f=open("sam_ts_1.txt","r")

a=f.read()
l=a.split()
lt=[]

b=[]
fl=0

for i in range(len(l)):
    t=[]

    if fl:
        
        if l[i][-1]=='"':
            lt.append(q)
            q=[]
            fl=0
        else:
            q=q+" "+l[i]
            
            
    else:

        #checking quotes
        if l[i][0]=='"':
            q=l[i][1:]
            fl=1
            continue
            
        if l[i][-1] in ['.',',']:
            t.append(l[i][:-1].lower())
        elif l[i][-1]=='!':
            t=[l[i][:-1].lower(),'!']
            
        else:
            t.append(l[i].lower())
        lt.extend(t)

#lt holds tokenised test
#d_p holds the dictionary [tot,[word,ct]]
tot=0
ct=0

for i in range(len(lt)-1):
    flag=0
    #print(lt[i],' taken')
    if lt[i] in d_p:
        den=d_p[lt[i]][0]
        #print('den ',den)

        for k in d_p[lt[i]][1:]:
            if lt[i+1] in k:
                #print('match found')
                flag=1
                num=k[1]
                #print('num',num)
                break

        if(flag==0):
            num=0

    else:
        num=0
        den=1
        
    ct+=1
    #print('num/den ',float(num/den))
    tot+=float(num/den)

    #print(tot)
    

print('Similarity Value :',tot*100/ct,'%')
            
            
            
        

