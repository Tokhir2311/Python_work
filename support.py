'''#funs7

def revers(son):
    raq = 0
    while son > 0:
        raq=raq*10+son%10
        son = son//10
    return raq
  
print(revers(123))

#funs9

def son_qosh(son):
    s = str(son)
    k = "9" + s
    return int(k) 
    
print(son_qosh(123))

#fun10
def swaper(*sonlar):
    for i in sonlar:
        if i % 2 ==0:
            ====
        else:
            return "Not swapable"
print(swaper(1, 2, 3, 4, 5, 6))

#fun21

def yig(son, son1):
    if son > son1:
        return 0
    if son < son1:
        summa = 0
        for i in range(son, son1+1, 1):
            summa +=i
        return summa
print(yig(10, 15))


#fun22
def kalk(son, son1, **blg):
    for val in blg.values():
        if val == "+":
            return son + son1
        elif val == "-":
            return son - son1
        elif val == "*":
            return son * son1
        elif val == "/":
            return son // son1
print(kalk(12, 2, op = "*"))
        
#funs 25
def issqr(son):
    chek = son//son**0.5
    if chek == son**0.5:
        return True
    else :
        return False
print(issqr(45))


#funs26
def issqr5(son):
    while son > 6:
        son = son // 5
    if son == 5:
        return True
    else : 
        return False
print(issqr5(125))
     

#fun28

def digcnt(son):
    cnt = 0
    while son > 0:
        son = son //10
        cnt +=1
    return cnt
print(digcnt(123456))
   
 
 
def isprm(son)->bool:
    for i in range(2,int(son**0.5)+1):
        if son%i==0:
            return  False
    return True
print(isprm(21))

==============================================================================================================.smd3 I think

def greet()->str:
    print("Hello")
    
var = greet

print(var())

def add(a, b):
    return a + b
def subt(a, b):
    return a-b
op = [add, subt]

for i in op:
    print(i(12, 11))
  
def add(a, b):
    return a + b
def subt(a, b):
    return a-b
def mul(a, b):
    return a*b
    
oper = input("Enter operation: (add , sub, mul) ")   
op = {"add":add, "sub":subt, "mul":mul}
a = int(input("a = "))
b = int(input("b = "))
print(op[oper](a, b))

v = int(input("son : "))
#def sqrr(val):
#   return val**2
    
def apply(funk, v):
    return funk(v)
print(apply(lambda x : x*x, v))   #lambda shu yerga yozilsun 


def mainfunk(funk, a, b):
    return funk(a, b)
    
print(mainfunk(lambda x, y : x**y, 3, 4))



nums = [1, 2, 3, 4, 5]

def sqrr(val):
    for i in range(5):     CHALAAAAAAAAAAAAAAAAAAAA
        print(lambda val: val**2)
print(sqrr( 5))
   
 
    
    
lmbs = (
lambda y: y.upper(),
lambda y: y.lower(),
lambda y: y.title()
)

for i in lmbs:
    print(i("python"))
    


tup = (
lambda x: x+5, 
lambda x : x+10,
lambda x : x+15
)

def taker():
    for i in tup:
        print(i(20))

taker()


def choose(i: bool, x, f1, f2):
    if i == True:
        return f1(x)
    elif i ==False:
        return f2(x)


print(choose(False, 20, lambda x: x+10, lambda x : x-10 ))

def funk_s(n):
    if n == "sq":                        <-----13
        return lambda x : x*2
    elif n == "db":
        return lambda x : x**2
    elif n == "cube":
        return lambda x : x**3

funk = funk_s("db")
print(funk(3))
 

def funk_s(n, nums):
    if n == "even":
        for i in nums:
            return lambda x : x%2==0
    elif n == "odd":
        for i in nums:
            return lambda x : x%2==1

funk = funk_s("odd", [1, 2, 3, 4, 5])


print(funk)

15

def ret(strin):
    for i in "aoeui":
        if strin[0] == i:
            return lambda x: x + " your str"
        return lambda x: x + " your str not vowel"

idonno = ret("salom")
print(idonno("assalom"))



16 

names = ['ali', 'vali', 'eshmat']

def trans(s):
    return s.upper()
    
def fun(f, l):
    s = []
    for i in l:
        s.append(f(i))
    return s
    
print(fun(trans, names))




17
def con_ap(f1t, f2f, num):
    if num %2==0:
        return f1t
    return f2f
    
print(lambda x : x**2, lambda x : x**3, 3)


18
19 

def repeat(f: Callable, n: int):
    for i in range(1, n+1)
        return f

print(repeat(lambda x: x+2, 3))




20
def ch_op(sym):
    if sym == "+":
        s = lambda x: x+x
    elif sym == "-":
        s = lambda x: x-x
    elif sym == "*":
        s = lambda x: x*x
    elif sym == "/":
        s = lambda x: x//x
    return s
k = ch_op('*')
print(k(5))

 21
words = ['vali', 'ali', 'eshmat', 'buuzunsoz']

sorted_list = sorted(words, key=lambda x : len(x))
print(sorted_list)
 
 22
 
l = [('ali', 20), ("vali", 19), ("akmal", 22)]
l_sorted = sorted(l, key=lambda x : min(x))
print(l_sorted)
 
 
 
31

s = lambda x : print('even') if x%2==0 else print('odd')
print(s(4))

32

names = ['ali', 'vali', 'eshmat', "kimdir"]

prin = filter(lambda x: if i in x[0] == "aouie")



41
def make_p(n):
    return lambda x: x**n
    
res = make_p(3)
print(res(3))

    42
Listf = [
lambda x : x+1,
lambda x : x+2,
lambda x : x+3,
lambda x : x+4]
def main_f(f):
    s = []
    for i in Listf:
        s.uppend(i(val))
    return s
    
res= main_f(f2)
print(res(3))

from typing import Callable
def kool():
    return "Hello"
def repeat(f: Callable, n: int):
    for i in range(1, n+1):
        f(3)

print(repeat(kool(), 3))
    '''


Listf = [
lambda x : x+1,
lambda x : x+2,
lambda x : x+3,
lambda x : x+4]
def main_f(f):
    s = []
    for i in Listf:
        s.uppend(i(val))
    return s
    
res= main_f(f2)
print(res(3))    
    
