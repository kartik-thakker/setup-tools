# -*- coding: utf-8 -*-
"""
Created on Sat May 14 15:49:54 2022

@author: KARTIK THAKKER
"""

import multiprocessing
import time
  
  
#pool is useful for time taking funcs
#instant return funcs have no pooling advantage
def factorial(n):
    time.sleep(0.5)
    if (n==1 or n==0):
        return 1
      
    else:
        return (n * factorial(n - 1)) 

#pool works only when using name == main
if __name__ == '__main__':
    start = time.time()
    pool = multiprocessing.Pool(processes = 3)
    result_async = [pool.apply_async(factorial, args = (i, )) for i in
                    range(10)]
    results = [r.get() for r in result_async]
    print("Output: {}".format(results))
    end = time.time()
    print("Seconds since epoch =", end-start)
    