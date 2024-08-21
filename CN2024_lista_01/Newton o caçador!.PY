# F(x) = x**3 - 6*x**2 + 11*x -  6
# Precisão : 10^-4(1e-4)
def f(x): # Primeira Função
    return x**3 - 6*x**2 + 11*x -  6
def df(x): # Derivada da primeira função
    return 3*x**2 - 12*x + 11
def Newt(f,df,x,p): # Metodo de Newton
    vn = 0
    pn = 0
    i = 0
    while abs(vn-x) >= p: # Criterio de Parada, |Xn+1 - Xn| < Precisão. 
        vn = x
        xn = vn-(f(vn)/df(vn))
        x = xn
        i+=1
    return xn,i
x = float(input())
PRECI = 1e-4
ITERA = 0
RAIZ, ITERA = Newt(f,df,x,PRECI)
print(f'Raiz perdida está em : {round(RAIZ,1)}, iterações necessárias: {ITERA}') 
# Foi arredondado a solução.
