import math

#Derivative Functions

def polynomialDerivative(degree):
    polynomial = {}
    for i in range(1, degree+1):
        var = float(input("Enter the coefficient for the variable with {} as the degree: ".format(i)))
        polynomial[i] = var
    string = ""
    funcstring = ""

    constant = float(input("Enter the constant of your function: "))

    for degree in polynomial:
        
        coefficient = degree * polynomial[degree]
        power = degree - 1

        funcCoeff = polynomial[degree]
        funcPower = degree

        if power != 0:
            string = "{}x^{} +".format(coefficient, power) + string 
            
        else:
            string = "{}".format(coefficient) + string

        if funcPower != 0:
            funcstring = "{}x^{} +".format(funcCoeff, funcPower) + funcstring
        
        else:
            funcstring = "{}".format(funcCoeff) + funcstring

    funcstring = funcstring + str(constant)
    return [string, funcstring]


def logDerEquation (base):
    logValue = math.log(base)
    string = "1 / {}x".format(logValue)
    return string

def trigDerEquation (a, f):
    if a==0:
        d="0"
    elif f.lower()=="sin(x)":
        d=str(a) + "cos(x)"
    elif f.lower()=="cos(x)":
        d=str(a*-1) + "sin(x)"
    elif f.lower()=="tan(x)":
        d= str(a) + "sec^2(x)" 
    elif f.lower()=="csc(x)":
        d=str(a*-1) + "csc(x)cot(x)"
    elif f.lower()=="sec(x)":
        d= str(a) + "sec(x)tan(x)"
    elif f.lower()=="cot(x)":
        d=str(a*-1) + "csc^2(x)"
    elif f.lower()=="arcsin(x)" or f.lower()=="asin(x)" or f.lower()=="sin^-1(x)":
        d= str(a) + "/" + "sqrt(1-x^2)"
    elif f.lower()=="arccos(x)" or f.lower()=="acos(x)" or f.lower()=="cos^-1(x)":
        d=str(a*-1) + "/" + "sqrt(1-x^2)"
    elif f.lower()=="arctan(x)" or f.lower()=="atan(x)" or f.lower()=="tan^-1(x)":
        d=str(a) + "/" + "(1+x^2)"
    elif f.lower()=="arccsc(x)" or f.lower()=="acsc(x)" or f.lower()=="csc^-1(x)":
        d= str(a*-1) + "/" + "(x)(sqrt(1-x^2))"
    elif f.lower()=="arcsec(x)" or f.lower()=="asec(x)" or f.lower()=="sec^-1(x)":
        d= str(a) + "/" + "(x)(sqrt(1-x^2))"
    elif f.lower()=="arccot(x)" or f.lower()=="acot(x)" or f.lower()=="cot^-1(x)":
        d= str(a*-1) + "/" + "1+x^2"
    return d

def powerDerEquation(a, n):
    c= a*n
    n2=n-1
    if n2>1 or (n2<1 and n2>0):
        d= str(c)+ "x^"+str(n2)
    elif n2==1:
        d= str(c) + "x"
    elif n2==0:
        d=str(c)
    elif n2<0:
        d=str(c) + "/" + "x^" + str(abs(n2)) 
    return d

def exponentDerEquation(a, n):
    ln= math.log (n, math.e)
    c= round(a*ln, 5)
    d=  "(" + str(c) + ")(" + str(round(n,2)) + "^x)"
    return d


# User Input

print("Welcome to the Derivatives Calculator!")

funcType = int(input("What type is your function? (Enter 0 for simple, 1 for compound): "))

if funcType is 0:
    func = input("What type is your function? Select one from logarithmic, polynomial, trigonometric, exponential, power: ")

    if func.lower()=="logarithmic":
        base = float(input("What is the base of the logarithm? "))
        d1 = logDerEquation (base)
        f1 = "log" + str(base) + "(x)" 
    elif func.lower()=="polynomial":
        degree = int(input("What is the degree of the polynomial? "))
        d1= polynomialDerivative (degree) [0]
    elif func.lower()=="exponential":
        print("After converting your function to the form f(x)=an^x, please input the vales of a and n below: ")
        a= float(input("a: "))
        n= float(input("n: "))
        d1= exponentDerEquation (a, n)
        f1= "(" + str(a) + ")(" + str(n) + "^x)"
    elif func.lower()=="trigonometric":
        print("After Converting your function to the form (a)(t(x)) (where t is some trigonometric function), please enter the relevant infromation below:")
        a= float(input("a: "))
        f= input("f(x)= ")
        d1= trigDerEquation(a, f)
        f1= str(a) + f
    elif func.lower()== "power":
        print("After Converting you function to the form ax^n, please input the values of x and n below:")
        a= float(input("a: "))
        n= float(input("n: "))
        d1= powerDerEquation(a, n)
        f1= "(" + str(a) + ")(x^" + str(n) + ")"
    else:
        print("Invalid Function Type.")

    print("Derivative =", d1)

