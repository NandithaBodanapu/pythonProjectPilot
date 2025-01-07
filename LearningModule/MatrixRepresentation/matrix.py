#we use numpy for performing manipulations for matrices
import numpy as np

# create matrix
matrix_1=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_2=np.array([[1,1,1],[2,2,2],[3,3,3]])
print(matrix_1)
print(matrix_2)

#creating a matrix of zeros
zero_mat=np.zeros((3,3))
print("Zero matrix \n",zero_mat)

#creating a matrix of 1s
one_mat=np.ones((3,2))
print("ones matrix \n",one_mat)

#creating a matrix of identity matrix
identity_matrix=np.eye(4)
print("identity matrix \n",identity_matrix)


#Matrix addition
add_mat=np.add(matrix_1,matrix_2)
print("matrix addition \n" ,add_mat)

sub_mat=np.subtract(matrix_1,matrix_2)
print("matrix subtraction \n", sub_mat)

mul_mat=np.multiply(matrix_1,matrix_2)
print("matrix multiplication \n",mul_mat)

div_mat=np.divide(matrix_1,matrix_2)
print("matrix division \n", div_mat)



