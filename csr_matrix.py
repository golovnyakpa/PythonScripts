#!/usr/bin/env python
# coding: utf-8


import numpy as np


class CSRMatrix:
    """
    CSR (2D) matrix.
    Here you can read how CSR sparse matrix works: https://en.wikipedia.org/wiki/Sparse_matrix

    Must be implemented:
    1. Getting and setting element by indexes of row and col.
    a[i, j] = v -- set value in i-th row and j-th column to value
    b = a[i, j] -- get value from i-th row and j-th column
    2. Pointwise operations.
    c = a + b -- sum of two CSR matrix of the same shape
    c = a - b -- difference --//--
    c = a * b -- product --//--
    c = alpha * a -- product of scalar alpha and CSR matrix a
    c = a / alpha -- divide CSR matrix a by nonzero scalar alpha
    3. Scalar product
    c = a.dot(b) -- matrix multiplication if shapes match
    c = a @ b --//--
    4. nnz attribute -- number of nonzero elements in matrix
    """

    def __init__(self, init_matrix_representation):
        """
        :param init_matrix_representation: can be usual dense matrix
        or
        (row_ind, col, data) tuple with np.arrays,
            where data, row_ind and col_ind satisfy the relationship:
            a[row_ind[k], col_ind[k]] = data[k]
        """
        self.A = []
        self.IA = [0]
        self.JA = []
        if isinstance(init_matrix_representation, tuple) and \
           len(init_matrix_representation) == 3:
            if len(init_matrix_representation[0]) == \
               len(init_matrix_representation[1]) == \
               len(init_matrix_representation[2]):
                for i in range(len(init_matrix_representation[0])):
                    self.A.append(init_matrix_representation[2][i])
                    self.JA.append(init_matrix_representation[1][i])
                for i in range(max(init_matrix_representation[0])+1):
                    self.IA.append(init_matrix_representation[0].count(i)+self.IA[-1])
            else:
                raise ValueError
            self.col_num = max(init_matrix_representation[1])
            self.row_num = max(init_matrix_representation[0])
            '''
            print(self.A)
            print(self.IA)
            print(self.JA)'''
        elif isinstance(init_matrix_representation, np.ndarray):
            for row in init_matrix_representation:
                nnz_in_row = 0
                for i, element in enumerate(row):
                    if element != 0:
                        self.A.append(element)
                        self.JA.append(i)
                        nnz_in_row += 1
                self.IA.append(self.IA[-1]+nnz_in_row)
            self.col_num = len(init_matrix_representation[0])
            self.row_num = len(init_matrix_representation)
            '''
            print(self.A)
            print(self.IA)
            print(self.JA)'''
        else:
            raise ValueError

    def to_dense(self):
        """
        Return dense representation of matrix (2D np.array).
        """
        lst_of_lst = [[] for i in range(len(self.IA)-1)]
        for i in range(len(self.IA)-1):
            for j in range(max(self.JA)+1):
                lst_of_lst[i].append(self[i, j])
        return np.array(lst_of_lst)

    def __getitem__(self, indexes):
        i, j = indexes
        ptr_1 = self.IA[i+1]
        ptr_0 = self.IA[i]
        if not ptr_1 - ptr_0:
            return 0
        try:
            offset = self.JA.index(j, ptr_0, ptr_1)
            return self.A[offset]
        except ValueError:
            return 0

    def __setitem__(self, indexes, val):
        i, j = indexes
        if self[i, j]:
            if val:
                ptr_0 = self.IA[i]
                ptr_1 = self.IA[i+1]
                offset = self.JA.index(j, ptr_0, ptr_1)
                self.A[offset] = val
            else:
                ptr_0 = self.IA[i]
                ptr_1 = self.IA[i+1]
                offset = self.JA.index(j, ptr_0, ptr_1)
                for k in range(i+1, len(self.IA)):
                    self.IA[k] -= 1
                del self.A[offset]
                del self.JA[offset]
        else:
            if not val:
                return
            else:
                for k in range(i+1, len(self.IA)):
                    self.IA[k] += 1
                ptr_0 = self.IA[i]
                ptr_1 = self.IA[i+1]
                tmp_ptr = self.IA[i]
                for el in self.JA[ptr_0:ptr_1]:
                    if el > j:
                        break
                    else:
                        tmp_ptr += 1
                if tmp_ptr == self.IA[i]:
                    self.JA.insert(tmp_ptr, j)
                    self.A.insert(tmp_ptr, val)
                    return
                self.JA.insert(tmp_ptr-1, j)
                self.A.insert(tmp_ptr-1, val)

    @property
    def nnz(self):
        return self.IA[-1]

np.random.seed(42)
'''
matrix = np.random.randint(0, 2, (200, 200))
csr_matrix = CSRMatrix(matrix)
print(csr_matrix.IA)
csr_matrix[1,1]'''
'''
for i, j in zip(range(matrix.shape[0]), range(matrix.shape[1])):
    print(csr_matrix[i, j])
    np.isclose(matrix[i, j], csr_matrix[i, j])'''


row_ind = [1,1,2,3,3]
col_ind = [0,1,2,1,3]
data = [5, 8, 3, 6,5]
#x = np.array([[10, 20, 0, 0, 0, 0], [0, 30, 0, 40, 0, 0], [0, 0, 50, 60, 70, 0], [0, 0, 0, 0, 0, 80]])
x = np.array([[0, 0, 0, 0], [5, 8, 0, 0], [0, 0, 2, 0], [0, 0, 0, 1]])
m = CSRMatrix(x)
M = CSRMatrix((row_ind, col_ind, data))
m[0, 3] = 1
print(m.A, m.IA, m.JA)
m[1, 1] = 10
m[2,2] = 3
print(m.A, m.IA, m.JA)
print(m.to_dense())
