import numpy as np
from sympy import *
import math
init_printing()

z = Symbol('z',real=True)
A3 = Matrix([[1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,1,1],
			 [1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1],
			 [0,1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1],
			 [0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0],
			 [0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0],
			 [0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1],
			 [0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,0,1,1],
			 [0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0],
			 [0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,0,0],
		   	 [1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,1,0,0],
			 [1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0],
			 [1,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1],
			 [0,1,0,0,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1],
			 [0,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0],
			 [0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,0],
			 [1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1],
			 [1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,1],
			 [0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1],
			 [0,1,0,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0]])
			 
Az = Matrix([[1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,1,1],
			 [1,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1],
			 [0,1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1],
			 [0,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0],
			 [0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0],
			 [0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1],
			 [0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,0,1,1],
			 [0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0],
			 [0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,0,0],
		   	 [1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,1,0,0],
			 [1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0],
			 [1,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1],
			 [0,1,0,0,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1],
			 [0,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0],
			 [0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,0],
			 [1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1],
			 [1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,1],
			 [0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1],
			 [0,1,0,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0]])
		
#####Характеристический многочлен#####
def char_polynomial():
	E = eye(19)
	for i in range(19):
		for j in range(19):
			if Az[i,j] == 1:
				Az[i,j] = z
	return(expand(det(E - Az)))

#####Проверка на приводимость#####
def is_irreducible(characteristic_polynomial):
	Q = factor(characteristic_polynomial)
	if Q == characteristic_polynomial:
		return("Неприводим")
	else:
		return("Приводим")
	
	
W = np.array([[1, 1], [1, -1]],int)
#####Треугольник Паскаля#####
def anf(function):
    buff = []
    iterations = len(function)
    ANF = [ function[0] ]
    for _ in range(iterations-1):
        for i in range(len(function)-1):
            buff.append(function[i]^function[i+1])
        ANF.append(buff[0])
        function = buff
        buff = []
    return ANF

# Матрица Адамара
def hadamardMatrix(dimension):
    if dimension == 1:
        return W
    else:
        return np.hstack((np.vstack((hadamardMatrix(dimension-1),hadamardMatrix(dimension-1))),np.vstack((hadamardMatrix(dimension-1),-hadamardMatrix(dimension-1)))))

#####Список Уолш образов для функции#####
def walschSpectrum(function):
    unit_array = np.array([1 for _ in range(len(function))])
    M = hadamardMatrix(int(math.log2(len(function))))
    return np.matmul((unit_array - 2 * np.array(function)).T,M).tolist()

# Десятичное число в список из двоичных разрядов
def decimalToBinaryList(num, bites):
  zeros = []
  for i in range(bites):
          zeros.append((num >> i) & 1)  
  return zeros

#####Шаг в графе де Брейне#####
def step(pos,val,n):
        pos <<= 1
        pos += val
        pos &= (2 ** n) - 1
        return pos
###############################
######Проверка функции на наличие гамильтонова цикла на графе#####
def check(fun,n):
        start = 0
        chk = []
        for i in range(2 ** n):
                val = (fun >> start) & 1
                start = step(start,val,n)
                if bin(start + 2 ** n)[3:] in chk:
                        break
                chk.append(bin(start + 2 ** n)[3:])
        return chk
#####################################################################
###########Матрица смежности###########
def createMatrix(size):
    AdjacencyMatrix = [ [-1] * 2 ** (size-1)  for _ in range(2 ** (size-1))] 
    for i in range ( 2 ** (size -1) ):
        for j in range( 2 ** (size - 1) ):
            if (bin(j | 2**(size-1))[3:]  ==  bin(((i | 2**(size-1)) << 1) | 1 )[4:])  or  (bin(j | 2**(size-1))[3:]  ==  bin((i | 2**(size-1)) << 1)[4:]):
                AdjacencyMatrix[i][j] = (i<<1)  + (j%2)   
    return AdjacencyMatrix                                
##############Эйлеровы циклы ###############    
def EulerCycle(size):
    Matrix = createMatrix(size)
    Matrix[0][0] = -1
    S = [0]
    cycle=[] 
    count = True
    while  len(S) != 0 :
        w = S[len(S)-1]
        if Matrix[w//2][w] != -1: 
            S.append(w//2)
            Matrix[w//2][w] = -1
        elif Matrix[w//2 + 2 ** (size-2)][w] != -1:
            S.append(w//2 + 2 ** (size-2))
            Matrix[w//2 + 2 ** (size-2)][w] = -1
        if w ==  S[len(S)-1]:
            S.pop()
            cycle.append(w)
    return cycle 
   ##############Построение функций#################### 
def createFunction(cycle):
    rip,var,function = [],[],[]
    for i in range(len(cycle)-1):
        rip.append((cycle[i]<<1)+cycle[i+1]%2)
    rip.append(0)
    for i in range(len(rip)-1):
        var.append((rip[i]<<1) + (rip[i+1]%2))
    var.append((rip[len(rip)-1]<<1) + (rip[0]%2))
    for i in range (len(var)):
        for j in range(len(var)):
            if i == var[j]>>1:
                function.append(var[j]%2)
                break
    h = function[len(function)-1]
    for i in range((len(function)-1),-1,-1):
        h= (h << 1) + function[i]
    return h
f = open("an.txt","w")
# Функции де Брёйна от n переменных
def number(n,funCount,val=0):
        print("Найдено %d функций де Брейне от %d переменнных:" % (funCount, n),end="\n\n",file=f)
        num = 0
        for i in range(2 ** ( 2 ** (n - 1) )):
                if num == funCount:
                        break;
                val += (2 ** ( 2 ** (n - 1) )) - 1
                if len(check(val,n)) == 2 ** n:
                        print("Функция де Брейне №",num + 1,sep='',file=f)
                        num += 1
                        print("Вектор значений:",file=f)
                        print(bin(val + 2 ** 16)[3:],file=f)
                        print("Цикл вершин:",file=f)
                        print(*check(val,n),sep="-->",file=f)
                        print("Коэффициенты АНФ:",file=f) 
                        print(anf(decimalToBinaryList(val, 2**n)),file=f)
                        print("Коэффициенты Уолша-Адамара:",file=f)
                        print(walschSpectrum(decimalToBinaryList(val, 2**n)),end="\n\n",file=f)
			
			
			
characteristic_polynomial = char_polynomial()
print(characteristic_polynomial)
print(is_irreducible(characteristic_polynomial))
print("Задание №2:",file=f)
number(4,16)
val = createFunction(EulerCycle(10))
print("Задание №3:",file=f)
number(10,5,val)
f.close()
