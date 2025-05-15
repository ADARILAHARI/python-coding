list = ["lahari", "sailu" , "keerthi" ,"sowji", "janu"]
#print(list)

print (list[0])
print(list[0:5])
print(list[::-1])
print(list[::-2])
print(list[0:2])
#o/p
['lahari', 'sailu', 'keerthi', 'sowji', 'janu']
['janu', 'sowji', 'keerthi', 'sailu', 'lahari']
['janu', 'keerthi', 'lahari']
['lahari', 'sailu']
#append
name = ["lahari", "sailu" , "keerthi" ,"sowji", "janu"]
#print(name[3:4:])
name.append("barthi")
print(name)
#let's take empty list and add()
list = []
list.append(1)
list.append(2)
list.append(4)
list.append(5)
list.append(7)
print(list)
print(list[0:3])

m = []
for x in range(2,11):
    m.append(x**2)
print(m) 
#comprehensions:
m = [i**2 for i in range(2,11)]
print(m)
#slicing
m = m[::-1]
print(m)
#copy
m = m[:]
#o/p
[4, 9, 16, 25, 36, 49, 64, 81, 100]
[4, 9, 16, 25, 36, 49, 64, 81, 100]
[100, 81, 64, 49, 36, 25, 16, 9, 4]

