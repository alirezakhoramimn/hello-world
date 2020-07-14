# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:14:52 2020

@author: j.khorami
"""
from PIL import Image

def zarib3ya5(n):
    if n % 3 == 0 or n % 5 == 0 :
        return True 
    else: 
        return False 
    
    
sums = 0
for i in range(1,1000):
    if zarib3ya5(i):
        sums = sums + i
print(sums)

# as you see the answer is gonna be 233168

