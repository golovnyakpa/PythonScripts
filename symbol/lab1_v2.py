import math
import numpy as np
W = np.array([[1, 1], [1, -1]],int)
V = np.array([[1, 0], [-1, 1]],int)
combinations = []
FI = []
S7 = (
     54, 50, 62, 56, 22, 34, 94, 96, 38,  6, 63, 93, 2,  18,123, 33,
     55,113, 39,114, 21, 67, 65, 12, 47, 73, 46, 27, 25,111,124, 81,
     53,  9,121, 79, 52, 60, 58, 48,101,127, 40,120,104, 70, 71, 43,
     20,122, 72, 61, 23,109, 13,100, 77,  1, 16,  7, 82, 10,105, 98,
    117,116, 76, 11, 89,106,  0,125,118, 99, 86, 69, 30, 57,126, 87,
    112, 51, 17,  5, 95, 14, 90, 84, 91,  8, 35,103, 32, 97, 28, 66,
    102, 31, 26, 45, 75,  4, 85, 92, 37, 74, 80, 49, 68, 29,115, 44,
     64,107,108, 24,110, 83, 36, 78, 42, 19, 15, 41, 88,119, 59,  3,
)

S9 = (    
    167,239,161,379,391,334,  9,338, 38,226, 48,358,452,385, 90,397,
    183,253,147,331,415,340, 51,362,306,500,262, 82,216,159,356,177,
    175,241,489, 37,206, 17,  0,333, 44,254,378, 58,143,220, 81,400,
     95,  3,315,245, 54,235,218,405,472,264,172,494,371,290,399, 76,
    165,197,395,121,257,480,423,212,240, 28,462,176,406,507,288,223,
    501,407,249,265, 89,186,221,428,164, 74,440,196,458,421,350,163,
    232,158,134,354, 13,250,491,142,191, 69,193,425,152,227,366,135,
    344,300,276,242,437,320,113,278, 11,243, 87,317, 36, 93,496, 27,
    487,446,482, 41, 68,156,457,131,326,403,339, 20, 39,115,442,124,
    475,384,508, 53,112,170,479,151,126,169, 73,268,279,321,168,364,
    363,292, 46,499,393,327,324, 24,456,267,157,460,488,426,309,229,
    439,506,208,271,349,401,434,236, 16,209,359, 52, 56,120,199,277,
    465,416,252,287,246,  6, 83,305,420,345,153,502, 65, 61,244,282,
    173,222,418, 67,386,368,261,101,476,291,195,430, 49, 79,166,330,
    280,383,373,128,382,408,155,495,367,388,274,107,459,417, 62,454,
    132,225,203,316,234, 14,301, 91,503,286,424,211,347,307,140,374,
     35,103,125,427, 19,214,453,146,498,314,444,230,256,329,198,285,
     50,116, 78,410, 10,205,510,171,231, 45,139,467, 29, 86,505, 32,
     72, 26,342,150,313,490,431,238,411,325,149,473, 40,119,174,355,
    185,233,389, 71,448,273,372, 55,110,178,322, 12,469,392,369,190,
      1,109,375,137,181, 88, 75,308,260,484, 98,272,370,275,412,111,
    336,318,  4,504,492,259,304, 77,337,435, 21,357,303,332,483, 18,
     47, 85, 25,497,474,289,100,269,296,478,270,106, 31,104,433, 84,
    414,486,394, 96, 99,154,511,148,413,361,409,255,162,215,302,201,
    266,351,343,144,441,365,108,298,251, 34,182,509,138,210,335,133,
    311,352,328,141,396,346,123,319,450,281,429,228,443,481, 92,404,
    485,422,248,297, 23,213,130,466, 22,217,283, 70,294,360,419,127,
    312,377,  7,468,194,  2,117,295,463,258,224,447,247,187, 80,398,
    284,353,105,390,299,471,470,184, 57,200,348, 63,204,188, 33,451,
     97, 30,310,219, 94,160,129,493, 64,179,263,102,189,207,114,402,
    438,477,387,122,192, 42,381,  5,145,118,180,449,293,323,136,380,
     43, 66, 60,455,341,445,202,432,  8,237, 15,376,436,464, 59,461,
)
test_function2 = (2,2,0,1)
test_function = (0, 0, 0, 1, 0, 1, 1, 1)
#####Вес разрядных функций#####
def weight(function):
    input_size = len(bin(max(function))[2:])
    #print(input_size)
    weights = [0 for _ in range(input_size)]
    for numbers in range(len(function)):
        for functions in range(len(weights)):
            weights[functions] = weights[functions] + (function[numbers] >> functions & 1)
    return weights
