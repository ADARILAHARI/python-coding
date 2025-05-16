'''def count(n):
    i = 1
    while i <= n:
        yeild i
        i += 1

        counter = count(5)

        print(next(counter))
        print(next(counter))
        print(next(counter))
        print(next(counter))
        print(next(counter))
        print(next(counter))
        
''
a = [1,2,3,4]
b = [3,5,6,7]

print(7 in b)'

#sum of add elemtents

a = int(input( ))

''x,y,z = a.split( )
sum = int (x)+ int (y)+int (z)
print(f"sum of :{sum}")''

def fullname():
    first_name="lahari"
    lastname="adari"
    full_name=first_name+ ' '+ lastname
    print(full_name)
fullname()
''
list = ["lahari", "sailu" , "keerthi" ,"sowji", "janu"]
#print(list)
print (list[0])
print(list[0:5])
print(list[::-1])
print(list[::-2])
print(list[0:2])
'''
'''lahari
['lahari', 'sailu', 'keerthi', 'sowji', 'janu']
['janu', 'sowji', 'keerthi', 'sailu', 'lahari']
['janu', 'keerthi', 'lahari']
['lahari', 'sailu']''

name = ["lahari", "sailu" , "keerthi" ,"sowji", "janu"]
#print(name[3:4:])
name.append("barthi")
print(name)
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
print(list[0:3])'''

'''1. Even or Odd
Write a program to check whether a number is even or odd.

i = int(input("enter number:" ))
if i%2==0:
    print("i is even")
else:
    print("i is not even")
    x = int(input())
'' t f f t f t ''
print(x==42)
print(x!=42)
print(x>42) 
print(x>=42)
print(x<42)
print(x<=42)

        
''

list = ['1','2','3','4']
print(list)
''
x=5
y=6
print("the value of x {} and y {}".format(x,y))
print(x,y,sep = ',')
''


t=(1,3,4,2)
print(*t)
''
a = (input())
b = (input())
print(a,b,a,b, sep = ' ', end = " end here")

''
expected = '5'
e = "you enter :5"


''
l = ['a', 'c', 'b', 'd', 'e']
i = 0
n = 4  # loop 10 times

for _ in range(n):
    print(l[i])
    i = (i + 2) % len(l)

l=l[i]
print(l[i])
print("Last item in list:", l[-1])

''
s=(input("enter any strint: "))
f={}
for char in s:
    f[char]=f.get(char,0)+1
    f[char]+=1
print(f)
''

def longest_word(s):
    words=s.split()
    return max(words,key=len)

print(longest_word("i love python programming"))
               
''

#anagram
str1 = "School Master"
str2 = "The Classroom"

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

print(str1)  # Output: schoolmaster
print(str2)  # Output: theclassroom

''
#non-repating
def non_repeating_chars(s):
    for char in s:
        if s.count(char) == 1:
            print(char, end=' ')

# Example
non_repeating_chars("programming")


''
def compress_string(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))  # for the last character
    return ''.join(compressed)

# Example usage:
input_string = "aaabbbccdaa"
print(compress_string(input_string))  # Output: "a3b3c2d1a2"

''
def count_w(s):
    return len(s.split())

print(count_w("hi everyone how are you"))

''
s= input("")
l = len(s.split())
print(l)
''

s = input("")
m = ' '.join(s.split()[::-1])
print(m)
''
n = [2,3,4,21]
def  max_min(n):
    return max(n),min(n)
print(max_min(n))

'''

def rev(r):
    return r[::-1]

print(rev(['1','2','3','4','5']))

































