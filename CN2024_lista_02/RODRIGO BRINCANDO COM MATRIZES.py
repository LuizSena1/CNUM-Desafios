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

def Flu(MATRIZ):
    ML = np.eye(N)
    MU = np.zeros((N,N)) 
    for k in range(N):
        if np.linalg.det(MATRIZ[:k+1, :k+1]) == 0:
            print("Não é possível realizar a fatoração LU nessa matriz pois não admite inversa")
            return None, None
        for j in range(k, N):
            MU[k, j] = MATRIZ[k, j] - sum(ML[k, m] * MU[m, j] for m in range(k))
        for i in range(k+1, N):
            ML[i, k] = (MATRIZ[i, k] - sum(ML[i, m] * MU[m, k] for m in range(k))) / MU[k, k]
    return ML, MU

def Res(L, U, VCOLUNA):
    y = np.zeros(N)
    for i in range(N):
        y[i] = (VCOLUNA[i] - sum(L[i, j] * y[j] for j in range(i))) / L[i, i]

    solu = np.zeros(N)
    for i in range(N-1, -1, -1):
        solu[i] = (y[i] - sum(U[i, j] * solu[j] for j in range(i+1, N))) / U[i, i]

    return solu.reshape(-1, 1)

N = int(input())
MATRIZ = Matriz(N)
VCOLUNA = VColuna(N)
ML, MU = Flu(MATRIZ)
if ML is not None:
    solu = Res(ML, MU, VCOLUNA)
    print(f'Matriz L:\n{ML}\nMatriz U:\n{MU}\nSolução do sistema:\n{solu}')