#Tester
#Weights introduced
#0 weights - Ok OK segregation. Check weights

from pickle import *

d_p=load(open("common_1.p","rb"))

test_o_l1=["o_s_"+str(i)+".txt" for i in range (5,11)]
test_o_l2=["o_f_"+str(i)+".txt" for i in range (5,11)]
test_o_l3=["o_b_"+str(i)+".txt" for i in range (5,11)]
test_n_l=["n_"+str(i)+".txt" for i in range (1,11)]
test_l=test_o_l1+test_n_l+test_o_l2+test_o_l3


for test_file in test_l:
    f=open(test_file,"r")

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
    

    print('2 Word Link Probability for ',test_file,' :',tot*100/ct,'%')
            
            
            
        

