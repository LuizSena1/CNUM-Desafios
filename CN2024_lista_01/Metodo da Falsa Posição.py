import math
def f(x):
    return 2*math.log(x**2)
def pos(a,b):
    i = 0
    if (f(b)*f(a))< 0:
        for i in range(5):
            i +=1
            z = (a*f(b)-b*f(a))/(f(b)-f(a))
            print(f'Iteração {i}: Z = {round(z,4)},F(z) = {round(f(z),4)}')
            if (f(a)*f(z)) > 0:
                a = z
                print(f'F(a)*F(z) > 0')
            else:
                b = z
                print(f'F(a)*F(z) < 0')
        return z
    
a = float(input())
b = float(input())
raiz = pos(a,b)
print(f'A Raiz e = {round(raiz,4)}')