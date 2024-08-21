# F(x) = Ax**2+bx+c
# 5 iterações maximas.
ITERA = 5
A = int(input()) # Coeficiente A
B = int(input()) # Coeficiente B
C = int(input()) # Coeficiente C
INTERVALO1 = int(input())
INTERVALO2 = int(input())
RAIZR = int(input()) # Raiz real.
PRECISAO = 1e-10 # Precisão de 10 casas decimais.

# Testar tanto metodo da Falsa posição, e Metodo interativo Linear Começando com Falsa Posição.
def fun(A,B,C,x):
    return A*x**2 + B*x + C
def gf(A,B,C,x):
    return (-C)/(A*x+ B)

def fp(f,A,B,C,x,y,ite,P): # Define a função de falsa posição.
    i=0
    fx = f(A,B,C,x)
    fy = f(A,B,C,y)
    for i in range(ite):
        i += 1
        z = (x*f(A,B,C,y) - y*f(A,B,C,x))/(f(A,B,C,y)-f(A,B,C,x)) # Metodo da Falsa posição.
        fz = f(A,B,C,z)
        if fx*fz > 0: # Compara para saber onde  substituir.
            x = z
        else:
            y = z
    return z # Retorna z como raiz.

def MIL(f,A,B,C,x,y,ite,P): # Define a função do Metodo Iterativo Linear(Ponto Fixo)
    x0 = (x + y) / 2 # Faz com que o x0 esteja dentro do intervalo fornecido.
    for i in range(ite): # Faz as iterações.
        x1 = gf(A,B,C,x0)
        x0 = x1
    return x1 # Retorna x1 como raiz.
resul = MIL(fun,A,B,C,INTERVALO1,INTERVALO2,ITERA,PRECISAO)
COMP = abs(resul - RAIZR)
print(f'Realmente Igor tinha razão! Ganhou o método MIL com uma discrepância de {round(COMP, 12)}')  # Round foi usado no lugar de z
# Round foi usado no lugar de :.10f porque o codigo não iria arredondar quando resultado fosse 0.