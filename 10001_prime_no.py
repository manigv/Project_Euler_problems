#!/usr/bin/env python
import sys
#prime or not
n=int(input("Enter a number:"))
for i in range(2,n):
    if n%i==0:
        print ("The number you a entred is Not a Prime number.")
        break
else:
    print("The number you have entred is a Prime number")
