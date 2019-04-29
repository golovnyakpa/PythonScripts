import math
import numpy as np

W = np.array([[1, 1], [1, -1]], int)
V = np.array([[1, 0], [-1, 1]], int)
pi2 = (11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0)


def anf(function):
    """
    Получение коэффициентов АНФ
    """
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


def hadamard_matrix(dimension):
    """
    Создание мтрицы Адамара-Сильвестра соответстыующего размера
    """
    if dimension == 1:
        return W
    else:
        return np.hstack((np.vstack((hadamard_matrix(dimension - 1), hadamard_matrix(dimension - 1))),
                          np.vstack((hadamard_matrix(dimension - 1), -hadamard_matrix(dimension - 1)))))


def function_value(function):
    """
    Получение таблиц истинности разрядных функций
    """
    values = [[] for _ in range(len(bin(max(function))[2:]))]
    for value in function:
        for function_number in range(len(bin(max(function))[2:])):
            values[function_number].append(value >> function_number & 1)
    return values


def generate_monoms(n):
    """
    Генерация всех мономов в лексикографическом порядке
    Функция нужна для вывода разрядных функций в виде АНФ (buildFunction)
    """
    monoms = ['1']
    x = 1
    for i in range(2 ** n - 1):
        mon = ''
        for j in range(n):
            if x >> j & 1:
                mon += 'x' + str(j)
        monoms.append(mon)
        x += 1
    return monoms


def build_function(function):
    """
    Вывод значений функции в виде АНФ
    """
    answer = ''
    num_of_bits = len(bin(max(function))[2:])
    monoms = generate_monoms(num_of_bits)
    print_yi = "y{}"
    counter = 0
    for i in range(num_of_bits):
        answer += print_yi.format(counter) + ' = '
        coefficients = function_value(anf(function))[i]
        for j in range(len(function)):
            if coefficients[j]:
                answer += monoms[j] + ' ⊕ '
        counter += 1
        answer = answer[0:len(answer) - 3:]
        answer += '\n'
    return answer


def fourier_spectrum(function):
    """
    Коэффициенты фурье разрядных функций
    """
    values = function_value(function)
    spectrum = []
    M = hadamard_matrix(int(math.log2(len(function))))
    for functions in range(len(bin(max(function))[2:])):
        spectrum.append(np.matmul(np.array(values[functions]).T, M).tolist())
    return spectrum


def walsch_spectrum(function):
    """
    Коэффицинты Уолша-Адамара разрядных функций
    """
    values = function_value(function)
    unit_array = np.array([1 for _ in range(len(function))])
    M = hadamard_matrix(int(math.log2(len(function))))
    spectrum = []
    for functions in range(len(bin(max(function))[2:])):
        spectrum.append(np.matmul((unit_array - 2 * np.array(values[functions])).T, M).tolist())
    return spectrum


def strict_avalanche_effect(function):
    answer = []
    for k in range(4):
        values = function_value(function)[k]
        temp = 0
        counter = 0
        for i in range(16):
            for j in range(4):
                if values[temp] != values[temp ^ (2 ** j)]:
                    counter = counter + 1
            temp = temp + 1
        answer.append(counter)
    for i in range(len(answer)):
        answer[i] = answer[i] / 64
    return answer


def possitions_of_ones(n):
    """
    Определяет на сколько позиций надо сдвигать число циклически
    вправо, чтобы получить единицу.
    Ответ возвращает в виде списка
    """
    answer = []
    for i in range(4):
        if n >> i & 1 == 1:
            answer.append(i)
    return answer


def bit_independence_criterion(function):
    probs = strict_avalanche_effect(function)
    tpl = (3, 5, 6, 9, 10, 12)
    result = []
    answ = []
    for i in tpl:
        pos = possitions_of_ones(i)
        counter = 0
        for j in range(16):
            for k in range(4):
                if function[j] >> pos[0] & 1 != function[j ^ (2 ** k)] >> pos[0] & 1 and \
                   function[j] >> pos[1] & 1 != function[j ^ (2 ** k)] >> pos[1] & 1:
                    counter += 1
        answ.append(counter / 64)
        if counter / 64 == probs[pos[0]] * probs[pos[1]]:
            result.append('independent')
        else:
            result.append('dependent')
        counter = 0
    return result


def avalanche_effect(function):
    """
    первый список- результаты для х4,..
    Первый элемент первого списка- количество векторов, поменявших 0 координат...
    """
    answer = [[0, 0, 0, 0, 0] for _ in range(4)]
    for k in range(4):
        for i in range(16):
            counter = 0
            for j in range(4):
                if function[i] >> j & 1 != function[i ^ (2 ** k)] >> j & 1:
                    counter += 1
            answer[k][counter] += 1
    sum = 0
    for i in answer:
        for j, k in enumerate(i):
            sum += j * k
    result = sum / (16 * 4)
    return result


print(function_value(pi2))
print(build_function(pi2))
print(walsch_spectrum(pi2))
print(fourier_spectrum(pi2))
print(strict_avalanche_effect(pi2))
print(bit_independence_criterion(pi2))
print(avalanche_effect(pi2))
m = avalanche_effect(pi2) / 4
print(m)
