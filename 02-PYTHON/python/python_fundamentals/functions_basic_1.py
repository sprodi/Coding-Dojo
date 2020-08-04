# # 1
def a():
    return 5
print(a())

# # PREDICTION: 5
# # OUTPUT: 5

# #2
def a():
    return 5
print(a()+a())

# # PREDICTION: 10
# # OUTPUT: 10

#3
def a():
    return 5
    return 10
print(a())

# PREDICTION: 5 10
# OUTPUT: 5 WHY: once it hits the first return, it ends the function.

#4
def a():
    return 5
    print(10)
print(a())
# PREDICTION: 5
# OUTPUT: 5

#5
def a():
    print(5)
x = a()
print(x)
# PREDICTION: 5, 5
# OUTPUT: 5

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# PREDICTION: 8
# OUTPUT: 3, 5, TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# PREDICTION: "25"
# OUTPUT: 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# PREDICTION: 100
# OUTPUT: SyntaxError: invalid character in identifier 'else:'

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# PREDICTION: 7, 14, 21   (7 + 14)
# OUTPUT: 7, 14, 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# PREDICTION: 8
# OUTPUT: 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# PREDICTION: 500, 500, 300, 500
# OUTPUT: 500, 500, 300, 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# PREDICTION: 500, 500, 300, 300
# OUTPUT: 500, 500, 300, 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# PREDICTION: 500, 500, 300, 300
# OUTPUT: 500, 500, 300, 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# PREDICTION: 1, 3, 2
# OUTPUT: 1 ,3 ,2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# PREDICTION: 1, 3, 5, 10
# OUTPUT: 1, 3, 5, 10