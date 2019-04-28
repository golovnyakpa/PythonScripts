import math
import numpy as np

W = np.array([[1, 1], [1, -1]], int)
V = np.array([[1, 0], [-1, 1]], int)
pi2 = (11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0)


def anf(function):
    '''
    Получение коэффициентов АНФ
    '''
    buff = []
    iterations = len(function)
    ANF = [function[0]]
    for _ in range(iterations - 1):
        for i in range(len(function) - 1):
            buff.append(function[i] ^ function[i + 1])
        ANF.append(buff[0])
        function = buff
        buff = []
    return ANF


def hadamardMatrix(dimension):
    '''
    Создание мтрицы Адамара-Сильвестра соответстыующего размера
    '''
    if dimension == 1:
        return W
    else:
        return np.hstack((np.vstack((hadamardMatrix(dimension - 1), hadamardMatrix(dimension - 1))),
                          np.vstack((hadamardMatrix(dimension - 1), -hadamardMatrix(dimension - 1)))))


def functionValue(function):
    '''
    Получение таблиц истинности разрядных функций
    '''
    values = [[] for _ in range(len(bin(max(function))[2:]))]
    for value in function:
        for function_number in range(len(bin(max(function))[2:])):
            values[function_number].append(value >> function_number & 1)
    return values


def generateMonoms(n):
    '''
    Генерация всех мономов в лексикографическом порядке
    Функция нужна для вывода разрядных функций в виде АНФ (buildFunction)
    '''
    monoms = ['1']
    x = 1
    for i in range(2 ** n - 1):
        mon = ''
        for j in range(n):
            if x >> j & 1:
                mon += 'x' + str(j)
        monoms.append(mon)
        x += 1
    return (monoms)


def buildFunction(function):
    '''
    Вывод значений функции в виде АНФ
    '''
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
    return (answer)


def fourierSpectrum(function):
    '''
    Коэффициенты фурье разрядных функций
    '''
    values = functionValue(function)
    spectrum = []
    M = hadamardMatrix(int(math.log2(len(function))))
    for functions in range(len(bin(max(function))[2:])):
        spectrum.append(np.matmul(np.array(values[functions]).T, M).tolist())
    return spectrum


def walschSpectrum(function):
    '''
    Коэффицинты Уолша-Адамара разрядных функций
    '''
    values = functionValue(function)
    unit_array = np.array([1 for _ in range(len(function))])
    M = hadamardMatrix(int(math.log2(len(function))))
    spectrum = []
    for functions in range(len(bin(max(function))[2:])):
        spectrum.append(np.matmul((unit_array - 2 * np.array(values[functions])).T, M).tolist())
    return spectrum


def strict_avalanche_effect(function):
    answer = []
    for k in range(4):
        values = functionValue(function)[k]
        temp = 0
        counter = 0
        for i in range(16):
            for j in range(4):
                if (values[temp] != values[temp ^ (2 ** j)]):
                    counter = counter + 1
            temp = temp + 1
        answer.append(counter)
    return(answer)

'''
def bit_independence_criterion(function):
    tpl = (3, 5, 6, 9, 10, 12)
    values = functionValue(pi2)
    for k in range(4):
        temp = 0
        counter = 0
        for i in range(6):
            for u in range(4):
                if tpl(i) << u & 1 == 1:
                    temp_function.append(values[4-u])
            for j in range(16):
         
def bit_independence_criterion(function):
    tpl = (3, 5, 6, 9, 10, 12)
    values = functionValue(pi2)
    for i in range(6):
        temp_functions = []
        for u in range(4)
            if tpl(i) << u & 1 == 1:
                temp_functions.append(4-u)
        for j in range(16):
            if values[temp_functions[1]] 
'''
'''
def avalanche_effect(function):
    answer = []
    for i in range(len(function)):
        counter = 0
        for j in range(4):
            if function(i) << j & 1 != function(i ^ ))
'''

print(functionValue(pi2))
print(buildFunction(pi2))
print(walschSpectrum(pi2))
print(fourierSpectrum(pi2))
print(int('111', 2))
print(strict_avalanche_effect(pi2))
print(bin(5))
