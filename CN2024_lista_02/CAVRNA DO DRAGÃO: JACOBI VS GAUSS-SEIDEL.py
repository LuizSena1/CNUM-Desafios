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
            j += 1
        val.append(val_linha)
        i += 1
    Matriz = np.array(val)
    return Matriz

def VColuna(N):
    c = []
    i = 0
    for i in range(N):
        e = float(input())
        c.append([e])
        i += 1
    VColuna = np.array(c)
    return VColuna

def Gauss(Matriz,VColuna):
    vetorsolu = np.zeros(N)
    for k in range(1,ITEMAX + 1):
        vetorsolup = np.copy(vetorsolu)
        i = 0
        for i in range(N):
            vetorsolu[i] = (VColuna[i]-(np.dot(Matriz[i,:i],vetorsolu[:i])+np.dot(Matriz[i,i+1:],vetorsolup[i+1:])))/Matriz[i, i]
            i += 1
        erro = np.sqrt(np.sum((1-vetorsolu)**2))
        if erro < ERROMIN:
            print(f"Gauss-Seidel: {vetorsolu}")
            print(f"Gauss-Seidel: {k} iterações")
            return vetorsolu,k
        elif erro > ERROMAX:
            print("O método de Gauss-Seidel não convergiu!")
            return k
        k += 1

def Jacobi(Matriz,VColuna):
    vetorsolu = np.zeros(N)
    for k in range(1,ITEMAX + 1):
        vetorsolup = np.copy(vetorsolu)
        i = 0
        for i in range(N):
            vetorsolu[i]=(VColuna[i]-(np.dot(Matriz[i,:i],vetorsolup[:i])+np.dot(Matriz[i,i+1:],vetorsolup[i+1:])))/Matriz[i,i]
            i += 1
        erro = np.sqrt(np.sum((1-vetorsolu)**2))
        if ERROMIN > erro:
            print(f"Jacobi: {vetorsolu}") 
            print(f"Jacobi: {k} iterações\n")
            return vetorsolu,k
        elif ERROMAX < erro:
            print("O método de Jacobi não convergiu!")
            return k
            
        k += 1

ITEMAX = 100
ERROMAX = 1e+4
ERROMIN = 1e-10
N = int(input())
Matriz = Matriz(N)
VColuna = VColuna(N)
gauss = Gauss(Matriz,VColuna)
jacobi = Jacobi(Matriz,VColuna)