elif funcType is 1:
    Fxt= input("Please input the function type of your first Function (Select one from logarithmic, polynomial, trigonometric, exponential, power): ")
    if Fxt.lower()=="logarithmic":
        base = float(input("What is the base of the logarithm? "))
        d1 = logDerEquation (base)
        f1 = "log" + str(base) + "(x)" 
    if Fxt.lower()=="polynomial":
        degree = int(input("What is the degree of the polynomial? "))
        pol = polynomialDerivative (degree)
        d1= pol [0]
        f1 = pol [1]
    if Fxt.lower()=="exponential":
        print("After converting your function to the form f(x)=an^x, please input the vales of a and n below: ")
        a= float(input("a: "))
        n= float(input("n: "))
        d1= exponentDerEquation (a, n)
        f1= "(" + str(a) + ")(" + str(n) + "^x)"
    if Fxt.lower()=="trigonometric":
        print("After Converting your function to the form (a)(t(x)) (where t is some trigonometric function), please enter the relevant infromation below:")
        a= float(input("a: "))
        f= input("f(x)= ")
        d1= trigDerEquation (a, f)
        f1= str(a) + f
    if Fxt.lower()== "power":
        print("After Converting you function to the form ax^n, please input the values of x and n below:")
        a= float(input("a: "))
        n= float(input("n: "))
        d1= powerDerEquation(a, n)
        f1= "(" + str(a) + ")(x^" + str(n) + ")"

    Gxt= input("Please input the function type of your second Function (Select one from logarithmic, polynomial, trigonometric, exponential, power): ")
    if Gxt.lower()=="logarithmic":
        base = float(input("What is the base of the logarithm? "))
        d2 = logDerEquation (base)
        g1= "log" + str(base) + "(x)"
    if Gxt.lower()=="polynomial":
        degree = int(input("What is the degree of the polynomial? "))
        pol = polynomialDerivative (degree)
        d2= pol [0]
        g1 = pol [1]
    if Gxt.lower()=="exponential":
        print("After converting your function to the form f(x)=an^x, please input the vales of a and n below: ")
        a= float(input("a: "))
        n= float(input("n: "))
        d2= exponentDerEquation (a, n)
        g1= "(" + str(a) + ")(" + str(n) + "^x)"
    if Gxt.lower()=="trigonometric":
        print("After Converting your function to the form (a)(t(x)) (where t is some trigonometric function), please enter the relevant infromation below:")
        a= float(input("a: "))
        f= input("f(x)= ")
        d2= trigDerEquation (a, f)
        g1= str(a) + f
    if Gxt.lower()== "power":
        print("After Converting you function to the form ax^n, please input the values of x and n below:")
        a= float(input("a: "))
        n= float(input("n: "))
        d2= powerDerEquation(a, n)
        g1= "(" + str(a) + ")(x^" + str(n) + ")"

    Op= input("Please input the operation between the two functions: ")
    if Op.lower()=="subraction":
        d= "(" + d1 + ")" + " - " + "(" + d2 + ")"
    if Op.lower()=="addition":
        d= "(" + d1 + ")" + " + " + "(" + d2 + ")"
    if Op.lower()=="multiplication":
        d= "(" + d1 + ")(" + g1 + ") + (" + d2 + ")(" + f1 + ")"
    if Op.lower()=="division":
        d= "((" + d1 + ")(" + g1 + ") - (" + f1 + ")(" + d2 + "))/(" + g1 + ")^2"

    print("Derivative: " + d)

else:
    print("Invalid Function Type.")

print("Thank you for Using The Python Derivative Calculator!")
