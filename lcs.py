
#obtain LCS --------------------------
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

lcs("10010101","010110110")
#print("LCS of (10010101,010110110) is: ", lcs("10010101","010110110"))
