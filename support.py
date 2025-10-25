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
    
     
     
def main(funk):
    def wrap(*args, **kwargs):
        print("starting...")
        funk()
        print("we are done here!")
    return wrap
@main  
def map_info():
    print("Yunusobod, osiyo street, 1")
    
map_info() 


def main(funk):
    cnt = 0
    def wrap(*args, **kwargs):
        nonlocal cnt
        funk()
        cnt +=1
        print(cnt, "martta")
    return wrap
@main  
def map_info():
    print("hello")
    
map_info()
map_info()
map_info() 





def main(funk):
    def wrap(*args, **kwargs):
        print(funk.__name__)
        funk()
    return wrap
@main    
def map_info():
    print("hello")   
    
map_info()
  
    
def main(funk):
    def wrap(*args, **kwargs):
        return funk().upper()
    return wrap
@main    
def map_info():
    return ("hello")     
print(map_info())
    
    
    #Javoxirniki 5 sinf 
    
from typing import Callable

def decorator(func: Callable):
    def wrapper(string):
        if string:
            print(string.upper())

        func(string)  #return 
    return wrapper

@decorator
def myfunc(n):
    return f"{n}"

myfunc("Hello Javohir")
  
  8
def main(funk):
    def wrap(*args, **kwargs):
        
        for i in args:
            print(type(i))
            funk()
    return wrap
        
        
@main
def funksiya(*k):
    return k

funksiya(12, 3.4, True)

ustoz yozdi 

def dec(f):
    def wrp(*arg, **kwarg):
        for i in arg:
            print(type(i))
        for k in kwarg.values():
            print(type(k))
        f()
    return wrp
    
@dec
def myf(*arg, **kwarg):
    return arg
    
myf(1, 2, "s")


 9
def main(fun):
    def wrp():
        for i in range(3):
            fun()
    return wrp
    
@main
def sayer():
    print("Hello Ehsmat")
    
sayer()
10 
def main(fun):
    def wrp():
    if return fun == None:
        print("No res")
    else :
        return fun
    return wrp
    
@main
def hi():
    return 
    
hi()

11 
def main(fun):
    def wrp(*arg):
        l = []
        for i in arg:
            if i%2==0:
                l.append(i)
            else : 
                "Odd numbers prohibited"
            func(*tuple(l))
    return wrp
    
@main
def add(*arg):
    print(arg)
    
add(12, 13, 15, 100)



def main(fun):
    def wrp():
        if fun() is None:
            return "No res"
        else :
            return fun()
        return fun()
    return wrp
    
@main
def hi():
    return None
    
print(hi())


12

def main(f):
    def wrp(l : list):
        t = set(l)
        f(t)
    return wrp
    
@main 
def myf(s:list):
    print(s)
    
myf([1, 2, 3,3,1, 4,5])


def decorator(func:Callable):
    def wrapper(*args,**kwargs):
     l=[]
     for i in args:
         if isinstance(i,str):
            l.append(i.lower())
     return func(*tuple(l))     
               
    return wrapper
@decorator
def f(*n):
    return n
print(f("ASsror","GIU"))


def decorator(fun):
    def wrapper(*args,**kwargs):
        if fun.count>5:
            return None
        return fun()
    return wrapper
        
        
        
        
@decorator
def my():
    print("hi")
    
my()
my()
my()
my()
my()
my()

21 
def main(d:dict):
    try:
        if isinstance(d, dict):
            d.update({"c":4})
            print(d)
        else:
            raise TypeError()
    except TypeError:
        print("Not dikt")
        
main([2,3]) 


23

def main(l:list):
    try:
        for i in l:
            if not isinstance(i, int):
                raise TypeError()
            #else : 
             #   print(i)
        print(l)
    except TypeError:
        print("son bo`lmagan element aniqlandi")
main([1, 2, 3, 4, 5, "a", "b"])

24 

def main(l:list):
    for i in range(len(l)):
        try:
            l[i] = int(l[i])
        except Exception("Son qilib bo`lmadi"):

main([1, 2, 3, 4, 5, "a", "b"])


25 

try:
    a = list(map(int, input().split()))
    print(a)
except ValueError:
    print("Int bo`lmagan qiymat kiritildi ")


26

l = [1, 2, 3, 4, 5]

