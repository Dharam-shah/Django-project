# Decision Making And Loop
a = 5
b = 10
c = a > b
print(c)

# Comparison Operators
p = 5
q = 10
print(p == q) # False
print(p != q) # True
print(p < q) # True
print(p > q) # False
print(p <= q) # True
print(p >= q) # False

#and operator
x = 5
y = 10
z = 10

print(x == y and x == z) # False
print(x == y and x != z) # False
print(x == y and x < z) # True

#or operator
print(x == y or x == z) # True
print(x == y or x != z)  # True
print(x == y or x < z) # True

#not operator
print(not(x == y)) # False
print(not(x == z)) # True

# If..else statement
d = 5
e = -1
if d > 0:
    print('d is positive')

print('This is always executed')

if e > 0:
    print('e is positive')

print('This is always executed')

# if...else
f = -1
if f >= 0:
    print('f is positive or zero')

else:
    print('f is negative')

print('This is always executed')

# if...elif...else
g = -1
if g > 0:
    print('g is positive')
elif x == 0:
    print('g is zero')
else:
    print('g is negative')

print('This is always executed')

# Nesting if...else
num  = float(input('Enter a number: '))
if num >= 0:
    if num == 0:
        print('Zero')
    else:
        print('Positive number')
else:
    print('Negative number')

# While loop
n = 3
i = 1
while i <= n:
    print(i)
    i = i + 1

#infinite loop
while i <= n:
    print(i)

# For loop
#string
a = "Python"
for letter in a:
    print('Current Letter:', letter)

#lists
m = [1, 2, 3]
n = ['Python', 'JavaScript', 'C++']
for ele in m:
    print('Current Element:', ele)

for language in n:
    print('Current language:', language)

#range()
numbers = list(range(1, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for num in numbers:
    sum = sum + num

print('Sum :', sum)

# Break and continue statement
number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numb1 in number1:
    if numb1 == 5:
        break
    print(numb1)

number2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numb2 in number2:
    if numb2 == 5:
        continue
    print(numb2)

# Pass statement
number3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numb3 in number3:
    pass