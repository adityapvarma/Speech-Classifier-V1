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
            
        if l[i][-1]==',':
            t.append(l[i][:-1].lower())
        elif l[i][-1]=='!':
            t=[l[i][:-1].lower(),'!']
        elif l[i][-1]=='.':
            if l[i+1][-1]
            
        else:
            t.append(l[i].lower())
        lt.extend(t)


    
