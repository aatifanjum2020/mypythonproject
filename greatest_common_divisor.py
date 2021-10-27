#! /usr/bin/python3.8


import math

def gcd(x , y , z):
    divisors_list = []
    for i in range(1, min(x , y,z)+1):
        if x % i == 0 and y % i == 0 and z % i == 0:
            divisors_list.append(i)
    
    print(max(divisors_list))
    return max(divisors_list)





x = gcd(100,200,300)



  





