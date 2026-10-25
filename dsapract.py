from array import *

val = array('i',[1,2,3,4,5])

# print(val)

# for i in range(0,4):
#     print(val[i])
#     i+=1

# print("\n")    
val.insert(1,50)
for i in range(0,len(val)):
    print(val[i], end = " ")

# print("\n")

# for x in val:
#     print(x, end = " , ")