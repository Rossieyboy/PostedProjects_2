First_Names = ["Leander","Ehan","Jonatewin","Alex","Rondea","Shaune","Christo","Bradley","Mervin","Aidan","Janco","Mercholm","Wade","Lucian","Marcus","Eugene","Daniel","Adam","Sihle","Zaid","Jonathan","Anro","Junior","Wian","Danjo","Erik","Elaine","Stefan","Luvuyo"]



First_Names.sort()
First_Names.insert(0,"Ross")
First_Names.pop(-1)
First_Names_copy = First_Names.copy()
First_Names.remove("Ross")
print(First_Names,"\n")
First_Names_copy.sort(reverse=True)  #Reverse alphabetical 
print(First_Names_copy,"\n")

x=0 #Prints everything in the list in a new line
for first_name in First_Names:
    
    first_name = First_Names[x]
    x += 1
    print(first_name,"\n")
    