###############################
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
#############################
#####Число мономов у функций в отдельности#####
def monomeNumber(function):
    input_size = len(bin(max(function))[2:])
    #print(len(function))
    ANF = anf(function)
    buff = []
    monome_number = []
    for functions in range(input_size):
        for i in range(len(ANF)):
            buff.append(ANF[i] >> functions & 1)
        monome_number.append(sum(buff))
        buff = []
    return monome_number
#################################
#####Общее число различных мономов#####
def combinedMonomeNumber(function):
    ANF = anf(function)
    counter = 0
    for item in ANF:
        if item != 0:
            counter += 1
    return counter
#######################################
#####Матрица Адамара-Сильвестра#####
def hadamardMatrix(dimension):
    if dimension == 1:
        return W
    else:
        return np.hstack((np.vstack((hadamardMatrix(dimension-1),hadamardMatrix(dimension-1))),np.vstack((hadamardMatrix(dimension-1),-hadamardMatrix(dimension-1)))))
####################################
#####Получение массива значений функций#####
def functionValue(function):
    values = [ [] for _ in range(len(bin(max(function))[2:]))]
    for value in function:
        for function_number in range(len(bin(max(function))[2:])):
            values[function_number].append(value >> function_number & 1)
    return values
###################################################
#####Генерирует все мономы в лексикографическом порядке#####
def generateMonoms(n):
	monoms = ['1']
	x = 1
	for i in range(2 ** n - 1):
		mon = ''
		for j in range(n):
			if x >> j & 1:
				mon += 'x' + str(j)
		monoms.append(mon)
		x += 1
	return(monoms)
############################################################
#####Вывод значений функции в нормальном виде#####
def buildSFunction(function):
    answer = ''
    num_of_bits = len(bin(max(function))[2:])
    monoms = generateMonoms(num_of_bits)
    print_yi = "y{}"
    counter = 0
    for i in range(num_of_bits):
        answer += print_yi.format(counter) + ' = '
        coefficients = functionValue(anf(function))[i]
        for j in range(len(function)):
            if coefficients[j]:
                answer += monoms[j] + ' ⊕ '
        counter += 1
        answer = answer[0:len(answer) - 3:]
        answer += '\n'
    return(answer)
##################################################
#####Список Фурье образов для всех разрядных функций#####
def fourierSpectrum(function):
    values = functionValue(function)
    spectrum = []
    M = hadamardMatrix(int(math.log2(len(function))))
    for functions in range(len(bin(max(function))[2:])):
        spectrum.append(np.matmul(np.array(values[functions]).T,M).tolist())
    return spectrum
#########################################################
#####Список Уолш образов для всех разрядных функций#####
def walschSpectrum(function):
    values = functionValue(function)
    unit_array = np.array([1 for _ in range(len(function))])
    M = hadamardMatrix(int(math.log2(len(function))))
    spectrum = []
    for functions in range(len(bin(max(function))[2:])):
        spectrum.append(np.matmul((unit_array - 2 * np.array(values[functions])).T,M).tolist())
    return spectrum
#########################################################
#####Вывод вероятности #####
def printProbability(function):
    spectrum = fourierSpectrum(function)
    values = len(bin(max(function))[2:])
    for i in range(values):
        print("By function y%d:" % i)
        for j in range(len(spectrum[i])):
            a = (0.5 - spectrum[i][j]/(len(function)))
            print("Probability P(f(x) =%d* x) = %f - f(%d)" % (j,a,j))
############################
#####Матрица дейстивтельного многочлена#####
def realMatrix(dimension):
    if dimension == 1:
        return V
    else:
        return np.hstack((np.vstack((realMatrix(dimension-1),-realMatrix(dimension-1))),np.vstack((np.zeros((2**(dimension-1),2**(dimension-1)),dtype=int),realMatrix(dimension-1)))))
############################################
#####Список коэффициентов действительного многочлена#####
def realSpectrum(function):
    values = functionValue(function)
    M = realMatrix(int(math.log2(len(function))))
    spectrum = []
    for functions in range(len(bin(max(function))[2:])):
        spectrum.append(np.matmul(M,np.array(values[functions])[np.newaxis].T).T[0].tolist())
    return spectrum
