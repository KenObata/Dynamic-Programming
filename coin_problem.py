# Coin exchange problem
# Given types of coin such as cents, quarter,...etc,
# this program returns minimum number of coin and its combination.

#initialize
price=15
coin_5=[]
coin_12=[]
memorized_coin_12=[]
memorized_coin_5=[]

for k in range(price+1):
    coin_5.append(0)
    coin_12.append(0)
    memorized_coin_5.append(0)
    memorized_coin_12.append(0)

#only for coin_1
coin_1=[i for i in range(0, price+1)]

#for coin$1 and $5
for k in range(1,len(coin_5)):
    if(k>4 and coin_1[k] > coin_5[k-5]+1):
        coin_5[k]=coin_5[k-5]+1
        memorized_coin_5[k]=5
    else:
        coin_5[k]=coin_1[k]
        memorized_coin_5[k]=1

#for coin$1 ,$5 and $12
for k in range(1,len(coin_12)):
    if(k>11 and coin_5[k] > coin_12[k-12]+1):
        coin_12[k]=coin_12[k-12]+1
        memorized_coin_12[k]=12
    else:
        coin_12[k]=coin_5[k]
        memorized_coin_12[k]=memorized_coin_5[k]


# function to output combination of rod
# input1: memorized_rod (which means we have i types of rod),
# input2: n th price -->To what price do we want to find solution?
# output: list of rod number
def combination_coin(memorized_coin,n):
    li_coin=[]
    
    combination1=memorized_coin[n]
    li_coin.append(combination1)
    
    if(memorized_coin[n-combination1]>0):
        combination2=memorized_coin[n-combination1]
        li_coin.append(combination2)
    
    else:
        return li_rod
    
    if(memorized_coin[n-combination1-combination2]>0):
        combination3=memorized_coin[n-combination1-combination2]
        li_coin.append(combination3)
    
    else:
        return li_coin
    
    return li_coin

# if we calculate only max, code gets long.
# at every coin_12, we need to recalculate coin_5 again.
# This is avoided in above dynamic programming of bottom up approach.

#print([i for i in range(0, 16)])
print(coin_1)
print(coin_5)
print(coin_12)
print("combination of price{} is:".format(price), combination_coin(memorized_coin_12, price) )
