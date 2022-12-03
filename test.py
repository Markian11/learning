a = int(input("write your number here:"))
for i in range(2,round(a/2)+1):
    if a % i == 0:
     print(a,"its not a prime number")
    break
else: 
    print(a,"its a prime number")