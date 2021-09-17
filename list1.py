list = []


# python programme to find smallest
#number in a list


#create number of elements to put in list
num = int(input("Enter number of elements in list:"))

# iterating till num to append elements in list
for i in range(1,num +1):
    ele= int(input("Enter elements: "))
    list.append(ele)
# print maximum elements
print("Greatest  elements is:", max(list))