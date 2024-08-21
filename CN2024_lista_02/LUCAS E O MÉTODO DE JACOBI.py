import numpy as np
# Iteração = 100
# Erro Minimo = 1e-10
# Erro Maximo = 1e-4

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
    
def Jacobi(Matriz,vetc):
    itemax=100
    erromin = 1e-10
    erromax = 1e+4
    vetorsolu=np.zeros(N)
    for k in range(1,itemax +1):
        vetorsolup = np.copy(vetorsolu)
        i = 0
        for i in range(N):
            vetorsolu[i]=(vetc[i]-(np.dot(Matriz[i,:i],vetorsolup[:i])+np.dot(Matriz[i,i+1:],vetorsolup[i+1:])))/Matriz[i,i]
            i+=1
        erro = np.sqrt(np.sum((1-vetorsolu)**2))
        if erromin > erro:
            print(f"Jacobi: {vetorsolu}") 
            print(f"Jacobi: {k} iterações\n")
            return vetorsolu,k
        elif erromax < erro:
            print("O método de Jacobi não convergiu!")
            return k
            
        k += 1

N = int(input())
Matriz = Matriz(N)
vetc = VColuna(N)
RESPOSTA=Jacobi(Matriz,vetc)