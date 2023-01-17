b = False
a = int(input("write your number here:"))
for i in range(2,round(a/2)+1):
    if a % i == 0:
     b = True
    break
if b == False:
    print("number is prime")
if b == True:
    print("number is not prime")
