# f = open("name.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("name.txt","r")
# # data = f.read(5)
# data = f.read()
# print(data)
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

f = open("name.txt","r")
# data=f.read()
data=f.read(5)
line1=f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

print(data)
print(type(data))
f.close
