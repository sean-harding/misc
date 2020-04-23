from math import exp,sin

#Define functions and create function objects
def quadratic(A,B,C):
    return lambda x: A*x**2+B*x+C

def gauss(A,k):
    return lambda x: A*exp(-k*x**2)

Q = quadratic(3,4,5)
G = gauss(1,0.4)

#Arithmetic operations are supported out of the box
s = Q(2) + G(0.4)
print(s)

#Also supports arbitrary function arithmetic and nesting
def operation(f1,f2):
    return lambda x: f2(f1(x)) - 0.2*sin(f2(x)-f1(x))   #Define some bizzare function of functions to demonstrate
values = [operation(Q,G)(x) for x in [0.1,0.2,0.4,1,2]] #Evaluate for some arbitrary values

#We can also reduce arbitrary numbers, for example we can create the polynomial ax**n + bx**n-1 +  cx**n-2...

def poly(coeffs):
    #You could write this as an object for sure. Also we don't have to use sum to sum each element.
    #You could use the reduce function with an arbitrary function to piece together the terms
    #It is also pretty easy to
    return lambda x:sum(a*x**n for n,a in enumerate(coeffs))

a = poly((1,2,3,8)) #A cubic function
print(a(4))


#If we wanted to store base-exponent pairs as in your classes, it would be best to create a simple class
#It is not clear to me why this is particularly relevant however, as we will rarely be dealing with simple
#polynomials which in any case are easy to deal with. Otherwise, coefficients could be obtained using numerical
#differentiation and an expansion as a Taylor or Laurent series