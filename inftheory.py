import numpy as np 
import math

def fourier_spectrum(a):
	matrix = np.zeros((len(a),len(a)), dtype=complex)
	for i in range(len(a)):
		for j in range(len(a)):
			matrix[(i,j)] = complex(math.cos(-2 * math.pi * i * j / len(a)), math.sin(-2 * math.pi * i * j / len(a)))
	return(np.around(np.matmul(matrix, a), decimals =3))


def hartley_spectrum():
	matrix = np.zeros((len(a),len(a)), dtype=complex)
	
while True:
	strg = input()
	a = strg.split()
	for i in range(len(a)):
		a[i] = int(a[i])
	a = np.array(a)
	fs = fourier_spectrum(a)
	hs = []
	for i in fs:
		hs.append(i.real - i.imag)
	print("Фурье: " + str(fs))
	print("Хартли: " + str(hs))
