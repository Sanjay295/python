
"""
# python program to print Even Numbers in a List

# List of numbers
list = [103, 105, 6, 67, 89, 66, 77, 44]
# iterating each number in the list
for num in list:
    #checking condition
    if num % 2 == 0:
        print(num, end = " ")
 
        
        
        
# Using while Loop
# list of numbers
list = [88,21,4,67,66,45,90] 
num = 0
# Using while loop
while(num< len(list)):
    # checking condition
    if num % 2 == 0:
        print(list[num],end = " ")
    # increament num
    num += 1
    
    """
  
  
# Using list comprehension:
# python program to print even Numbers in a List
# list of numbers
list = [15,67,34,88,105, 210]
# Using list comprehension
even_nos = [num for num in list if num % 2 == 0]
print("odd numbesr in the list:", even_nos)
