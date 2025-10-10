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
 '''  
 
 
def isprm(son):
    for i in range(2,int(son**0.5)+1,1):
        if son%i==0:
            return False
print(isprm(3))




            
