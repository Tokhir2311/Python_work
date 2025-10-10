'''son = int(input("Sonni yozing: "))
if son>0 :
    qiymat= son+1
    print(qiymat)
else : 
	print(son)
	
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

s = int(input())
if s>0:
    print(s+1)
else:
    print(s-2)

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

s = int(input())
if s > 0 : 
    print(s+1)
elif s == 0:
    print(10)x 
else : 
    print(s-2)
    
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

x = int(input())
y = int(input())
z = int(input())
if(x>0 and y>0 and z>0) :
    print(3)
elif((x>0 and y>0 ) and z<0):
    print(2)
elif((y>0 and z>0) and x<0):
    print(2)
elif((z>0 and x>0) and y<0):
    print(2)
elif(x>0 or y>0 or z>0):
    print(1)
else : 
    print(0)
    
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

-------------------------------------------------------------------------------------------BOOL
1
a = int(input())
b = bool(a)
if b == True :
    print("A musbat son") 
2

a = int(input())
print("A toq son") if a%2 != 0 else print("juftku")
    
3 
a = int(input())
print("A juft son") if(a%2==0) else print("A toq son")

4 
a= int(input())
b= int(input())
if(a>2 and b<=3) :
    print(True)
else : print(False)

6 
a = int(input())
b = int(input())
c = int(input())
if(a<=b<=c) :
    print(True)
else : 
    print(False)
    
7 
a = int(input())
b = int(input())
c = int(input())
if(b>a and b<c) :
    print(True)
else : 
    print(False)
    
11 
a = int(input())
b = int(input())
if((a%2==0 and b%2==0) or (a%2 !=0 and b%2!= 0)) :
    print("a va b ni ikkalasi yo toq yo juft")
else :
    print("idonno")

14
a = int(input())
b = int(input())
c = int(input())
if((a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0)) :
    print("Kamida bittasi musbat")
    
17 
a = int(input())
if(a%2!=0 and (a>99 and a<1000)) :
    print(True)
else : 
    print(False) 
    
18 
a = int(input())
b = int(input())
c = int(input())
if((a == b) or (a== c) or (b==c)) :
    print(True)
    
20 
a = int(input())
b = a%10
c = (a%100-b)//10
d = (a%1000-c-b)//100
if(d!=b and d != c and c!=b ) :
    print(True)
else :
    print(False)  

INTEGER $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
1 
a = int(input())
print(a//100, "m",a%100,"sm") 

4 

a = int(input())
b = int(input())
print(a//b)

5 
a = int(input())
b = int(input())
print(a//b,a%b )

13 

a = int(input())
print(a%100*10+a//100)


24 
---------------------------------------------------------------------------------------------begin
9 

import math
a = int(input())
b = int(input())
print(math.sqrt(a*b))

13

PI = 3.141509
R1= float(input())
R2 = float(input())
print(PI*(R1*R1-R2*R2))

17 
a = int(input())
b = int(input())
c = int(input())
BC = c-b
AC = c-a
print(BC, 'BC KESMA', AC ,'AC KESMA', BC+AC, 'YIG`INDI') 
20 
import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

S = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
print(S) ********************************************************************************************************************

x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if(x == x1 or y == y1) : 
    print("Bo`ladi")
else : 
    print("Bo`maydi")
    
    


c = 39
while True : 
    a = int(input())
    b= int(input())
    print("Guess what : ")
    num = input())
    if c > num :
        print("Higher than this")
    elif c < num: 
        print("Lower than yours ")
    else :
        print(" Right " )
        break
    
    
string = input("matn : ")
karakter = input("char : ")
i = 0
cnt = 0
while i<len(string): 
    
    if string[i] == karakter :
        i=i+1
        cnt = cnt+1
print(cnt)
        
        
otni yurishi
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
  
ox = abs(x1-x2)
oy = abs(y1-y2)
res = (ox ** 2 + oy ** 2 == 2 or ox ** 2 + oy ** 2 == 1) and (ox ** 2 + oy **2 != 0)
print(res)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
ox = x1-x2
oy = y1-y2
yig = ox ** 2 + oy ** 2 
print(yig == 1 or yig == 2) and (yig != 0)


a = input()
i = 0
while i < len(a):
    if ord(a)+3>90 :
        a = chr(ord(a)-26)
    else : 
        a = chr(ord(a)+3)
    
print(chr(ord(a)+ 3))
   
n = input()
i = 0
sum = 0
son = int(n)
while i < len(n) :
    i=i+1
    sum = sum + son%10
    son = (son)//10
print(sum) 
    






#n = int(input())

n=10
sl = list()
while n > 3:
   s = n//3
   sl.append(s)
cnt = 0
for i in sl:
    cnt +=i
print(cnt)


#funk3_6
def safe_divide(a, b):
    return a//b
    
def error_handler(a, b):
    return "False"

def run_ifsafe(func, handler, a, b):
    if (b!=0):
        return  func(a, b)
    else :
        return handler()
     
print(run_ifsafe(safe_divide, error_handler, 4, 2))'''


