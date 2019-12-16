#!/usr/bin/env python

def pw_checker(num):
    num_arr = [int(x) for x in str(num)]
    adjacency_check = False
    is_decreasing = False
    
   
    for i in range(len(num_arr)-1):
         
         # Check that each digit is smaller than the next
        if (num_arr[i] > num_arr[i + 1]):
            is_decreasing = True
            break 
        # Check that there exists two adjacent digits that are the same 
        if ((num_arr[i] ==  num_arr[i+1]) and num_arr.count(num_arr[i]) == 2):
            adjacency_check = True
        
    return adjacency_check and not(is_decreasing)

pw_list = []
for num in range(128392, 643281):
    if (pw_checker(num)):
        pw_list.append(num)

print(len(pw_list))

print(pw_checker(111111))
print(pw_checker(223450))
print(pw_checker(123789))
