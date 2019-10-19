#before_ training
#Pre-Presidential Term Training
#Training Model Tials 3
#DelimiterV2, data_structV2, dataDumpV1

#Automated training
#DelimiterV2 - Preserves quotes and no sentence delimiting


#Integration with Selective Weight
#optimisation of weight used



from pickle import*
from random import*

no_files=27

all_file_l=["o_b_"+str(i)+".txt" for i in range (1,no_files+1)]
shuffle(all_file_l)

pick_out=input("Enter Pickle File name :")
rat_in=float(input("Enter (train:total) file ratio :"))

train_l=all_file_l[:round(no_files*rat_in)]
test_l=all_file_l[round(no_files*rat_in):]




#training and pickling file

"""
vars used
d --> dict
f --> file handle (closed)
a --> File read
l --> tokenised
lt --> mod tokens
b --> ??
fl --> Flag
t --> temp tokens
q --> temp quotes
ch --> temp dict value hold - for cross ch
p --> flag


"""

print("Starting Training\n\n")
print("No of Files used for Training :",len(train_l))


d={}

for file_n in train_l:

        
    f=open(file_n,'r')

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
                
            if l[i][-1] in ['.',',',';',':']:
                t.append(l[i][:-1].lower())
            elif l[i][-1]=='!':
                t=[l[i][:-1].lower(),'!']
                
            else:
                t.append(l[i].lower())
            lt.extend(t)


    #Data StructV2 : Accounts total occurences of former word
    #can be used to calculate probability
            
            
    i=0

    while i<len(lt)-1:
        if lt[i] not in d:
            d[lt[i]]=[1,[lt[i+1],1]]

        else:
            ch=d[lt[i]]
            p=1
            for j in range(len(ch)-1):
                if ch[j+1][0]==lt[i+1]:
                    ch[j+1][1]+=1
                    ch[0]+=1
                    p=0
                else:
                    pass

            if p:
                temp=[lt[i+1],1]
                ch.append(temp)
                ch[0]+=1
            d[lt[i]]=ch          
                          
        i+=1



    #print("Training with file :",file_n," completed!")
    print("#",end='')

#dataDumpV1
dump(d,open(pick_out+".p","wb"))
f.close()
d={}
print("\nData Dumped into ",pick_out,".p File")



#TESTING

#Optimising

def test_block():
    
    f=open(test_file,"r")
    a=f.read()
    f.close()

    
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
                
            if l[i][-1] in ['.',',',';',':']:
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
                    num=k[1]*pos_wt
                    #print('num',num)
                    break

            if(flag==0):
                num=-(neg_wt)

        else:
            num=-(neg_wt)
            den=1
            
        ct+=1
        #print('num/den ',float(num/den))
        tot+=float(num/den)

        #print(tot)
    

    #print('2 Word Link Probability for ',test_file,' :',tot*100/ct,'%')
    return round(tot*100/ct,3)




#Weights introduced

#test_l --> Obama Files
#test_n_l --> Non Obama

print("Starting Optimiser Varations \n")
opt_l=[round(0.1*i,1) for i in range(2,10)]

final_opt_vars=[]


for opt_var in opt_l:

    print("\nRatio :",opt_var)

    pos_in=5
    neg_in=5
    step=1.0


    d_p=load(open(pick_out+".p","rb"))

    all_test_n_l=["n_"+str(i)+".txt" for i in range (1,42)]
    shuffle(all_test_n_l)
    test_n_l_1=all_test_n_l[:round(42*opt_var)]        #for weight opt
    test_n_l_2=all_test_n_l[round(42*opt_var):]        #for actual testing

    temp_size=len(test_l)
    test_l_1=test_l[:round(temp_size*opt_var)]      #for Weight opt
    test_l_2=test_l[round(temp_size*opt_var):]      #for actual testing


    #test_final=test_l+test_n_l

    pos_wt=1.0
    neg_wt=0.0

    wt_res=[]

    print("No of Files Used in Optimiser :",len(test_l_1+test_n_l_1))
    while pos_wt<=pos_in:
        
        neg_wt=0

        while neg_wt<=neg_in:

            #print("pos_wt =",pos_wt,"  neg_wt =",neg_wt)
            print(".",end='')

            temp=[]
            for test_file in test_l_1:
                temp.append(test_block())
            o_min=min(temp)

            temp=[]
            for test_file in test_n_l_1:
                temp.append(test_block())
            n_max=max(temp)

            diff=o_min-n_max
            wt_res.append([diff,pos_wt,neg_wt])

            neg_wt+=round(step,2)

        pos_wt+=round(step,2)


    print("\n")
    wt_res.sort(reverse=True)
    pos_wt=wt_res[0][1]
    neg_wt=wt_res[0][2]

    temp=[]
    for test_file in test_l_1:
        temp.append(test_block())
    o_min=min(temp)

    temp=[]
    for test_file in test_n_l_1:
        temp.append(test_block())
    n_max=max(temp)

    cut_off=(o_min+n_max)/2

    """
    print("Optimised Weights ")
    print("Positive Weight :",pos_wt)
    print("Negative Weight :",neg_wt)
    print("\n\nCut Off :",cut_off)
    print("\nOptimisation Complete!")

    """

    #Actual TESTING ;)

    """
    Using test_l_2 and test_n_l_2
    expand to include custom file check
    """
    print("Testing")
    final_test=test_l_2+test_n_l_2
    shuffle(final_test)
    print("No of test files :", len(final_test))
    print("\n")

    yy,yn,ny,nn=0,0,0,0

    for test_file in final_test:
        sim_val=test_block()

        if sim_val<=cut_off:
            #print(test_file," is not an Obama File")
            if(test_file[0]=='n'):
                nn+=1
                print("*",end='')
            else:
                ny+=1
                print("|",end='')
        else:
            #print(test_file," is an Obama File")
            if(test_file[0]=='o'):
                yy+=1
                print("*",end='')
            else:
                yn+=1
                print("|",end='')

    print("\n\nConfusion Matrix")
    print("Actual ->")
    print("\tYes\tNo")
    print("Yes\t",yy,"\t",yn)
    print("No\t",ny,"\t",nn)

    print("\n\nAccuracy :",(yy+nn)*100/len(final_test),"%\n\n")

    final_opt_vars.append([opt_var,(yy+nn)*100/len(final_test),pos_wt,neg_wt])



for i in final_opt_vars:

    print("\nRatio :",i[0])
    print("Pos_wt :",i[2])
    print("Neg_wt :",i[3])
    print("Accuracy :",i[1])


                            






    
    










        
            
                
            
                        
            
            










