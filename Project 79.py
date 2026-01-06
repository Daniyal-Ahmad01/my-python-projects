import time
a=time.time()
i=1
while i<100:
    print(i)
    i+=1
b=time.time()
for i in range(1,101):
    print(i)
print(time.time()-a)
print(time.time()-b)