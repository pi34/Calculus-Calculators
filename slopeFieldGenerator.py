import numpy as np
import matplotlib.pyplot as plt

xn = int(input("What is the power of x? "))
yn = int(input("what is the power of y? "))

operation = input("What is the operation between x and y? ")

print(operation)

def diffEq (x, y):
    if operation == "Addition":
        return x**xn + y**yn
    elif operation == "Subtraction":
        return x**xn - y**yn
    elif operation == "Multiplication":
        return x**xn * y**yn
    elif operation == "Division":
        return x**xn / y**yn
    

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)

for j in x:
    for k in y:
        dydx = diffEq(j, k)
        domain = np.linspace(j-0.05, j+0.05, 2)
        range = np.linspace(k-0.05, k+0.05, 2)
        def func(x1, y1):
            z = dydx * (domain-x1)+y1
            return z
        plt.plot(domain, func(j, k))

plt.show()
