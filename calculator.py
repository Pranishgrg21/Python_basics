"""shortcut way yo chai"""

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# print("Add:", x + y)
# print("Sub:", x - y)
# print("Mul:", x * y)
# print("Div:", x / y)



# def add(x, y):
#     return x + y

# def mult(x, y):
#     return x * y

# def subtract(x, y):
#     return x - y

# def divide(x, y):
#     return x / y


# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# print("Subtraction:", subtract(x, y))
# print("Division:", divide(x, y))
# print("addition:", add(x, y))
# print("multiply:",mult(x, y) )


"""each operation = separate function
main code = input + print only
f-string = professional output style"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {multiply(x, y)}")
print(f"{x} / {y} = {divide(x, y):.2f}")

# manual 
print(add(10,5)) 