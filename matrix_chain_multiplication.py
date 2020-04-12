# Given n matrices from A1, A2, ..., An, we will give optimal solution to what order
# should we do matrix multiplication. Since Matrix multiplication is associative,
# changing order of computation does not change result of matrix multiplication.
# So, instead of giving result of matrix multiplication, this program gives in what order
# should we compute by giving parenthesizes.

import math

# Initialize
matrix_colmuns=[5,10,3,12,5,50,6] #define matrices

number_of_matrix=len(matrix_colmuns)-1

value_table = [0] * number_of_matrix
memorized_table = [0] * number_of_matrix

for i in range(number_of_matrix):
    value_table[i] = [0] * number_of_matrix
    memorized_table[i]= [0] * number_of_matrix

#Dynamic Programming Computation
for l in range(2,len(matrix_colmuns)): # l is length of matrices.
#l=2
    for i in range(0, len(matrix_colmuns)-l): # i is start index of matrices
        #print("(l,i)",l,i)
        j=i+l-1 #j is end index of matrices
        
        #debug
        #print("l:",l, "i:",i ,"j:",j)
        # first set all value to infinity since we replace to min value
        value_table[i][j]=math.inf

        for k in range(i, j): # k is intermaviate dot
            
            current_multiplication = value_table[i][k] + value_table[k+1][j]\
            + matrix_colmuns[i]*matrix_colmuns[k+1]*matrix_colmuns[j+1]
            
            #update minimum mult. count if smaller than current value
            if(current_multiplication < value_table[i][j]):
                value_table[i][j]= current_multiplication
                memorized_table[i][j]=k+1 # memorize in which (left) matrix to split


def print_order(memorized_table,i,j):
    if(i==j):
        print("A"+str(i+1))
    else:
        print("(")
        print_order(memorized_table,i,memorized_table[i][j]-1)
        print_order(memorized_table,memorized_table[i][j],j)
        print(")")
    
    

#Print
for item in value_table:
    print(item)
print("------ memorized table ------")
for item in memorized_table:
    print(item)

print("------------The optimal order is below------------")
print_order(memorized_table,0,number_of_matrix-1)
