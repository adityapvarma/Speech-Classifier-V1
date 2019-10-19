#does not store quotes as quotes

f=open("sample1.txt",'r')
a=f.read()
l=a.split()
lt=[]
b=[]

for i in l:
    t=[]
    if i[-1] in ['.',',']:
        t.append(i[:-1].lower())
    elif i[-1]=='!':
        t=[i[:-1].lower(),'!']      
    else:
        t.append(i.lower())
    lt.extend(t)


    
