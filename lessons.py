#str1 = "Mening ismim Eshmat emas, Toxir"
#print(str1)

#my_infolar = """Mening ismim Toxir
#Yoshim 20 da
#Backend 6 da o`qiyman!"""
#print(infolar)

#print(my_infolar[23])

Uzbekistan = " O'zbekiston kelajagi buyuk davlat! "
'''if "buyuk" in Uzbekistan:
    print("bor")
else:
    print("yo'q")'''
#print(Uzbekistan[-9:-1])

'''print(10>9)
print(11<9)
print(10==10)

print(bool("Ehsmat"))
print(bool(15))

print(10%3, 10/3, 10//7)
x: int = 10
print(x<5 and x<10)
print(x<5 or x<4)
#print(bool("'"))

x = int(input("x "))
#if x > 10 : print("Eshmat") else :  print("Toshmat")
print("eshmat") if x>10 else print("toshmat")


person: dict = {
  name : "John",
  age: 21,
  city:"London"
}
# qo`shtirnoqlar    GET methodi  update 

fruits = ["olma", "olcha", "banana", "ananas"]
fruits2 = [12, 15, 20, 17]

#lugat = {i:j for i, j in fruits fruits2}
lugat = {i: j for i, j in zip(fruits, fruits2)}
print(lugat)

print(lugat)


dc = {
"eshmat": {"math":45, "science": 60}, "toshmat": {"math":50, "science": 70}}

for key, _ in dc.items():
    print(key)
for i in dc.values(values()):
    print(i)


def count_vowels(word: str)->str:
    vowels = "aeuio"
    return vowels in word
res = count_vowels("assalom")
print(res)  CHALA
20
def pos_num(son:int) ->bool:
    poss=list()
    for i in son:
        if i > 0:
            poss.append(i)
    return poss
res = pos_num((1, 2, -3, 5, -9))
print(res)
            
def ds_pet(name:str, **details)->None:
    return name, details
res = ds_pet("kuchuk", nomi="mushuk")
print(res)


print("hello")



from typing import Callable 

def funk1(f: Callable):
    def ichki(*arg, **kwarg):
        print("starting...")
        f()
        print('done')
    return ichki
    
    
@loggger.funk1   
def funk2(*arg, **kwarg):
    print(arg, kwarg)

        
funk2(5, a=12) 


def decorator(funk):
    def wrapper(*arg, **kwargs):
        ret = funk(*arg, **kwargs)
        print(ret.upper())
    return wrapper
    
@decorator                                              o`xshadi 
def say(s:str):
    return "Salom "+s
    
say("Xayot")




def decorator(funk):
    def wrapper(s: str):
        if s == "":
            print("Not found")
            return
        else :
            print(s)
            return
        funk(s)
    return wrapper      
@decorator         
def string(s):
    print(s+ " here is my boy")
    
string("h")




def decorator(funk):
    def negative(son: int):
        if son<0:
            
            print(f"{son} is negative")
            return
        else:
            print(f"{son} is positive")
            return
        negative(son)
        son_ol(son)
    return negative

@decorator 
def son_ol(son):
    print(son**2)

son_ol(5)







def decor(funk):
    def wrapper(*args, **kwargs):
        l = args[0]
        ls = sorted(l)
        funk(ls)
    return wrapper
        
@decor
def funksiya(*args, **kwargs):
    print(args)

funksiya((1, 2, 4, 3, 7, 4))
'''

