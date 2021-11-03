#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n - Should be the size of the initial array
#  2. INTEGER_ARRAY ar - Array of intergers that will contains "socks"
#

def sockMerchant(n, ar):
    '''
        Count the amount of the elements in the list
        and sum the result of the %2 division to get
        the amount of pairs
    '''    
    totalPairs = 0
    size = n 
    i = 0

    # Iterate the list until size of the list
    # is more than 2 elements
    while size > 1:
        #Get always the sock in the first position
        sock = ar[i]
        
        # Count how many times that item 
        # appears in the list  
        numOcurr = ar.count(sock)

        # If we have at least two items, 
        # means that at least exist 1 pair of the sock 
        if numOcurr >= 2:
            # Get the amount of number of pairs
            numPairs = numOcurr // 2
            # Increase the total of pairs
            totalPairs = totalPairs + numPairs
         
        # Once the sock is counted, remove all the 
        # appearances of the element or the element itself
        # since it doesn't exist pair for that element
        ar[:] = (s for s in ar if s != sock)
        
        # Recalculate the size of the list 
        # making sure that all elements of the list are cover
        size = len(ar)
    
    return totalPairs
