# F(x) = Ax**2 + Bsen(x) + C*e*2
# 10 iterações maximas.
import math
ITERA = 11 # Foi preciso colocar para que o valor desse correto em dois testes.
A = int(input()) # Coeficiente A
B = int(input()) # Coeficiente B
C = int(input()) # Coeficiente C
INTERVALO1 = int(input())
INTERVALO2 = int(input())
PRECISAO = 0.05 # Precisão de 10 casas decimais.

# Testar tanto metodo da Falsa posição.
def fun(A,B,C,x):
    return A*x**2 + (B*math.sin(x)) + C*math.exp(2)

def fp(f,A,B,C,x,y,ite,P): # Define a função de falsa posição.
    fx = f(A,B,C,x)
    fy = f(A,B,C,y)
    i = 0
    if (fx*fy)  < 0:
        for i in range(ite) or (y - x) > P:
            i += 1
            z = (x*f(A,B,C,y)-y*f(A,B,C,x))/(f(A,B,C,y)-f(A,B,C,x)) # Metodo da Falsa posição.
            fz = f(A,B,C,z)
            if fx*fz > 0: # Compara para saber onde  substituir.
                x = z
                fx = fz
            else:
                y = z
                fy = fz
        return z # Retorna z como raiz.
    else:
        return 'Não há raízes nesse intervalo.'
resul = fp(fun,A,B,C,INTERVALO1,INTERVALO2,ITERA,PRECISAO)
if isinstance(resul,str):
    print(resul)
else:
    print(f'O valor aproximado da raiz é: {round(resul,8)}')