# Iteração maxima = 100
# Erro = 1e-10

import numpy as np

def Matriz(N):
    i = 0
    val = []
    for i in range(N):
        j = 0
        val_linha = []
        for j in range(N):
            el = float(input())
            val_linha.append(el)
            j+=1
        val.append(val_linha)
        i+=1
    Matriz=np.array(val)
    return Matriz

def VColuna(N):
    c = []
    i = 0
    for i in range(N):
        e = float(input())
        c.append([e])
        i += 1
    VColuna=np.array(c)
    return VColuna

def Gauss(Matriz, vcoluna):
    n = len(Matriz)
    vsolu = np.zeros(n)
    ITMAX = 100
    ERRO = 1e-10
    
    for k in range(1, ITMAX + 1):
        vsoluant = np.copy(vsolu)
        for i in range(n):
            soma1 = np.dot(Matriz[i, :i], vsolu[:i])
            soma2 = np.dot(Matriz[i, i+1:], vsoluant[i+1:])
            vsolu[i] = (vcoluna[i] - soma1 - soma2) / Matriz[i, i]
        
        erro = np.sqrt(np.sum((1 - vsolu) ** 2))
        if erro < ERRO:
            break

    return vsolu, k


N = int(input())
Matriz = Matriz(N)
vcoluna = VColuna(N)
    
VSOLU, ITERA = Gauss(Matriz, vcoluna)

print("Vetor solução é:")
print(VSOLU.reshape(-1, 1)) # Reshape pra manter a Matriz organizada Verticalmente.

if ITERA % 2 == 0: # Serve apenas para descobrir se o valor foi Par ou Impar pelo resto da divisão.
    print(f"Com {ITERA} interações, a raposa foi cativada pois é um numero par")
else:
    print(f"Com {ITERA} interações, a raposa não foi cativada pois é um numero ímpar")
