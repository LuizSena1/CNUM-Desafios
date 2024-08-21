import math
def f(x):
    return math.cos(x) + math.log(x) + x
TOL = 1e-3
def bis(a,b,t):
    i = 0
    for i in range(100):
        i += 1
        c = (a+b)/2
        print(f'Valores na iteração {i}: C = {round(c,4)}, A = {round(a,4)}, B = {round(b,4)}, F(c) = {round(f(c),4)}')
        if abs(f(c)) <= t:
            break
        n = f(a)*f(c)
        if f(c)*f(a) > 0:
            a = c
            print(f'F(a)*F(c) > 0\n')
        else:
            b = c
            print(f'F(a)*F(c) < 0\n')
        # print(f'Apos Iteração {i}: A = {round(a,4)}, B = {round(b,4)}, C = {round(c,4)}\n')
    return c,i
Fazer = input(f'1 PARA FUNÇÃO, 2 PARA BISSEÇÃO: ')
Fazer=int(Fazer)
if Fazer == 1:
    x = float(input())
    print(round(f(x),4))
else:
    A = float(input())
    B = float(input())       
    raiz,interaveis = bis(A,B,TOL)
    print(f'Raiz = {round(raiz,4)}, Interaveis = {interaveis}')
