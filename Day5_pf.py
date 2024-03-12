#While loop

i = 1
while i < 6:
    print(i)
    i += 1    #Prints 1,2,3,4,5
     
#Break statement
j = 1
while j<6:
    print(j)
    if j == 3:
        break
    j += 1    #Prints 1,2,3
    
#Continue statement
l = 0
while l < 6:
    l += 1
    if l == 3:
        continue
    print(l)        #prints 1,2,4,5,
    
#else statement

t = 1
while t < 6:
    print(t)
    t += 1
else:
    print("t is no longer less than 6")

#For Loop

fruits = ["Apple","Banana","Grape","Strawberry"]

for fruit in fruits:
    print(fruit)
    
#Range

for x in range(6):
    print(x)

#Nested
adjs = ["Big","Red","Juicy","Sweet"]
fruits = ["Cherry","Apple","Strawberry","Banana"]

for adj in adjs:
    for fruit in fruits:
        print(adj,fruit)

#Average Temp
totTemp = 0

for x in range(1,11):
    temp = float(input("What is the temp"))
    totTemp = totTemp + temp

ave = totTemp/10
print("Ave is",ave)
     
    























