#Goal is to maximize price we can sell from a given length n of gold.
#decide whether we should cut into pieces or just cell as it is.


rod1=[]
rod2=[]
rod3=[]
rod4=[]
rod5=[]
rod6=[]
rod7=[]
rod8=[]
rod9=[]
rod10=[]

memorized_rod1=[]
memorized_rod2=[]
memorized_rod3=[]
memorized_rod4=[]
memorized_rod5=[]
memorized_rod6=[]
memorized_rod7=[]
memorized_rod8=[]
memorized_rod9=[]
memorized_rod10=[]

#initialize rod1
rod1=[i for i in range(0, 11)]
memorized_rod1=[1 for i in range(0,11)]

#initialize cost
cost=0

for k in range(11):
    rod2.append(0)
    rod3.append(0)
    rod4.append(0)
    rod5.append(0)
    rod6.append(0)
    rod7.append(0)
    rod8.append(0)
    rod9.append(0)
    rod10.append(0)

    memorized_rod2.append(0)
    memorized_rod3.append(0)
    memorized_rod4.append(0)
    memorized_rod5.append(0)
    memorized_rod6.append(0)
    memorized_rod7.append(0)
    memorized_rod8.append(0)
    memorized_rod9.append(0)
    memorized_rod10.append(0)

#for rod2
for k in range(1,len(rod2)):
    if(k>1 and rod1[k] < rod2[k-2]+5 -cost):
        rod2[k]=rod2[k-2]+5 -cost
        memorized_rod2[k]=2
    else:
        rod2[k]=rod1[k]
        memorized_rod2[k]=memorized_rod1[k]

#for rod3
for k in range(1,len(rod3)):
    if(k>2 and rod2[k] < rod3[k-3]+8-cost):
        rod3[k]=rod3[k-3]+8-cost
        memorized_rod3[k]=3
    else:
        rod3[k]=rod2[k]
        memorized_rod3[k]=memorized_rod2[k]

#for rod4
for k in range(1,len(rod4)):
    if(k>3 and rod3[k] < rod4[k-4]+9-cost):
        rod4[k]=rod4[k-4]+9-cost
        memorized_rod4[k]=4
    else:
        rod4[k]=rod3[k]
        memorized_rod4[k]=memorized_rod3[k]

#for rod5
for k in range(1,len(rod5)):
    if(k>4 and rod4[k] < rod5[k-5]+10-cost):
        rod5[k]=rod5[k-5]+10-cost
        memorized_rod5[k]=5
    else:
        rod5[k]=rod4[k]
        memorized_rod5[k]=memorized_rod4[k]

#for rod6
for k in range(1,len(rod6)):
    if(k>5 and rod5[k] < rod6[k-6]+17-cost):
        rod6[k]=rod6[k-6]+17-cost
        memorized_rod6[k]=6
    else:
        rod6[k]=rod5[k]
        memorized_rod6[k]=memorized_rod5[k]

#for rod7
for k in range(1,len(rod7)):
    if(k>6 and rod6[k] < rod7[k-7]+17-cost):
        rod7[k]=rod7[k-7]+17-cost
        memorized_rod7[k]=7
    else:
        rod7[k]=rod6[k]
        memorized_rod7[k]=memorized_rod6[k]

#for rod8
for k in range(1,len(rod8)):
    if(k>7 and rod7[k] < rod8[k-8]+20-cost):
        rod8[k]=rod8[k-8]+20-cost
        memorized_rod8[k]=8
    else:
        rod8[k]=rod7[k]
        memorized_rod8[k]=memorized_rod7[k]

#for rod9
for k in range(1,len(rod9)):
    if(k>8 and rod8[k] < rod9[k-9]+24-cost):
        rod9[k]=rod9[k-9]+24-cost
        memorized_rod9[k]=9
    else:
        rod9[k]=rod8[k]
        memorized_rod9[k]=memorized_rod8[k]

#for rod10
for k in range(1,len(rod10)):
    if(k>9 and rod9[k] < rod10[k-10]+30-cost):
        rod10[k]=rod10[k-10]+30-cost
        memorized_rod10[k]=10
    else:
        rod10[k]=rod9[k]
        memorized_rod10[k]=memorized_rod9[k]

print(rod1,"\n"\
      ,rod2,"\n"\
      ,rod3,"\n"\
      ,rod4,"\n"\
      ,rod5,"\n"\
      ,rod6,"\n"\
      ,rod7,"\n"\
      ,rod8,"\n"\
      ,rod9,"\n"\
      ,rod10
      )

#memorized array
print("-----memorized------")
print(memorized_rod1,"\n"\
      ,memorized_rod2,"\n"\
      ,memorized_rod3,"\n"\
      ,memorized_rod4,"\n"\
      ,memorized_rod5,"\n"\
      ,memorized_rod6,"\n"\
      ,memorized_rod7,"\n"\
      ,memorized_rod8,"\n"\
      ,memorized_rod9,"\n"\
      ,memorized_rod10
      )

# function to output combination of rod
# input1: memorized_rod (which means we have i types of rod),
# input2: n th price -->To what price do we want to find solution?
# output: list of rod number
def combination_rod(memorized_rod,n):
    li_rod=[]
    
    combination1=memorized_rod[n]
    li_rod.append(combination1)
    
    if(memorized_rod[n-combination1]>0):
        combination2=memorized_rod[n-combination1]
        li_rod.append(combination2)
    
    else:
        return li_rod
    
    if(memorized_rod[n-combination1-combination2]>0):
        combination3=memorized_rod[n-combination1-combination2]
        li_rod.append(combination3)
    
    else:
        return li_rod
        
    return li_rod


print("Available rod type=9, length=9: value is {}, combination is:"\
      .format(rod9[9]), combination_rod(memorized_rod9,9)  )

