def greet(name):   #Function definition
    print("Hello " + name)
    print("Welcome to the world of Python")

greet("John")  #Function Call

def hello(a,b):  #name = "Bickky"
    print("Hello", a)
    print(b +5)
hello("Bickky",5)

def add(a,b):  #a = 5, b = 6
    sum  = a + b  #sum = 11
    return sum   #return 11
result = add(5,6)
print(result)    

def mul(a,b,c):
    mul = a * b * c
    print(mul) #210
j = mul(5,6,7)
print(j) #by default funtion return null

def my_func():
    x = 10  # x is local variable
    y = 20  # y is local variable
    print("value inside function : ", x, y)

z = 20  # z is global variable
my_func()
print("value outside function : ", z)
# print(y) # y is not accessible outside the function


def add(a=4,b=1,c=1):  
    sum  = a + b + c
    return sum   
result = add()
print(result)


def add(a,b,c=1):  
    sum  = a + b + c
    return sum   
result = add(b=3,a=5,c=4)
print(result)

def add(*a):
    print(a)#(1,2,3)
    print(type(a)) #tuple
    sum = 0
    for i in a:
        current_value = i
        total_value = current_value + sum
        sum = total_value
    return sum
    
print(add(1,2,3,4,5,6))


# sum = 0
# for i in a:
#     sum += i
# return sum

# s = add(1,2,3)
# print(s)
