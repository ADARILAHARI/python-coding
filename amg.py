#print("python is \nesay to use ")
'''
x=6
y=4
print(x,y, sep=":")
print("hello"*4)
hellohellohellohello
print(" hello "*5)
 hello  hello  hello  hello  hello 
print("class =" + "ams" + "ist")
class =amsist


a=10
b=15
c=20
m=(a+b+c)/2
area=(m*(m-a)*(m-b)*(m-c))**0.5
print(area)
k

a=10
b=15
area= 1/2*b*a
print(area)

x=25
m= x**0.5
print(m)

s = "hello"
rev_s = ''.join(reversed(s))
print(rev_s)

s="lahari"
rev_s= s[::-1]
print(rev_s)

def rev_s(s):
    result=''
    for char in s:
        result=char+result
    return result

print(rev_s("lahari"))

s= str(input())
rev_s= s[::-1]
print(rev_s)

s= str(input())
rev_s= ''.join(reversed(s))
print(rev_s)

def pal_s(s):
    s= input()
    pal_s = s[::-1]
    print(pal_s)

    if pal is pal_s:
        print(true)
    else:
        print(false)
    
def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print(fact(8))
    
import math
print(math.factorial(5))

def feb(n):
    if n<=1:
        return n
    else:
        return feb(n-1)+feb(n-2)
for i in range(10):
    print(feb(i), end =' ')
    
def feb(n):
    a , b = 0,1
    for i in range(n):
        print(a, end = ' ')
        a , b = b, a+b
feb(10)

print("enter a num: ", end='')
n = int(input())

def sum(n):
    total=0
    while n>0:
        digit = n%10
        total += digit
        n = n//10
    return total
print(sum(n))


def prim(n):
    if n<=1:
        print("n is not a prime num")
        return
    for i in range(2,n):
        if n% i == 0:
            print(n, "is a prime num")
            return
    print(n, "is prim")
num = int(input())
prim(num)     ''

n=input()
m="a"
for i in n:
    if i!=m:
        print(i,end="")
x=3
n=20
while x<=n:
    print(x)
    x+=1
     
ch = 'a'
vowels= 'aeiou'
while ch <= 'z':
    if ch not in vowels:
        print(ch)
    ch = chr(ord(ch)-1)
    #ch = chr(ord(ch)-1)''
ch = {1,2,3,4,4,5,2}
print(ch)

'''

n = "banana"
set_n= set(n)
print(set_n, end='#')
    


        
