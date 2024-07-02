#List comprehension
n = [i for i in range(1,20)]
print("The numbers in the range are:",n)

def add_num(x,y):
    z = x + y
    return z
ans = add_num(4,5)
print("The result of add_num:",ans)

#map()
a_num = list(map(lambda x:add_num(x,5),n))
print("The updated list:",a_num)

#filter()

b_num = list(filter(lambda x:x%2 == 0,n))
print("The even numbers list:",b_num)

#Closure
def Abc():
    f = 2
    def Xyz(n):
        x = n*f
        return x
    return Xyz
ans = Abc()
res = ans(5)
print("The result is:",res)
