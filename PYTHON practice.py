X = input("Enter your first number : ")
operator = input("Enter your operator (+,-,/,*,%) : ")
Y = input("Enter your second number : ")

X = int(X)
Y = int(Y)

if operator == "+" :
    print(X+Y)
elif operator == "-" :
    print(X-Y)
elif operator == "/" :
    print(X/Y)
elif operator == "*" :
    print(X*Y)
elif operator == "%" :
    print(X%Y)
else:
    print("invalid operations")