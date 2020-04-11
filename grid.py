#This program computes distinct shortest path from start to end point
# of grif n time m size. You can pick your start point an dend point

# If you want to compute start point from (0,0) to intermediate point(n,m)
# and compute end point(x,y), the first compute start[0,0] to [n,m].
# where height =n, base=m.
# After that set the start point[n,m] and with height and base
# are the original size. Then total distinct path is
# sum of the two computation.

#-------------setup--------------
#Define size
height=5
base=6

#define where you start from
start=[0,0]

#initialize table
value_table = [0] * height
for i in range(len(value_table)):
    value_table[i] = [1] * base

#--------------------------------


#Dynamic Programming Computation
for row in range(start[0],height):
    for col in range(start[1],base):
        if(row ==0 and col==0):
            value_table[row][col]=1
        elif(row ==0 and col!=0):
            value_table[row][col]=value_table[row][col-1]
        elif(row !=0 and col==0):
            value_table[row][col]=value_table[row-1][col]
        else:
            value_table[row][col]=value_table[row][col-1]\
        +value_table[row-1][col]

#adjust
value_table[0][0]=0
#Print
for item in value_table:
    print(item)

