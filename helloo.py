#1 Classic "hello world!"
# print("Hello World!")

#2 Ask the user for their name and print a greeting that includes their name, e.g., "Hello, [Name]!".
#name = input("What is your name : ")
#print("Greetings ",name," from Eshmat!")

#3 Ask the user for their first name and last name, then print them on the same line.
# NameofUser = input("Your name please? ")
# print(f"Welcome, {NameofUser} .")

#4 Print the numbers 1, 2, and 3 on a single line, separated by commas. Use the sep parameter.

# print("1", "2", "3", sep=",")

#5 Print "Python" and "is" on the same line, and "fun" on the next. Use the end parameter to control the output.
#print("Python ", end=" ")
#print("is")
#print("fine")

#6 Ask the user for their age and print a sentence that states their age.
#age=input("your age: ")
#print(f"Your age is {age}!")

#7 Print the word "Welcome" centered in a field of 20 characters, with asterisks as a fill character.
#print("Welcome".center(20, "*"))


#8 Ask the user for a word and a number. Print the word that many times on a single line.
#word=input("Word: ")
#num=int(input("Num: "))
#res = word * num
#print(res)

#9Use an f-string to print a message that includes the value of a variable.
#age: int = 7
#print(f"Ticket is free for {age} year-old children")

#10Print the words "A", "B", and "C" each on a new line.
#print(" A\n", "B\n", "C")


#Varaibles -----------------------------------------------------------------


#1Create a variable called my_number and assign it the integer value 10. Print the variable.
#my_number: int =10
#print(f"My var is {my_number}.")

#2Create a variable my_decimal and assign it a floating-point value like 3.14. Print its data type.
#my_decimal: float = 2.72
#print(type(my_decimal))

#3Create a boolean variable is_true and set it to True. Print a message that includes this variable.
#is_true = True
#print(f"There are 4 oceans in the Earth, this fact is {is_true}!")

#4Store your name in a variable name and your age in a variable age. Print a single sentence using both variables.
#my_name = "Toxir"
#my_age = "20"
#print(f"Hi there! My name is {my_name}, and I'm in my {20}s")

#5Create three variables x, y, and z and assign them different integer values on a single line.
#x, y, z = 12, 17, 22
#print(x, end=" ")
#print(y, end=" ")
#print(z)

#6Assign the value of one variable to another, for example, a = 5, b = a. Print b.
#a = input('name ')
#b = a
#print(f"{a} it is copy of your name from var b ")

#7Store the string "123" in a variable. Convert it to an integer and print its new type.
#a = '123'
#b = int(a)
#print(type(b))

#8Ask the user to enter a number as a string, convert it to an integer, and store it in a variable. Print the variable.
#Num_str = input("enter number ")
#Num_int = int(Num_str)
#print(Num_int, "<--it is integer")

#9Create a variable pi with the value 3.14159. Print a message saying "The value of pi is [pi].
#pi = 3.14159
#print(f"The value of pi is {pi}, we use it to find circle's surface")

#10Swap the values of two variables, a and b, without using a temporary variable.
#a=9
#b=12
#a, b = b, a
#print(f"a= {a}, b= {b}")

#Arithmetic------------------------------------------------------------------

#1Declare two variables, num1 = 15 and num2 = 4. Print their sum.
#num1 = 15
#num2 = 4
#print("Their sum: ", num1+num2)

#2Calculate the difference between 50 and 23.
#print("Difference between 50 and 23 is: ", 50-23)

#3Multiply 5 by 9 and print the result.
#res = 5*9
#print(res)

#4Divide 100 by 10 and print the result.
#res = 100/10
#print(res)

#5Calculate 17 divided by 3 using integer division (//).
#res_qoldiq = 17 // 3
#print(res_qoldiq)

#6Find the remainder when 25 is divided by 7 using the modulo operator (%).
#a=19
#b=12
#rem=17%12
#print(rem)

#7Calculate the result of (10 + 5) * 2
#print((10+5)*2)

#8Ask the user for two numbers, and then print their sum, difference, product, and quotient.
#a = int(input('1st value '))
#b = int(input("2nd value "))
#print(f"sum: {a+b}, diff: {a-b}, product: {a*b}, quotient: {a/b}")

#9Ask the user for a number, then calculate and print the result of that number to the power of 2.
#num = int(input("Enter the number that you want: "))
#print(f"power of {num} is {num**2}")

#10A user buys a T-shirt for $25 and a hat for $15. Calculate and print the total cost.

#t_shirt=int(input("t-shirt: "))
#hat = int(input("hat: "))
#print("Total cost:", t_shirt*25+hat*15,'$')


