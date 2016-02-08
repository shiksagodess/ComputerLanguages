#This program create tuples, lists and uses slice

#here we are creating tuples
a=("one","two","three")
b=("four","five","six","seven")
c=(1,2,3,4,5,6,7)

print(a)
print(len(a))
print(b)
print(len(b))
print(a+b)

#This shows slice
print(c[1:])
print(c[2:4])

list = list(b)
print(list)
print(list[-2])
print(list[:3])
list[3] = "7"
print(list)
print(list[-1])
print(list[3])
list.insert(4, "eight")
print(list)