"""Create a decorator that counts how many elements in a list argument satisfy a certain condition (eg even numbers).
    
    Write a decorator that removes None values from list arguments before calling the function.
    Write a decorator that reverses all string arguments passed to the function.
    Create a decorator that multiplies a numeric return value by 10.
    Write a decorator that wraps a function’s string result in parentheses.
    Write a decorator that converts a function’s return type:
    if list → tuple if tuple → list
    Create a decorator that joins the characters of a string return value with -.
    Write a decorator that returns a sorted version of any iterable returned by the function.
    Write a decorator that applies a given lambda to every element of a list returned by the function.
    Write a decorator that adds "Hello, " before and "!" after a string return value.
    Write a decorator that doubles each element in a list returned by the function.
    Write a decorator that converts a dictionary’s values to uppercase if they are strings.
    Create a decorator that, when the function returns a list of numbers, filters out the odd ones 
    
17

def decorator(funk):
    def wrp(*args, **kwargs):
        funk()
        cnt = 0 
        for i in args:
            if i %2 ==0:
                cnt +=1
        print(cnt) 
    return wrp
        
@decorator         
def mainf(*args, **kwargs):
    print(args)
    
mainf([1, 2, 3, 4 ,5])


def dec(fun):
    def wrp(*args):
        for i in args:
            if i is None:
                return False
            else : 
                return fun()
    return wrp 


@dec 
def main(*arg):
    print(arg)

main([], [1, 2,3],())



#Create a decorator that multiplies a numeric return value by 10.

def dec(funk):
    def wrp():
        return res * 10
        
    return wrp
@dec 
def main():
    print(10)
    
main()
=======================================================================================================
                    TRY EXCEPT 
=======================================================================================================
1 
try:
    a = int(input("a ni :"))
    b = int(input("b ni :"))
    print(a/b)
except ZeroDivisionError:
    print("Nolga bo`la olmaysiz")
except ValueError:
    print("Son turida muammo bor") 


2 
try:
    ls = map(list(int, input()))
    def main(ls):
        for i in ls:                            CHALAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            print(i**(-1))
        return main
except ValueError:
    print("Nol mumkinmas")



def invert(l:list):
    res=[]
    for i in range(0, len(l)):
        try:
            res.append(l[i]**(-1))
        except ZeroDivisionError:
            print(f"l[{i}] = 0 ekan, chopdim!")
            continue
    return res
print(invert([1, 2, 3, 4, 5]))
print(invert([1, 0, 3, 4, 5]))

4 
def invert(l:list):
    res=[]
    for i in l:
        if i :
            try:
                res.append(int(i))
                continue
            except ValueError:
                print(f"string ekan")
                continue
    return res
print(invert(["1", "2", "stringcha", "4"]))


5 
while True:
    try:
        a = int(input("Son kiriting "))
        print(f"Son = {a}")
        break
    except ValueError:
        print("Xatolik")



def dec(fun):
    def wrp():
        try:
            for i in range(3):
                print(f"{i} chi urinish")
                fun()
        except ZeroDivisionError:
            print("Xatolik")
        
@dec
def main(a:int, b:int):
    print(a/b)
    
main() 



43



def safe_call(funk):
    def wrp():
        try:
            funk()
        except ZeroDivisionError:
            print("Div by 0 not allowed ")
        except Exception as er :
            print("Error", type(er))
    return wrp()  
@safe_call
def myf():
    print(12//0)
    
    
    
44    
      
def val_arg(funk):
    def wrp(*args):
        for i in args:
            if not isinstance(i, int):
                raise TypeError("Son int emas ")
        funk(*args)
    return wrp
    
    
@val_arg
def summm(*arg):
    r = sum(arg)
    print(r)

summm(1, 2, 3, 4, )
 
45 

def con_ex(funk):
    def wrp(**kwrg):
        try:
            funk()
        except KeyError as e:
            raise ValueError(e)
    return wrp
    
@con_ex 
def main():
    d = {}
    print(d["hi"])
    
main()



def cond(a):
    def main(func):
        def wrp():
            if a == True
                return func(b*2)
            else a == False :
                return func(b//2)
        return wrp
    return main
    
@cond(True):
def my_f(b):
    return b    
    
print(my_f(b)) 



f =open("faylim.txt", "w")

f.write("Toxir\n") 

f.close()
 
f = open("faylim.txt", "r")

print(f.read())

f.close() 


f = open("faylim.txt", "a+")

print(f.read())
f.write("Guliston")
print(f.read())

f.close() 


f = open("faylim.txt", "r")
res = f.read()
cnt = 0
for i in res:
    if i == "\n":
        cnt+=1
        
print(cnt )
f.close()


f = open("faylim.txt", "r")
res = f.read()
cnt = 0
for i in res:
    if i == " " or i == "\n":
        cnt+=1
        
print(cnt)
f.close()

f = open("faylim.txt", "r")
res = f.read()
cnt = 0
for i in res:
    if i != " " or i != "\n":
        cnt+=1
        
print(cnt)
f.close()


f = open("faylim.txt", "r")
res = f.read()
f = open("faylim2.txt", "r+")

f.write(res)

print(f.read())


f = open("faylim.txt", "r")
res = f.read().split()

print(len(res))

f.close()

f = open("faylim.txt", "a+")

print(f.read())
f.write("Guliston")
f.seek(0)
print(f.read())

f.close()


f = open("faylim2.txt", "r")

res2 = f.read()

k = open("faylim.txt", "r")

res = k.read()

f3 = open("faylim3.txt", "w+")
f3.write(res)
f3.write(res2)


f3.seek(0)
print(f3.read())

f3.close()
k.close()

f.close() 


============================================================
                    WITH
============================================================
with open("faylim.txt", "r") as f:
    print(f.read())
print(f.closed)



with open("Yangi_fayl.txt", "w+") as f:
    f.write("1 chi qator \n")
    f.write("2 chi qator\n")
    f.write("3 chi qator")
    
    


with open("faylim.txt","r") as f:
    if f.read() != " ":
        raise ValueError("QANDAYDIR XATOLIK")
print("yopiqmi : ", f.closed) 


import os

print(os.getcwd()) 


import os

os.mkdir("Hello.txt")
os.chdir("/Hello.txt")


import os

os.rename(/)

===============================================
            pathlib
=============================================
from pathlib import Path



Path.write_text( Path("./Yangi_fayl.txt"),"hello world")

from pathlib import Path 

for path in Path.iterdir(Path("../Python_work")):
    print(path)





=======================================================================================================
                                            O O P
=======================================================================================================


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"brand = {self.brand}, model = {self.model}"
my_car1 = Car(
    brand = 'bmw',
    model = "bmw4 competition"
)

    
my_car2 = Car(
    brand = "chevrolet",
    model = "spark"
)


print(my_car1,"\n", my_car2) 


class Humankind: 
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Ismi {self.name}, yoshi esa {self.age}"
        
odam1 = Humankind(name = "Eshmat",age = 12)

odam2 = Humankind(name = "Ali", age = 55)

print(odam1,"\n", odam2)


class Book:
    def __init__(self, name, auth):
        self.name = name
        self.auth = auth
        
    def __str__(self):
        return f"name {self.name}, auth {self.auth}"
        
        
    @classmethod
    def unknown(cls):
        return cls("Unknown", "unknown")
        
        
        
book1 = Book("kitob1", "auth1")
book2 = Book("kitob2", "auth2")

print(book1, book2)

print(Book.unknown())


class Soon:
    def __init__(self, son):
        self.son = son
        
    def __str__(self):
        return 
        

        
        
class Cat:
    def __init__(self, name):
        self.name = name
        
        
class Dog :
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"
 
 
dog = Dog("Bobik") 

print(dog)
print(isinstance(dog, Dog))
        


====================================================================================================
                    INHERITANCE
=====================================================================================================


class Animal:
    def __init__(self, ovoz):
        self.ovoz = ovoz
    def speak(self):
        return f"{self.ovoz}  bu ovoz."
 
class Dog(Animal):
    def speak(self):
        print("woow")                                                                     ??????????????
class Cat(Animal):                                          ////////?????????????????
    def speak(self):
        print("miov")
 
 
        
print(dog1 = Dog("wow-wow"))
print(cat1 = Cat("miyav-miyov"))
 
 class Vehicle:
    def __init__(self, name, brand, color):
        self.name = name
        
        CHALAAAAAAAAAAAAAAAAAAA
        
        
        
"""

        
import sys
import module 



print(sys.modules)
print("++++++++++++")
print(sys.path)       
        
        
        
        
        
        
