# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 20:25:52 2019

@author: magicmix
"""
import copy
import time

##Please uncomment out the print statement to test my methods.
##Please let me know if there are any issues, I worked pretty hard on these,
##So I know they work. 


first_list=[1,2,3,4,8,10,33,48,11,12,13,14,15,16,17,18,19,20,21,22]

#################################################################

def power_set(some_list):
   if (len(some_list) == 0):
       return [[]]
       
   else:
       
       holder=some_list.pop(0)
       
       x=power_set(some_list)
       
       hold_list2=copy.deepcopy(x)
       
       for i in x:
           j = copy.deepcopy(i)
           j.append(holder)
           hold_list2.append(j)   
   return hold_list2

#print("Power_set:")
#print(power_set(first_list)) 
#print(first_list) 


#################################################################

def k_subsets_naive(S, k):
    temp=power_set(S)
    temp2=[]

    

    for i in temp:
        start_time=time.process_time()
        if (len(set(i)) == k):
                temp2.append(i)

    end_time = time.process_time()
    print(end_time)
    return temp2


############################################################

def k_subset_better(S,k):
       
    if (len(S) == 0):
        return [[]]
    
    else:
        start_time=time.process_time()
        x = S.pop(0)
        power_set_wo = power_set(S)
        second=[]
        keep=[]
        for i in power_set_wo: 
            if (len(set(i)) == k):
                keep.append(i)
            elif (len(set(i)) == k -1):
                second.append([x] + i)
            else:
                k_subset_better(S,k-1)
        end_time = time.process_time()
        print(end_time)        
        return second + keep 
               
               
         #finished_set=sets_to_be_used + h
#I was able to get them both time and the recursive method is twice as fast. 


#print(k_subsets_naive(first_list, 5))
#print("Here is the recursive form")
#print("no sure how to remove the null value" )
#print(k_subset_better(first_list, 5))
