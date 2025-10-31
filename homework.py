''' Create a tuple numbers containing the integers 1, 2, 3, 4, 5.
    Access and print the third element of the numbers tuple.
    Find the length of the numbers tuple.
    Try to change the first element of numbers to 10. What happens?
    Create a tuple fruits with the elements 'apple', 'banana', 'cherry'.
    Check if 'banana' exists in the fruits tuple using an if statement.
    Use a for loop to print each fruit in the fruits tuple.
    CREATE A NEW TUPLE COMBINED BY JOINING NUMBERS AND FRUITS.-----
    Count how many times the number 3 appears in a tuple like (1, 2, 3, 3, 4).
10  UNPACK THE TUPLE ('RED', 'GREEN', 'BLUE') INTO THREE SEPARATE VARIABLES.
    Create a tuple colors with three colors. Use a for loop to print each color along with its index.
    Create a tuple with a single element, ('single',).
    WRITE A PROGRAM TO FIND THE MAXIMUM VALUE IN A TUPLE OF NUMBERS (10, 5, 20, 15).
    Use a while loop to print the elements of the tuple ('a', 'b', 'c').
15  Create a nested tuple my_data = (('John', 25), ('Jane', 30)).
    Access and print the age of 'John' from my_data.
    Convert the list ['milk', 'bread', 'eggs'] into a tuple.
    Check if a tuple is empty using an if statement.
    Write a program that takes a number and checks if it is present in the tuple (2, 4, 6, 8, 10).
    Create a tuple of squares for numbers from 1 to 5 without using a comprehension.
#1
my_tuple =(1, 2, 3, 4, 5)
#2 
my_tuple = (1,2,3,4,5,6)
print(my_tuple[2])
#3
my_tuple = (1,2,3,4,5,6)
print(len(my_tuple))
#4 Tuple does not support item assigement
my_tuple = (1,2,3,4,5,6)
#my_tuple[0]= 10
print(my_tuple)
#5 
fruits = ('apple', 'banana', 'cherry')
print(fruits)
#6
fruits = ('banana', 'apple', 'cherry', 'grape', 'peach', 'melon')
print(True) if 'banana' in fruits else print(False)
#7
fruits = ('banana', 'apple', 'cherry', 'grape', 'peach', 'melon')
for meva in fruits :
    print(meva)
#8
#9
numbers = (1, 2, 3, 3, 4, 3, 5, 18, 8)
cnt= 0
for i in numbers:
    if i == 3:
        cnt = cnt + 1
print(cnt)
#10
#11 CHALA 
colors = ("red", "blue","green")
for i in colors:
    print(i)# "the color's index is ", 
#12
One_element = ("element one")
print(One_element)
#13
nums = (10, 5, 20, 15)  
maks = 0
for i in nums:
    if i > maks :
        i == maks
    else : 
        i != maks
print(maks)
#14
letters = ('a', 'b', 'c', 'd')
for i in letters:
    print(i)
#15
classroom = (("Eshmat", 19, 4.2, "idx0712"), ("Gulpari", 18, 4.8, "idx1285"), ("Toshmat", 20, 4.7, "idx0572"))
print(classroom)
#16
classroom = (("Eshmat", 19, 4.2, "idx0712"), ("Gulpari", 18, 4.8, "idx1285"), ("Toshmat", 20, 4.7, "idx0572"))
print(classroom[1][1], "yoshda")
#17
this_list = ['milk', 'bread', 'eggs']
print(type(this_list))
this_new_tuple = tuple(this_list)
print(type(this_new_tuple))
#18
tuplee = ()
if tuplee == "":
    print("empty")
else :
    print(False)
#19
numbers = (2, 4, 6, 8, 10)
son = int(input("kerakli sonni yozing : "))
for i in numbers:
    if son == i:
        print(son,"shu yerda!")
        break
    else : 
        print(son, "ketib qolibdi?!")
        break
#20
powers = ()
for i in range(1,6):
    powers(i**2)
print(powers)




---------------------------------------------------------------------------------------------------------------
ABOVE SECTION IS ABOUT TUPLES
--------------------------------------------------------------------------------------------------------------- 

 Create a set unique_numbers with the elements 1, 2, 3, 4, 2. Print the set.
    Add the number 5 to the unique_numbers set.
    Add multiple numbers, 6 and 7, to the set.
    Remove the number 3 from the set.
    TRY TO REMOVE A NUMBER THAT DOESN'T EXIST, LIKE 10, USING THE DISCARD() METHOD.
    Use an if statement to check if the number 4 is in the set.
    Create two sets: set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}.
    Find and print the union of set1 and set2.
    Find and print the intersection of set1 and set2.
    Find and print the difference between set1 and set2.
    Convert the list [1, 1, 2, 3, 3, 4] into a set to find all the unique numbers.
    Use a for loop to iterate through a set and print each element.
    Write a program that uses if-else to determine if a number is present in a set.
    Check if set1 is a subset of a new set set3 = {1, 2, 3, 4, 5}.
    Check if set3 is a superset of set1.
    Write a program to find the unique elements in a list ['a', 'b', 'a', 'c', 'b'] using a set.
    Clear all elements from a set.
    Ask a user for three of their favorite colors and store them in a set.
    Find the symmetric difference between set1 and set2.
    Create a set of even numbers from 1 to 10.
#1
unique_numbers = {1, 3, 2, 4, 2,}
print(unique_numbers)
#2
unique_numbers = {1, 3, 2, 4, 2,}  #add funksiyasini ishlat set da 
print(unique_numbers)
unique_numbers.add(5)
print(unique_numbers)
#3
unique_numbers = {1, 3, 2, 4, 2,}  #add funksiyasini ishlat set da 
print(unique_numbers)
#unique_numbers.add(6, 7, 9) # faqat 1 ta qo`shsa bo`larkan 
for i in range(6, 8):
    unique_numbers.add(i)
print(unique_numbers)
#4
unique_numbers = {1, 3, 2, 4, 2,}
unique_numbers.remove(3)
print(unique_numbers)
#5
#6
unique_numbers = {1, 3, 2, 4, 2,}
if 4 in unique_numbers : 
    print(True)
else : 
    print(False)
#7
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}
print(set1, set2)
#8
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}
print(set1.union(set2))
#9
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}
print(set1.intersection(set2))
#10
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}
print(set1.difference(set2))
print(set2.difference(set1))

 ----------------------------------------------------------------------------------------
ABOVE SECTION IS ABOUT SETS
---------------------------------------------------------------------------------------- 

1Get the number of key-value pairs in the dictionary.
2Create a copy of a dictionary.
3Use the get() method to access a key, providing a default value if the key doesn't exist.
4Use the setdefault() method to add a new key only if it doesn't already exist.
5Count the frequency of characters in a string and store them in a dictionary.
6Count the frequency of words in a sentence and store them in a dictionary.
7Invert a dictionary, so that the values become keys and the keys become values (handle duplicate values by storing them in a list).
8Sort a dictionary by its keys and print the sorted dictionary.
Sort a dictionary by its values and print the sorted dictionary.
Problem Solving
Write a function that takes a dictionary and returns True if all values are unique, otherwise returns False.
Find the key with the maximum value in a dictionary.
Find the key with the minimum value in a dictionary.
Remove all key-value pairs where the value is an empty string.
Create a dictionary where keys are numbers from 1 to 10 and values are 'even' or 'odd'.
15Given a list of dictionaries, find the dictionary with the highest value for a specific key.
16Use pop() to remove a specific key and return its value.
17Zip two lists, one for keys and one for values, to create a dictionary.
Write a function that takes a dictionary and a list of keys to remove. Remove the specified keys from the dictionary.
18Check if two dictionaries are equal.

#1
students = {"Ali":{"math": 5, "bio":4.7}, 
"Vali":{"math": 4.9, "bio":4.8}}
cntr = 0
for i in students.keys():
    cntr +=1
print(cntr)

#2
students = {"Ali":{"math": 5, "bio":4.7}, "Vali":{"math": 4.9, "bio":4.8}}
other_students = {}
other_students = students.copy()
other_students.update({"Eshmat":{"math":4.4, "bio":4.6}})
print(students,"\n", other_students)
#3 chala
students = {"ali": 3.4, "vali": 3.5, "eshmat":3.8}
name = input(("N = "))
if name.lower() in stustudendents:
    print(students.get(name)) 
else :
    print("It seems they are not here!")
#4
students = {"Ali":{"math": 5, "bio":4.7}, "Vali":{"math": 4.9, "bio":4.8}}
ism = input("name : ")
if ism not in students:
    students.setdefault(ism, {"math": 0, "bio": 0})
    print(students)
else : 
    print("Borku bu")
#5 Ustozga aytamizmi yo`mi ?!
royxat = [{"olma": 3, "anjir":2,"nok":5}, {"olma": 7, "anjir":3,"nok":1} , {"olma": 4, "anjir":6,"nok":3} ]
kiy = input("Meva : ")
for i in royxat :
    if kiy in royxat:
        mva = 0
        if kiy > mva :
            mva = kiy
            print(mva)
else : 
    print("meva yo`q")



def funk(**kwargis)->bool:
    for i in kwargis.items():
        for j in range(kwargis.items():
            if i == j:
                return False


f = funk(a = 2, b = 12, c = 7)
print(f)

==========================================================================================================
    FUNKSIYALAR ---------------------------------------------------------------------------- FUNCTIONS
==========================================================================================================

#25
def averg(*sonlar):
    all_s = 0
    cnt = 0
    for i in sonlar:
        all_s +=i
        cnt +=1
    return all_s//cnt
r = averg(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(r)

#26
def out_kwargs(**diktion):
    return diktion
r = out_kwargs(ism = "ali", yosh = 22, maktab = 11, uy = "yunusobod, obodgul ko`cha 12-uy")
print(r)

#27
def infoo(*args, **kwargs):
    return args, kwargs
r = infoo(1, 2,3 ,19, -38, "alixo`ja", "x`ojali", yosh = 12, ism = "ali")
print(r)
    
#28
def mulORsum(*args, **operat):
    alls = 0
    alls2 = 1
    for i in operat.values():
        if i == "sum":
            for j in args:
                alls +=j
        elif i == "mult":
            for j in args:
                alls2 *=j
    if alls>alls2:
        return alls
    else :
        return alls2
r = mulORsum(1, 2, 4, 5, ishora = "mult")
print(r)

#29
def cust_greet(name, **kwargs)

return 





r = cust_greet("Eshmat", vaqt="Xayrli kun", belgi="!!!")
print(r)

#30
def senten(*words, sep=" "):
    dft = set()
    for i in words.index(0):        almost same
        dft.add(i)
        return dft
r = senten("Hi","my", "name", "is", "Eshmat")
print(r)


#31
def sqrs(*nums):
    ls=list()
    for i in nums:
        ls.append(i**2)
    return ls
r = sqrs(3, 2, 3, 3.1)
print(r)

#32
def swipp(**my_dikt):
    ds = dict()
    for k, v in my_dikt.items():
        ds[v]=k
    return ds
print(swipp(ism="ali", yosh=21))

#33
def com_el(set1, set2):
    return set2 - set1
print(com_el({"olma","nok"}, {"olma","nok", "limon"} ))


#34
def lst_tup(lst):
    t = tuple(lst)
    return t
print(lst_tup([1,23, -37,35, 39]))


#35


#36
def evens(*numbers):
    l = list()
    for i in numbers:
        if i % 2 ==0:
            l.append(i)
    return l
print(evens(1, 2, 3, 4, 5, 88))


#37

def longest(*words):
    temp_l = list()
    mx = 0
    for i in words:
        if i[::].len()> mx:
            mx = i
            temp_l.append(i)
    return temp_l
    
print(longest("hi", "hello", "mexanizatsiyalashtirilmaganligidandurda"))
  
  
#38

def dicts(**d1, **d2):
    return d1 + d2
    
print(dicts{"nok":3, "anjir":1}, {"olma":1, "o`rik":4})
  


#39
def u_cnt(lst):
    cnt = 0
    for i in lst:
        cnt+=1
        if lst[i]
          
#funk2_2
cnter = 0
def increment():
    global cnter
    cnter +=1
    return cnter
print(increment())
print(increment())
print(increment())
    
#funk2_3

name = "outer"

def somfunk():
    name = "inner"
    return name
print(name, somfunk())


#funk2_5
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "changed"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()


#funk2_7

x = 6
print(x)   #ozini qaytardi
def sett():
    global x
    x = 19
    print(x)   # 19 ni
sett()
def restt():
    global x
    x = 22
    print(x)  #22 ni 
restt()
print(x)   # x ni oxirgi qiymati 22 bolgani un 22 ni 




#funk2_8

def increment():
    cnt = 0
    cnt +=1
    print(cnt)
increment()
increment()
increment()  # bir xil narsa qaytaryapti chunki cnt = 0 funksiya ichida xar safar shu qiymatni oladi

#funk2_9


def sum_and_print(a, b):
    total = a+b
    print(total)# 30
    return total
r = sum_and_print(12, 18) #30
print(r)
print(total) # NameError: name 'total' is not defined total localligi un

#funk2_10
x = 100
def test():
    x = 10 # before it the code outputs 100 'cause global vars can go to any funk and there was only one var, after local one created, it was main var for test() funk.
    print(x)
test()
print(x)


#funk2_11
                                                    
def out():
    print("Outer start")
    def inn():
        print("Inner start")
    inn()
out()

 
#funk2_12

def cal(a, b):
    def add():
        s = a + b
        print(s)
    add()
cal(12, 8)

#funk2_13
def greet(name):
    def hello():
        print(f"Hello dear {name} !!!")
    hello()
    def byee():
        print("Bye", name)
    byee()
greet("Eshmat")

#funk2_14

def outer():
    def inn1():
        print("I am 1st funk")
    def inn2():
        print("Nah, I am the 1st funk")
    inn1()
    inn2()
outer()

#funk2_15

def outer():
    def inn1():
        print("I am 1st funk")
    return inn1  #    it did not reply
   
def outer():
    def inn1():
        print("I am cool boy")
    return inn1() # it returns the text inside of inn1 func
outer()

 
#funk2_16
def matem(a, b):
    def suum():
        return a+b
    def mult():
        return a*b
    def sub():
        return a//b
    suum()
    mult()
    sub()
    return suum() , mult() ,sub()
print(matem(12, 4))
 
#funk2_17

def table(n):
    def shower():
        for i in range(1, n+1):
            print(f"{i}*{n} = ", n*i)
        
    shower()
# none qayerdan kelyapti 
print(table(5))
   
#funk2_18

def outer():
    message = "Hello"
    def inner():
        print(message)
    inner()
outer()  # it returns Hello

def outer():
    message = "Hello"
    def inner():
        nonlocal message 
        message = "Message is not \"Hello\" anymore"
        print(message)
    inner()
out er()


#funk2_19

def pr_list(lst):
    cnt=0
    for i in lst:
        cnt+=1
    def sum():
        s = 0
        for i in lst:
            s +=i
        return s
    return cnt, sum() 
print(pr_list([1, 2, 3, 4, 5, 6]))


#funk2_20
def outer():
    def inner():
        s = 12+3
        return s
    def inner2():
        s1=12+8
        return s1
    return inner(), inner2()
print(outer())
'''
#funk2_21


