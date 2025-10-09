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
print(x<5 or x<4)'''
#print(bool("'"))

x = int(input("x "))
#if x > 10 : print("Eshmat") else :  print("Toshmat")
print("eshmat") if x>10 else print("toshmat")

'''

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
print(res)'''
            
def ds_pet(name:str, **details)->None:
    return name, details
res = ds_pet("kuchuk", nomi="mushuk")
print(res)


print("hello")
