# Given keys from A1, A2, ..., An with each given probability,
# we will give optimal solution to what order
# should we build binary search tree.

import math

# Initialize
probability_of_keys=[0.05, 0.1, 0.05, 0.05, 0.05, 0.1] #define probability of each keys

number_of_keys=len(probability_of_keys)

value_table = [0] * number_of_keys
probability_table= [0] * number_of_keys
memorized_table = [0] * number_of_keys

for i in range(number_of_keys):
    value_table[i] = [0] * number_of_keys
    memorized_table[i]= [0] * number_of_keys
    probability_table[i]= [0] * number_of_keys

#Dynamic Programming Computation
for l in range(1,len(probability_of_keys)): # l is length of keys.
#l=2
    for i in range(0, len(probability_of_keys)-l): # i is start index of matrices
        #print("(l,i)",l,i)
        j=i+l #j is end index of matrices
        
        value_table[i][j]=math.inf
        probability_table[i][j]=probability_table[i][j-1]+\
                                probability_of_keys[j]
        for k in range(i, j): # k is intermaviate dot
            current_multiplication =value_table[i][k-1]+value_table[k+1][j]+probability_table[i][j]
            
            
            #update minimum mult. count if smaller than current value
            if(current_multiplication < value_table[i][j]):
                value_table[i][j]= round(current_multiplication,4)
                memorized_table[i][j]=k+1 # memorize in which (left) matrix to split

"""
def print_order(memorized_table,i,j):
    if(i==j):
        print("A"+str(i+1))
    else:
        print("(")
        print_order(memorized_table,i,memorized_table[i][j]-1)
        print_order(memorized_table,memorized_table[i][j],j)
        print(")")
"""
    

#Print
print("------ probability sum table ------")
for item in probability_table:
    print(item)
print("------ expected value table ------")
for item in value_table:
    print(item)
print("------ memorized table ------")
for item in memorized_table:
    print(item)
"""
print("------------The optimal order is below------------")
print_order(memorized_table,0,number_of_keys-1)
"""
