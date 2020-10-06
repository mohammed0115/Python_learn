def sum(start, end):
   result = 0
   for i in range(start, end + 1):
       result += i
   print(result)

sum(1,10)

def sumN(*args):
    result=0
    for i in args:
        result+=i
    return result


print(sumN(1,2,3,4,5,6,7,8,9,10))
list={40,50,80,70}
print(sumN(*list))



