# This program finds monotonicly increasing subsequence from given integer sequence.
# Runtime is O(n^2) since each table consists of n row and n column.

# Function: print_lcs --------------
# After we computed value table and memorized table,
# This function prints what's the longest sequence.(of monotinc increasing)
# Input:memorized_table, sequence X, index i and j.

def print_lcs(memorized_table,X,i,j):
    if(i==0 or j==0):
        return
    if(memorized_table[i][j]=="↖"):
        #debug
        print("↖")
        
        print_lcs(memorized_table, X,i-1,j-1)
        print(X[i-1]) #index of X is -1 from table index
    elif(memorized_table[i][j]=="↑"):
        #debug
        print("↑")
        
        print_lcs(memorized_table, X,i-1,j)

    else:
        #debug
        print("←")
        print_lcs(memorized_table, X,i,j-1)
    
    return None
#-------------------------------------

# Function: lcs --------------
# By computing value table and memorized table,
# This function prints value table and memorized tabl
# Input: two string X and Y

def lcs(X,Y):
    
    n=len(X)+1
    m=len(Y)+1
    #initialize
    value_table = [0] * n
    memorized_table = [0] * n
    for i in range(n):
        value_table[i] = [0] * m
        memorized_table[i]= [0] * m

    #Dynamic Programming Computation
    for row in range(1,len(X)+1):
        for col in range(1,len(Y)+1):
            
            if(X[row-1]==Y[col-1]):
                value_table[row][col] = value_table[row-1][col-1] + 1
                memorized_table[row][col]="↖"
            elif(value_table[row-1][col] >= value_table[row][col-1] ):
                value_table[row][col]=value_table[row-1][col]
                memorized_table[row][col]="↑"
            else:
                value_table[row][col]=value_table[row][col-1]
                memorized_table[row][col]="←"
    #Print
    for item in value_table:
        print(item)
    for item in memorized_table:
        print(item)

    print("--------- function print_lcs ---------")
    print_lcs(memorized_table, X, len(X),len(Y))
    
    return None

#-----------------------------------

# Test Driver
# Given one sequence of integers, take it as one sequence.
# Another sequence is sorted sequence. Then compute LCS of the two.

# Here is the input of the sequence ↓
sequence="9187365584"

# sort sequence
array= [int(i) for i in list(sequence)]
array.sort()

#concatenate all sorted integers
sorted_sequence = ''.join([str(i) for i in array])

lcs(sequence,sorted_sequence)