#########################################################
#####Степень действительного многочлена#####
def realSpectrumDegree(function):
	spectrum = realSpectrum(function)
	monom_degree = 0
	max_degree = [0 for _ in range(len(bin(max(function))[2:]))]
	for i in range(len(function)):
		for j in range(len(bin(max(function))[2:])):
			if spectrum[j][i] != 0:
				for k in range(int(math.log2(len(function)))):
					if (i >> k & 1):
						monom_degree += 1
				if monom_degree > max_degree[j]:
					max_degree[j] = monom_degree
			monom_degree = 0
	return max_degree
############################################
#####Количество мономов в действительных многочленах#####
def realSpectrumPolinomsNum(function):
	spectrum = realSpectrum(function)
	monoms_num = [0 for _ in range(len(bin(max(function))[2:]))]
	for i in range(len(bin(max(function))[2:])): 
		for j in range(len(function)):
			if spectrum[i][j] != 0:
				monoms_num[i] += 1
	return monoms_num
#########################################################
#####Линейная комбинация функций#####
def linearCombination(function):
    function_values = functionValue(function)
    linearCombinations = []
    buff = np.zeros(len(function),dtype = int)
    for i in range(len(function)):
        for j in range(len(bin(max(function))[2:])):
            buff += (i >> j & 1)*np.array(function_values[j])
        #print(buff)
        linearCombinations.append(np.remainder(buff,2).tolist())
        buff = np.zeros(len(function),dtype = int)
    buff = 0
    for i in range(len(linearCombinations[0])):
        for j in range(len(linearCombinations)):
            buff += (2 ** j) * linearCombinations[j][i]
        combinations.append(buff)
        buff = 0
    return linearCombinations,combinations
#####################################
#####Разностная характеристика#####
def subCharacteristics(function):
    input_size = len(bin(max(function))[2:])
    max_list = []
    for a in range(2 ** input_size):
        for b in range(2 ** input_size):
            x_number = 0
            for x in range(2 ** input_size):
                if function[x ^ a] ^ function[x] == (b):
                    x_number +=1
            max_list.append(x_number)
    print("Таблица разностных характеристик:")        
    return max_list
###################################
#####Функция FI#####
def funFI(input, round_key):
        # assert _bitlen(input)  <= 16
        
        left  = input >> 7
        right = input & 0b1111111

        round_key_1 = round_key >> 9
        round_key_2 = round_key & 0b111111111

        tmp_l = right
        # assert _bitlen(left)  <= 9
        tmp_r = S9[left] ^ right

        left  = tmp_r ^ round_key_2
        # assert _bitlen(tmp_l) <= 7
        right = S7[tmp_l] ^ (tmp_r & 0b1111111) ^ round_key_1

        tmp_l = right
        # assert _bitlen(left)  <= 9
        tmp_r = S9[left] ^ right

        # assert _bitlen(tmp_l) <= 7
        left  = S7[tmp_l] ^ (tmp_r & 0b1111111)
        right = tmp_r

        # assert _bitlen(left)  <= 7
        # assert _bitlen(right) <= 9
        return (left << 9) | right

#####Записывает значения функций FI  в нужной форме#####
def funFIConvert(round_key):
    for i in range(2 ** 17):
        FI.append(funFI(i,round_key))
########################################################
norm, used = linearCombination(S7)
mass = weight(used)
fourier = fourierSpectrum(used)
walsh = walschSpectrum(used)
ANF = anf(used)
real = realSpectrum(used)
degree = realSpectrumDegree(used)
num = realSpectrumPolinomsNum(used)
for i in range(128):
        print("Коэффициенты при разрядных функциях слева направо",bin(i+128)[3:])
        print("Значение получившейся линейной комбинации")
        print(norm[i])
        print("Вес")
        print(mass[i])
        print("Число мономов для многочлена Жегалкина")
        print(len(ANF))
        print("Коэффициенты Фурье")
        print(fourier[i])
        print("Коэффициенты Адамара-Уолша")
        print(walsh[i])
        print("Действительный многочлен")
        print(real[i])
        print("Степень действительного многочлена")
        print(degree[i])
        print("Число мономов")
        print(num[i])
print("Список линейных аналогов и соответствующих вероятностей совпадения разрядной функции с линейной")
print(printProbability(used))
