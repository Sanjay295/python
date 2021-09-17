"""
Slicing on array can be used to retrive a piece of the array that contains a group of elements.
Slicing is usedful to retrive  a range of elements.
Syntax:-
        new_array_name = array_name[start:stop:stepsize]
"""
from array import *
stu_roll = array('i',[101,102,103,104,105,106,107])
print("Origan Array")
n = len(stu_roll)
for i in range(n):
    print(i, "=",stu_roll[i])
print("****************")
a = stu_roll[0:7:2]
for i in a:
    print(i)
    