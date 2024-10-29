# Input asks for an expression in 'x, y, z' format. Sets the value for x & z as numbers, y is set as '+, -, *, or /'
x, y, z = input("Expression: ").strip().split()

# Converts x and y input into a decimal / fractional value.
x = float(x)
z = float(z)

# if statement determines if the function adds, subtracts, multiplies, or divides based on which symbol is used in y.
if (y == "+"):
    print(x + z)
elif (y == "-"):
    print(x - z)
elif(y == "*"):
    print(x * z)
elif(y == "/"):
    print(x / z)
