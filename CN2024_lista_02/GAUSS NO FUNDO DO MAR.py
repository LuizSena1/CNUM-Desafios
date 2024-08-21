import numpy as np

def M(N): # Função que Cria Matrizes, 
    MATRIZ1 = [[float(input()) for _ in range(N)]  for _ in range(N)] # Cria a Matriz com N colunas e N linhas
    MATRIZ2 = [float(input()) for _ in range(N)] # Cria a Matriz con N linhas apenas.
    return MATRIZ1, MATRIZ2

def ElimGauss(A, B): # Eliminação de Gauss
    n = len(B)
    A, B = np.array(A, dtype=float), np.array(B, dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            fat = A[j, i] / A[i, i]
            A[j, i:], B[j] = A[j, i:] - fat * A[i, i:], B[j] - fat * B[i] # [j,i:]
    return A, B

def SR(A, B): # Substituição Retroativa
    n, X = len(B), np.zeros(len(B))
    for i in range(n - 1, -1, -1):
        X[i] = (B[i] - np.dot(A[i, i + 1:], X[i + 1:])) / A[i, i] # Calcula produto escalar e armazena no vetor.
    return X

N = int(input())
A, B = M(N)
A, B = ElimGauss(A, B)
print(f'Matriz Pivoteada de Coeficientes\n{A}')
print(f'Matriz Pivoteada de coeficientes independentes\n{B.reshape(-1,1)}') # Sem o Reshape, a matriz fica horizontal e não vertical ;-;
resp = np.linalg.solve(A, B).reshape((-1, 1))
print(f"Solução\n{resp}")