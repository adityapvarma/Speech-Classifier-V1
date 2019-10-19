#Basic testing model.
#No of occurences mapped.
#Total no of links with the former word notes as first item in the value list.


a="this is a test message this is do"
l=a.split()

i=0
d={}

while i<len(l)-1:
    if l[i] not in d:
        d[l[i]]=[1,[l[i+1],1]]

    else:
        ch=d[l[i]]
        p=1
        for j in range(len(ch)-1):
            if ch[j+1][0]==l[i+1]:
                ch[j+1][1]+=1
                ch[0]+=1
                p=0
            else:
                pass

        if p:
            lt=[l[i+1],1]
            ch.append(lt)
            ch[0]+=1
        d[l[i]]=ch          
                      
    i+=1
        
        
        
    
    
    
    
