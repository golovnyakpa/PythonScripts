def truth_table(table_of_values, num_of_bits):
	"""
	truth_table(table_of_values, num_of_bits)
	Return truth table of s- function using table of values . The result is matrix
	where y[i][j] corresponds to j string of yi truth table
	"""
	y = []
	for i in range(num_of_bits):
		y.append([])
		for j in table_of_values:
			y[i].append(j >> i & 1)
	return(y)


def pascal_triangle(lst):
	"""
	pascal_triangle(lst)
	Return coefficients of Zhegalkin polynomial in lexicographical order
	"""
	lst1, lst2 = [], []
	answer = []
	answer.append(lst[0])
	lst1 = lst
	for i in range(len(lst) - 1):
		if i % 2 == 0:
			lst = lst1
			lst2.clear()
		else:
			lst = lst2
			lst1.clear()
		for j in range(len(lst) - 1):
			if i % 2 == 0:
				lst2.append(lst1[j] ^ lst1[j+1])
				if j == 0:
					answer.append(lst1[j] ^ lst1[j+1])
			else:
				lst1.append(lst2[j] ^ lst2[j+1])
				if j == 0:
					answer.append(lst2[j] ^ lst2[j+1])
	return(answer)


def build_s_function(table, num_of_bits):
	"""
	build_s_function(table, num_of_bits):
	Return bit functions in string type
	"""
	answer = ''
	y = truth_table(table, num_of_bits)
	monoms = generate_monoms(num_of_bits)
	print_yi = "y{}"
	counter = 0
	for i in y:
		answer += print_yi.format(counter) + ' = '
		coefficients = pascal_triangle(i)
		for j in range(2 ** num_of_bits):
			if coefficients[j]:
				answer += monoms[j] + ' xor '
		counter += 1
		answer = answer[0:len(answer) - 4:]
		answer += '\n'
	print(answer)


def weight(table, num_of_bits):
	for i in range(num_of_bits):
		weight = 0
		for j in table:
			if (j >> i & 1):
				weight += 1
		print('Weight of y' + str(i) + ' = ' + str(weight))
	return(None)


def generate_monoms(n):
	"""
	generate_monoms(n)
	Return list of monoms in lexicographical order
	"""
	monoms = ['1']
	x = 1
	for i in range(2 ** n - 1):
		mon = ''
		for j in range(8):
			if x >> j & 1:
				mon += 'x' + str(j)
		monoms.append(mon)
		x += 1
	return(monoms)
	
	
def get_monoms_num(table, num_of_bits):
	y = truth_table(table, num_of_bits)
	k, counter = 0, 0
	for i in y:
		coefficients = pascal_triangle(i)
		for j in coefficients:
			if j == 1:
				counter += 1
		print('Monoms num in y' + str(k) + ' is: ' + str(counter))
		counter = 0
		k += 1


S7 = (
	54, 50, 62, 56, 22, 34, 94, 96, 38, 6, 63, 93, 2, 18, 123, 33,
	55, 113, 39, 114, 21, 67, 65, 12, 47, 73, 46, 27, 25, 111, 124, 81,
	53, 9, 121, 79, 52, 60, 58, 48, 101, 127, 40, 120, 104, 70, 71, 43,
	20, 122, 72, 61, 23, 109, 13, 100, 77, 1, 16, 7, 82, 10, 105, 98,
	117, 116, 76, 11, 89, 106, 0, 125, 118, 99, 86, 69, 30, 57, 126, 87,
	112, 51, 17, 5, 95, 14, 90, 84, 91, 8, 35, 103, 32, 97, 28, 66,
	102, 31, 26, 45, 75, 4, 85, 92, 37, 74, 80, 49, 68, 29, 115, 44,
	64, 107, 108, 24, 110, 83, 36, 78, 42, 19, 15, 41, 88, 119, 59, 3)


build_s_function(S7, 7)