def funk(s):
        try:
            print(l[s]**2)
        except IndexError:
            print("Xatolik")  

funk(6)


28 

def download():
    return "fail"
    
try:
    s = download()
    if s == "success":
        print("Yuklandi")
    elif s == "fail" : 
        raise Exception()
except Exception: 
    print("Xatolik")

29 


try:
    res = lambda x, y: x//y
except ZeroDivisionError:
    print(f"{x}sonni 0 ga bo`lib bo`lmaydi")
    
res(2, 0)  




def main(f):
    def wrp(*args, **kwargs):
        l = []
        res = 0
        for arg in args:
            l.append(arg)
            res = res + arg 
        print("List : ", l, "result ", res)
        dcs = []
        val = []
        for key, val in kwargs.items():
            dcs.append(key)
            val.append(val)
        print("Keys : ", dcs)
        print("Vals : ", val)
        
    return wrp
    
    
    
@main
def myf(a, b):
    return a + b
    
print(myf(2, 4))
print(myf(6, 4))
print(myf(2, 9))
    
print() 

def call_logger(func):
    history = []
    def wrp(*args, **kwargs):
        nonlocal history 
        try :
            res = func(*args, **kwargs)
            history.append(
            {"arg":args,
             "kwarg":kwargs,
             "res": res
            }
            )
        except ZeroDivisionError:
            print("Nolga Bo'lma")
        return res
        return history
    nonlocal get_history
    nonlocal history
    wrp.history = get_history
    return wrp
    def get_history():
        return history
    
        
@call_logger
def qosh(a, b):
    return a + b 
    
    
print(2, 3)
print(2, 3)
print(qosh.history())
'''
''' 
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"


print(myfunction())


def cond(a):
    def main(func):
        def wrp(*args):
            for arg in args:
                if a == True:
                    return func(arg*2)
                else :
                    return func(arg//2)
        return wrp
    return main
    
@cond(True)
def my_f(b):
    return b    
    
print(my_f(4))


s = list(map(int, input().split()))
f = open("faylim2.txt", "w+")
for i in s:
    if i % 2 ==0:
        f.write(str(i))
        f.write("\n")
f.close()


k = open("faylim2.txt", "r")
res = k.read()
f = open("faylim3.txt", "w+")
r = len(res)
f.writelines(r)
print(f.read())
f.close()
k.close()





f= open("faylim2.txt", "r")
lines = f.readlines()
f.close()

k = open("faylim3.txt", "a")
for l in lines:
    l = l[:-1]
    k.write(l[::-1]+ "\n")
k.close()


f = open("faylim2.txt", "r")

res = f.read().split()
ls={}
mx = 0
for i in res:
    if i in res:
        ls.update(i)
        mx +=1
    else :
        ls.update(i)
        mx = 1

print(ls[mx])


f.close()

f = open("faylim2.txt", "r")

res = f.read().split()
ls={}

for i in res:
    if i in ls:
        ls[i] +=1
    else:
        ls[i] = 1
print(ls)     
f.close()



f = open("faylim2.txt", "r+")

res =  f.read()

res = res.replace("hi", "goodbye")
f.seek(0)

f.write(res)
f.close()


f = open("faylim2.txt", "r+")

res =  f.readlines()
k = open("Yangi_fayl.txt", "w+")
for i in res :
    if "myself" in i:
        k.write(i)
print(k.read())  
k.close()

f.close()



import os

os.mkdir("practise_dir2/file_inside_practdr")


import os 

os.chdir("practise_dir")

with open("testcase.txt", "w") as f:
    f.write("ali, vali")
    
print(os.path.exists("practise_dir/testcase.txt"))




import os 
old = input("Eski fayl = ")
yangi = input("Yangi fayl = ")

try:
    os.rename(old, yangi)
except FileNotFoundError():
    (f"Eski fayl nomini to`g`ri kiriting, bu {old} nomdagi fayl topilmadi !!!")
except FileExistsError():
    (f"{yangi} bu nomda fayl ochib bo`lingan. O`zgartiring !!!")
    

from pathlib import Path 


print(Path().home())



from pathlib import Path

Path.mkdir("./temp_file")

'''

from pathlib import Path  

Path.write_text("temp_file/greet.txt", "hello ")
