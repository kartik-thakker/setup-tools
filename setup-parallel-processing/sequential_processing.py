# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:49:54 2022

@author: KARTIK THAKKER
"""

import time

def factorial(n):
    time.sleep(0.5)
    if (n==1 or n==0):
        return 1
      
    else:
        return (n * factorial(n - 1)) 
  

if __name__ == '__main__':
    start = time.time()
    results = [factorial(i) for i in range(10)]
    print("Output: {}".format(results))
    end = time.time()
    print("Seconds since epoch =", end-start)