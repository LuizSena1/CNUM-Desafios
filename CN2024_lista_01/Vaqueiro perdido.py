# Função- x^2 + ln(x)
# Metodo: Secante
# 5 casas decimais
TOL = 1e-5  
import math # Preciso para o Ln(x)
def f(x): # Função
    return x**2 + math.log(x)

def sec(a,b,t): # A = xn-1; B = xn
    it = 1
    for i in range(90):
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        if abs(c-b) <= t:
            break
        if abs(f(b)) <= t:
            break
        a = b
        b = c
        it += 1
    return b, it
a = float(input())
b = float(input())
BOI, TENTATIVA = sec(a,b,TOL)
print(f'Oh, o boi lá na posição misteriosa: {round(BOI,5)}')
print(f'O vaqueiro precisou realizar {TENTATIVA} tentativas para pegar o boi perdido na caatinga.')
