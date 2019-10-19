#Basic testing model. No of occurences mapped

a="this is a test message this is do"
l=a.split()

i=0
d={}

while i<len(l)-1:
    if l[i] not in d:
        d[l[i]]=[[l[i+1],1]]

    else:
        ch=d[l[i]]
        p=1
        for j in range(len(ch)):
            if ch[j][0]==l[i+1]:
                ch[j][1]+=1
                p=0
            else:
                pass

        if p:
            lt=[l[i+1],1]
            ch.append(lt)
        d[l[i]]=ch          
                      
    i+=1
        
        
        
    
    
    
    
