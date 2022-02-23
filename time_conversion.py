#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
  
  s_list = s.split(':')
  
  if s[-2:] == 'AM':
    if s[:2] == '12':
      s_list[0] = '00'
      # final_s = ':'.join(s_list)
      # return str(final_s[:-2])
  
  elif s[-2:] == 'PM':
    
    if s[:2] != '12':
      s_list[0] = str(int(s_list[0]) + 12)
      
  final_s = ':'.join(s_list)
  return str(final_s[:-2])
  
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