'''=====================================================================================================

                        SUPPORT HOMEWORK

======================================================================================================
#funs7

def revers(son):
    raq = 1
    while son > 0:
        raq=raq*10+son%10
        son//10
    return raq
  
print(revers(123))
====================================================================================
            TRY/EXCEPT 
======================================================================================
21 
def main(d:dict):
    try:
        for k, v in d.items():
            print(k, " ", v)
    except AttributeError:
        print("Not dikt")
main([1, 2, 3])  
    
   
   
24 

stds= {"ali": 4.5, "vali": 4.7, "guli": 4.97, "eshmat": 4.4}    
f = open("Student_db.txt", "w+")

for k, val in stds.items():
    f.write(k + " ")
    f.write(str(val))
    f.write("\n")
print(f.read())
f.close() 



25 
f = open("Yangi_fayl.txt", "w+")
res = f.read()

if "goodbye" in res:
    res.replace("goodbye", "hey")
f.seek(0)
f.write(res)

f.close() 


=====================================================================================
                                                        OOP                            
===============================================================================================


14 

class Book:

    def __init__(self,title, auth):
        self.title = title
        self.auth = auth
    
    def __str__(self):
        return f"<{self.title}> by <{self.auth}>"
    
book1 = Book("Days gone by", "A.Qodiriy")


print(book1)


15 

class Person:

    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"<{self.name}> by <{self.age}>"
    def __repr__
book1 = Book("Days gone by", "A.Qodiriy")


17

class Bank:

    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Owner is <{self.owner}>, and balance is <{self.balance}$>"
    
user = Bank("Eshmat", 12000)

print(user)

18/19

class School:
    school = "Greenwood High"
    def __init__(self,student,Gpa):
        self.student = student
        self.Gpa = Gpa
    def __str__(self):
        return f"student name {self.student}, Gpa {self.Gpa}"
std = School("eshmat", 4.7)

std1 = School("toshmat", 4.5)

print(std, std1, std.school)


20

class School:
    school = "Greenwood High"
    def __init__(self,student,Gpa):
        self.student = student
        self.Gpa = Gpa
    def __str__(self):
        return f"student name {self.student}, Gpa {self.Gpa}"
std = School("eshmat", 4.7)

std1 = School("toshmat", 4.5)

print(std, std1, std.school)

School.school = "Hogward wizards"
print(std, std1, std.school)




#   INHERITANCE   |||  POLYMORPHISM   |||  ENCAPSULATION   |||

6_ex 

class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"name : {self.name}, age : {self.age}"
    
    def speed(self):
        return "35 km/h "
    
class Xachiko(Dog):
    pass
dog1 = Xachiko("dogie", 2)

print(dog1)


7/8_ex

class Vehicle:
    def sound(ovoz: str):
        return "sound is here"
    

class Car(Vehicle):
    def sound(ovoz):
        return f"{ovoz}"
    
class Helicopter(Vehicle):
    def sound(ovoz):
        return f"{ovoz}"

print(Helicopter.sound("tftfttftffff"))
print(Car.sound("vmmmmmmmmmmmmm......"))


9_ex

class Appliance:
    def __init__(self, brand):
        self.brand = brand


class Wash_machine(Appliance):
    def __init__(self, brand, capacity):
        self.capacity = capacity
        super().__init__(brand)

Bosch = Wash_machine("bosch", 220)

print(Bosch.capacity)



10_ex

class Person:
    def __init__(self, name):
        self.name = name
        return f"Name: {self.name}"
    def __str__(self):
        return f"Name : {self.name}"

class Employee(Person):
    def __init__(self, name, salary):
        self.salary = salary 
        super().__init__(name)
    def __str__(self):
        return f"E`s salary :  {self.salary}, E`s name : {self.name}"

coder = Employee("JOhn", 1200)

print(coder)   


11_ex 

class Bird:
    def fly(self):
        print("I am flying ... yuhuuuu")

class Parot(Bird):
    def fly(self):
        super().fly()     #super class dan method chaqirganda uni child class dagi boshqa methodni ichiga yozish kerak 
        print("biz qondik")  

b1 = Parot()
b1.fly()


12/13_ex

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"NAME [{self.name.upper()}], age: {self.age} year-old"  
    
class Child(Parent):
    def __init__(self, name, age, height, status):
        self.height = height
        self.status = status
        super().__init__(name, age)

   # def __str__(self):
   #     return  f"NAME [{self.name.lower()}], Age: {self.age} years old, height - {self.height}, status - {self.status}"

Guy = Child("Max", 20, 178, "student")

print(Guy)


14_ex

class Tree:
    def __init__(self, name):
        self.name = name
    def get_info(self):
        print(f"{self.name}")

class Archa(Tree):
    def __init__(self, name):
        super().__init__(name)

archa = Archa("Yangi_yil_daraxti")

archa.get_info()
print(archa.name) 

15/16_ex 

class Animal:
    pass
class Mammal(Animal):
    pass
class Dog(Mammal):
    pass

print(issubclass(Dog, Mammal))  #True     
print(issubclass(Dog, Animal))  #True

print(isinstance(Dog, Mammal))  #False
print(isinstance(Dog, Animal))  #False

17_ex

class Animal:
    pass
class Mammal(Animal):
    pass
class Dog(Mammal):
    pass

dog = Dog()

print(isinstance(dog, Dog))     #True
print(isinstance(dog, Mammal))  #True
print(isinstance(dog, Animal))  #True

# Issubclass means -> {Is that class child of That class ?}
# Isinstance means -> {Is that object belongs to That class ?}  answer type is boolean



18_ex

class Emee:
    def describe(self):
        print("Good employee, works honestly")
class Manager(Emee):
    def describe(self):
        print("He is the best employee in our company, we proud of him!")

Tom = Manager()

Tom.describe() 



19_ex

class Shape:
    def __init__(self, n):
        self.n = n
    def area(self):
        return self.n
class Circle(Shape):
    def area(self):
        return self.n*self.n*3.1415
    
class Square(Shape):
    def area(self):
        return self.n*self.n 
    
circ = Circle(3)
sqr = Square(3)

print(circ.area())
print(sqr.area())

20_ex 

class Device:
    def status(self):
        return "it is device"
class Phone(Device):
    def status(self):
        print("It is phone`s.....status")

class Laptop(Device):
    def status(self):
        print("It is laptop`s....status")

redmi = Phone()
vivo = Laptop()

redmi.status()
vivo.status()

21_ex 


class  Flyer:
    def move(self):
        print("Flying..")
class Swimmer:
    def move(self):
        print("Swimming..")

class Duck(Swimmer, Flyer): # class can get first classes method
    pass

duck = Duck()
duck.move()   # It depends the order of class`s parent class`s  


23_ex

class Dog:
    def sound(self):
        print("woow, woow")

class Cat:
    def sound(self):
        print("miauv, miauv")

class Dat(Dog, Cat):
    pass

print(Dat.__mro__)
 
24_ex

class Logabe:
    def log(self):
        print("Logging...")

class Database:
    def saver(self):
        print("saving...")

class LogBase(Logabe, Database):
    def __init__(self):
        super().__init__()
f = LogBase()
f.log()
f.saver()
# bith of them working......


25_ex

class Animal:
    def __init__(self,name):
        self.name = name

    def nam(self):
        return self.name.lower()
class Mammal:
    def __init__(self, name):
        self.name = name
    def nam(self):
        return self.name.upper()
    
class Mamont(Mammal, Animal):
    def __init__(self, name):
        super().__init__(name)

fil = Mamont("FIlcha")

print(fil.nam())

#again it depends the order that given in third class`s parenthses

26_ex

class A:
    def msg(self):
        print(f"This is {self.__class__.__name__} class")

class B(A):
    def msg(self):
        print(f"This is {self.__class__.__name__} class")

class C(A):
    def msg(self):
        print(f"This is {self.__class__.__name__} class")

class D(B, C):
    pass

print(D.__mro__)  

27_ex_v1

class A:
    def msg(self):
        print(f"This is A class")

class B(A):
    def msg(self):
        print(f"This is B class")

class C(A):
    def msg(self):
        print(f"This is C class")

class D(B, C):
    pass


d = D()

d.msg()

27_ex_v2

class A:
    def msg(self):
        print(f"This is {self.__class__.__name__} class")

class B(A):
    def msg(self):
        print(f"This is {self.__class__.__name__} class")

class C(A):
    def msg(self):
        print(f"This is {self.__class__.__name__} class")

class D(B, C):
    pass

d = D()
b = B()
c = C()
d.msg()
c.msg()
b.msg()



28_ex '''

