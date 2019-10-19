Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35-32\ML\Project Final Run V1\With Stop Words\before_\int_wt_opt_V1.py 
Enter Pickle File name :bef_tr1_09
Enter (train:total) file ratio :0.9
Starting Training


No of Files used for Training : 24
Training with file : o_b_21.txt  completed!
Training with file : o_b_23.txt  completed!
Training with file : o_b_4.txt  completed!
Training with file : o_b_9.txt  completed!
Training with file : o_b_8.txt  completed!
Training with file : o_b_27.txt  completed!
Training with file : o_b_22.txt  completed!
Training with file : o_b_20.txt  completed!
Training with file : o_b_24.txt  completed!
Training with file : o_b_10.txt  completed!
Training with file : o_b_5.txt  completed!
Training with file : o_b_15.txt  completed!
Training with file : o_b_14.txt  completed!
Training with file : o_b_1.txt  completed!
Training with file : o_b_18.txt  completed!
Training with file : o_b_7.txt  completed!
Training with file : o_b_6.txt  completed!
Training with file : o_b_16.txt  completed!
Training with file : o_b_17.txt  completed!
Training with file : o_b_12.txt  completed!
Training with file : o_b_3.txt  completed!
Training with file : o_b_26.txt  completed!
Training with file : o_b_2.txt  completed!
Training with file : o_b_25.txt  completed!

Data Dumped into  bef_tr1_09 .p File
Starting Optimiser 


Enter Range for Positive Weight (1 to x) :5
Enter Range for Negative Weight (-y to 0) :5
Enter Step value for weight :1
No of Files Used in Optimiser : 23
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
Positive Weight : 5.0
Negative Weight : 5.0


Cut Off : -44.5755

Optimisation Complete!
Testing
No of test files : 21
n_20.txt  is not an Obama File
n_26.txt  is not an Obama File
n_15.txt  is not an Obama File
o_b_11.txt  is not an Obama File
n_23.txt  is not an Obama File
n_39.txt  is not an Obama File
n_41.txt  is not an Obama File
n_16.txt  is not an Obama File
n_40.txt  is not an Obama File
n_12.txt  is not an Obama File
n_9.txt  is not an Obama File
n_28.txt  is not an Obama File
n_30.txt  is not an Obama File
n_29.txt  is not an Obama File
n_22.txt  is not an Obama File
n_38.txt  is not an Obama File
n_7.txt  is not an Obama File
n_24.txt  is not an Obama File
n_5.txt  is not an Obama File
n_3.txt  is not an Obama File
n_36.txt  is not an Obama File


Confusion Matrix
Actual ->
	Yes	No
Yes	 0 	 0
No	 1 	 20


Accuracy : 95.23809523809524 %
>>> 
