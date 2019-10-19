Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35-32\ML\Project Final Run V1\With Stop Words\before_\int_wt_opt_V1.py 
Enter Pickle File name :bef_tr1_01
Enter (train:total) file ratio :0.1
Starting Training


No of Files used for Training : 3
Training with file : o_b_8.txt  completed!
Training with file : o_b_7.txt  completed!
Training with file : o_b_3.txt  completed!

Data Dumped into  bef_tr1_01 .p File
Starting Optimiser 


Enter Range for Positive Weight (1 to x) :5
Enter Range for Negative Weight (-y to 0) :5
Enter Step value for weight :1
No of Files Used in Optimiser : 33
pos_wt = 1.0   neg_wt = 0
pos_wt = 1.0   neg_wt = 1.0
pos_wt = 1.0   neg_wt = 2.0
pos_wt = 1.0   neg_wt = 3.0
pos_wt = 1.0   neg_wt = 4.0
pos_wt = 1.0   neg_wt = 5.0
pos_wt = 2.0   neg_wt = 0
pos_wt = 2.0   neg_wt = 1.0
pos_wt = 2.0   neg_wt = 2.0
pos_wt = 2.0   neg_wt = 3.0
pos_wt = 2.0   neg_wt = 4.0
pos_wt = 2.0   neg_wt = 5.0
pos_wt = 3.0   neg_wt = 0
pos_wt = 3.0   neg_wt = 1.0
pos_wt = 3.0   neg_wt = 2.0
pos_wt = 3.0   neg_wt = 3.0
pos_wt = 3.0   neg_wt = 4.0
pos_wt = 3.0   neg_wt = 5.0
pos_wt = 4.0   neg_wt = 0
pos_wt = 4.0   neg_wt = 1.0
pos_wt = 4.0   neg_wt = 2.0
pos_wt = 4.0   neg_wt = 3.0
pos_wt = 4.0   neg_wt = 4.0
pos_wt = 4.0   neg_wt = 5.0
pos_wt = 5.0   neg_wt = 0
pos_wt = 5.0   neg_wt = 1.0
pos_wt = 5.0   neg_wt = 2.0
pos_wt = 5.0   neg_wt = 3.0
pos_wt = 5.0   neg_wt = 4.0
pos_wt = 5.0   neg_wt = 5.0
Optimised Weights 
Positive Weight : 1.0
Negative Weight : 0


Cut Off : 3.6310000000000002

Optimisation Complete!
Testing
No of test files : 32
n_32.txt  is not an Obama File
n_27.txt  is not an Obama File
o_b_12.txt  is an Obama File
n_26.txt  is not an Obama File
n_21.txt  is not an Obama File
n_29.txt  is not an Obama File
n_9.txt  is not an Obama File
o_b_6.txt  is an Obama File
n_19.txt  is not an Obama File
o_b_20.txt  is an Obama File
n_17.txt  is not an Obama File
n_1.txt  is not an Obama File
n_20.txt  is not an Obama File
n_33.txt  is not an Obama File
n_3.txt  is not an Obama File
o_b_27.txt  is an Obama File
n_28.txt  is not an Obama File
o_b_14.txt  is an Obama File
o_b_23.txt  is an Obama File
n_31.txt  is not an Obama File
n_18.txt  is not an Obama File
o_b_24.txt  is an Obama File
n_40.txt  is not an Obama File
o_b_4.txt  is an Obama File
n_30.txt  is not an Obama File
n_6.txt  is not an Obama File
n_4.txt  is not an Obama File
o_b_21.txt  is an Obama File
o_b_2.txt  is an Obama File
o_b_1.txt  is an Obama File
o_b_18.txt  is not an Obama File
n_22.txt  is not an Obama File


Confusion Matrix
Actual ->
	Yes	No
Yes	 11 	 0
No	 1 	 20


Accuracy : 96.875 %
>>> 
