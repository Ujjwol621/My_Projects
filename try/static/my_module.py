#Horner's Method
def horner(poly,n,x):
    result=poly[0]
    for i in range(1,n):
        result=result*x+poly[i]
    return result
poly=[1,-3,4,0,-8]
x=2
n=len(poly)
function_value=horner(poly,n,x)
print("The function value of given polynomial is ",function_value)

#Bisection Method
import math

def bisection(f, a, b, e):
    if f(a) * f(b) >= 0:
        print("The bisection method cannot be applied.")
        return None
    
    N = math.ceil(math.log((b - a) / e) / math.log(2))
    print("Number of iterations is:", N)
    
    for _ in range(N):
        c = (a + b) / 2
        if abs(f(c)) < e or abs(b - a) / 2 < e:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

f = lambda x: x**2 - 4 * x - 10
a, b = 5, 6
e = 0.01
root = bisection(f, a, b, e)
print("The root is:", round(root,2))

    