#Iteration

i = 1
while i <=5:
    print(i)
    i = i + 1

print("Finished!")

#1
#2
#3
#4
#5
#Finished!
#------------------------------
#Odd and Even

x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1 
    
#1 is odd
#2 is even
#3 is odd
#4 is even
#5 is odd
#6 is even
#7 is odd
#8 is even
#9 is odd
#str(x) is used to convert the number x to a string, so that it can be used for concatenation.
#------------------------------
#Break

i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")

0
1
2
3
4
Breaking
Finished
#------------------------------
#Continue

i = 0
while True:
    i = i +1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)

print("Finished")

#1
#Skipping 2
#3
#4
#Breaking
#Finished
#------------------------------



