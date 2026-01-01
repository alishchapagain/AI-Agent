lst = [1,4,6,2,7,3]
lst1 = [11,12,13]
print(lst)

print(lst[3])
print(lst[1:4])

#List Methods
# 1 Append
lst.append(8)
print(lst)

# 2 Sort
lst.sort() #Ascending
print(lst)
#lst.sort(reverse=True) #Descending

# insert the list
lst.insert(4,5) # index, element
print(lst)

#add two list
lst.extend(lst1)
print(lst)