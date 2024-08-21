# F(x) = Ax**2 + B*x + C
# Precisão 0.01
def f(x,Coeficiente): #Função dada
    A,B,C = Coeficiente
    return A*x**2 + B*x + C
VALOR = []
INTERVAL = []
i  = 0
while i < 3:
    nu = float(input())
    VALOR.append(nu)
    i+=1
INTERVAL1 = float(input())
INTERVAL2 = float(input())
PRECI = 0.01
def metd(Valor,x,y,P): # O metodo da Bisseção.
    fx = f(x,Valor)
    fy = f(y,Valor)
    if f(x,Valor)*f(y,Valor) > 0:
        return 'Raiz não encontrada' # Retorna mensagem caso raiz não seja encontrada.
    while abs(y - x)/2 > P: 
        z = (x + y) / 2
        fz = f(z,Valor)
        if f(x,Valor) * fz < 0:
            y = z
        else:
            x = z
        if abs(fz) < P:
            return z
    return (x+y)/2
resul = metd(VALOR,INTERVAL1,INTERVAL2,PRECI)
if isinstance(resul,str): # filtra a mensagem de erro, ja que so ela e texto.
    print(resul)
else:
    print(f'Raiz aproximada = {resul}')
    