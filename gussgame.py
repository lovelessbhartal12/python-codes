import random
n=random.randint(1,100)
print(n)
a=-1
c=0
while(a!=n):
    c= c+1

    a=int(input("guess a number"))
    if(a>n):
     print("please enter the less number")
     
    else:
     print("please enter the higher number")
print("your guess is right")
print(f"your guess is right in attempt....",c)




