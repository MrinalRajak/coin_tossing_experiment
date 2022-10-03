

# 1:write python code to simulate single fair coin tossing experiment
# to numerically verify the probability of appearance of Heads and Tails.


import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint
import random

N=100
recordList=[]
for i in range(N):
    flip=random.randint(0,1)
    if (flip == 0):
        # print "Heads"
        recordList.append(1)
    else:
        # print "Tails"
        recordList.append(0)

print ("coin toss result is: ",str(recordList))
print ("Value of N is: ",N)
print ("No.of Heads: ",recordList.count(1))
print ("No.of Tails: ",recordList.count(0))
Prob_H= (recordList.count(1))/N
Prob_T= (recordList.count(0))/N
print ("Probability of Head is: ",Prob_H)
print ("Probability of Tail is: ",Prob_T)
        
        

        

        

