'''# Step 1: Start with a list
fruits = ['apple', 'banana', 'cherry']

# Step 2: Get the iterator from the list
fruit_iterator = iter(fruits)

# Step 3: Get each item one by one
print(next(fruit_iterator))  # apple
print(next(fruit_iterator))  # banana
print(next(fruit_iterator))  # cherry
print(next(fruit_iterator))  # Raises StopIteration

for fruit in fruits:
    print(fruit)

it = iter(fruits)
while True:
    try:
        fruit = next(it)
        print(fruit)
    except StopIteration:
        break
'''
names = ['lahari' , 'sailu', 'keerthi']
my_iteratore = iter(names)

#for name in names:
   # print (name)
    
it = iter(names)
while True:
    try:
        name = next(it)
        print(name)
    except stopIteratioun:
        break
