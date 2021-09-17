"""
# Using list comprehensions:
list = [20,56,79,111,221]
only_odd = [num for num in list if num % 2== 1]

print("Odd numbers in the list:", only_odd)



# Using fro loop
list = [10,29,49,50,80,78]
for num in list:
    if num % 2 != 0:
        print(num,end = " ")



# Using while loop
list = [10,21,6,67,95,111,198,201,505]
i = 0
while(i < len(list)):
# checking conditions
    if list[i] % 2 != 0:
        print(list[i],end = " ")
    i += 1
 """



# Using lambda expressions:
# Python program to print odd numbers in a List
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93, 11] 
  
  
# we can also print odd no's using lambda exp. 
odd_nos = list(filter(lambda x: (x % 2 != 0), list1))
  
print("Odd numbers in the list: ", odd_nos) 