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

no_files=150

all_file_l=["o_s_"+str(i)+".txt" for i in range (1,no_files+1)]
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



    print("Training with file :",file_n," completed!")


#dataDumpV1
dump(d,open(pick_out+".p","wb"))
f.close()
d={}


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
#0 weights - Proper Segregation

#test_l --> Obama Files
#test_n_l --> Non Obama




pos_in=int(input("\n\nEnter Range for Positive Weight (1 to x) :"))
neg_in=int(input("Enter Range for Negative Weight (-y to 0) :"))
step=float(input("Enter Step value for weight :"))


d_p=load(open(pick_out+".p","rb"))

all_test_n_l=["n_"+str(i)+".txt" for i in range (1,42)]
shuffle(all_test_n_l)
test_n_l_1=all_test_n_l[:21]        #for weight opt
test_n_l_2=all_test_n_l[21:]        #for actual testing

temp_size=len(test_l)
test_l_1=test_l[:round(temp_size/2)]      #for Weight opt
test_l_2=test_l[round(temp_size/2):]      #for actual testing



#test_final=test_l+test_n_l

pos_wt=1.0
neg_wt=0.0

#segregate obama and non

wt_res=[]


while pos_wt<=pos_in:
    
    neg_wt=0

    while neg_wt<=neg_in:

        print("pos_wt =",pos_wt,"  neg_wt =",neg_wt)

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

print("\n\nCut Off :",cut_off)


#Actual TESTING ;)

"""
Using test_l_2 and test_n_l_2
expand to include custom file check
"""

final_test=test_l_2+test_n_l_2
shuffle(final_test)
print("No of test file :", len(final_test))

yy,yn,ny,nn=0,0,0,0

for test_file in final_test:
    sim_val=test_block()

    if sim_val<=cut_off:
        print(test_file," is not an Obama File")
        if(test_file[0]=='n'):
            nn+=1
        else:
            ny+=1
    else:
        print(test_file," is an Obama File")
        if(test_file[0]=='o'):
            yy+=1
        else:
            yn+=1

print("\n\nConfusion Matrix")
print("Actual ->")
print("\tYes\tNo")
print("Yes\t",yy,"\t",yn)
print("No\t",ny,"\t",nn)

print("\n\nAccuracy :",(yy+nn)*100/len(final_test),"%")






    
    










        
            
                
            
                        
            
            










