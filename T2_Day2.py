#Duplicates are ignored


thisset = {"apple","banana","cherry","apple","banana","cherry"}
print(thisset)

print(len(thisset))

set1 = {"apple","banana","cherry"}
set2 = {1,5,7,9,3}
set3 = {True,False,False}
set4 = {"abc",34,True,40,"male"}

thisset2 = set(("apple","banana","cherry"))
print(thisset2)

for x in thisset:
    print(x)

print("banana" in thisset)

thisset.add("orange")
print(thisset)

tropical = {"pineapple" , "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset2.remove("banana")
print(thisset2)

thisset.discard("banana")
print(thisset)

thisset3 = {"apple","banana","cherry"}
thisset3.clear()

print(thisset3)

set4 = set1.union(set2)
set5 = set3 | set4 
print(set4)
print(set5)


myset = set1.union(set2,set3,set4)
print(myset)

set7 = set1.intersection(set2) # or use set7 = set1 & set2
print(set7)


set8 = set1.difference(set2)
print(set8)

