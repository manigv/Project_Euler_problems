import sys
import time
start=time.time()
n=100000
s=0
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        s=s+i
print("sum 100000 prime numbers",s)
end = time.time()
print(end-start)
