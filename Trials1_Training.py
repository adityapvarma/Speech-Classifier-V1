
#Pre processing  - Tokenizing
f=open("sample1.txt",'r')
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


#Training Dataset
i=0
d={}

while i<len(lt)-1:
    if lt[i] not in d:
        d[lt[i]]=[[lt[i+1],1]]

    else:
        ch=d[lt[i]]
        p=1
        for j in range(len(ch)):
            if ch[j][0]==lt[i+1]:
                ch[j][1]+=1
                p=0
            else:
                pass

        if p:
            sm=[lt[i+1],1]
            ch.append(sm)
        d[lt[i]]=ch          
                      
    i+=1
        
        
