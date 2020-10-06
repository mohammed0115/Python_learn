a=[
    [1,2,3,4],
    [5,6,7,8],
    [10,7,5,5],
    [6,2,4,3],
    
]
b=[
    [1,2,3,4],
    [5,6,7,8],
    [10,7,5,5],
    [6,2,4,3,]
]

#  summation
sum=[]
for i in range(len(a)): 
    row=[]
    for j in range(len(a[i])):
      x= a[i][j]+b[i][j]
      row.append(x)
    sum.append(row)
          

print(sum)       


#  substraction
sub=[]
for i in range(len(a)): 
    row=[]
    for j in range(len(a[i])):
      x= a[i][j]-b[i][j]
      row.append(x)
    sub.append(row)
          

print(sub)       

#  multiplication
mul=[]
for i in range(len(a)):
    row=[]
    for j in range(len(b)):
        x=0
        for k in range(len(b)):
            x+=a[i][k]*b[k][j]      
        row.append(x)
        print(row)
    mul.append(row)    

          

print(mul) 