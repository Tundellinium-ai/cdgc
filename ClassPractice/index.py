# name = input('What is your name?')
# print(name)

# person = 'Tunde'
# age = 25
# course = 'Python programming'
# state = 'Oyo'
# occupation = 'Data analyst'




# print("Hello World")
# age = 30
# price = 19.95
# first_name = "Babatunde"
# is_online = True 
# print(age)

# first_name = "John"
# last_name = "Smith"
# age = 20
# new_patient = True
# print(first_name, last_name, age, new_patient)

# name = input("What is your name? ")
# print("Hello " + name)

# birth_day = input("Enter your birthday: ")
# age = 2025 - int(birth_day)
# print(age)

# int()
# float()
# str()
# bool()

# first_number = float(input("First: "))
# second_number = float(input("Second: ")) 
# sum = first_number + second_number
# print("Sum: " + str(sum))
 
# course = "Python for beginners"
# print(course.replace('for', 'is'))
# print('for' in course)

# in operator
# addition operator
# subtraction operator
# multiplication operator
# single forward slash operator = float
# double forward slash operator = int
# modulus operator (%) = remainder
# exponent operator (**) = raise to power
# augmented assignment (=) operator 
# equality operator ==
# not equality operator !=
# logical operators (or, and, not)
#append is to add an element to the end of a list
#insert is to add an element to the end or middle of the list

# print(10 ** 3)

# x = 5
# x %= 2
# print(x)

# x = 3
# x = x + 3

# x -= +10
# print(x)

# x = (10 + 3) * 2
# print(x)

# x = 2 != 3
# print(x)

# price = 20
# print(not price > 10)

# temperature = 9
# if temperature > 30:
#     print("Hot Day!")
#     print("Drink plenty water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It is a bit cold")
# else:
#     print("it is cold")
# print("Done")

# weight = float(input("Weight: "))
# type = str(input("(k)g or (L)bs: "))
# if type == "K":
# # if type == "k" or "K" or "kg" or "KG" or "Kg" or "kG":
#     lbs = weight * 0.45
#     print(f"Weight in lbs: {lbs}")
# else:
#     kg = weight / 0.45
#     print(f"Weight in kg: {kg}")


# elif type.upper == "LBS":
#     kg = type / 0.45
#     print(f"Weight in kg: {kg}")

# elif type == "l" or "L" or "lbs" or "LBS" or "Lbs" or "LBs" or "lb" or "LB" or "LbS" or "lBS":
#     kg = type * 2.20462
#     print(f"Weight in Kg: {kg}")
# elif type != "k" "K" "kg" "KG" "Kg" "kG" "l" "L" "lbs" "LBS" "Lbs" "LBs" "lb" "LB" "LbS" "lBS":
#     print("You have inputted a wrong SI unit of your weight")
# else:
#     print("Invalid Inputs")

# i = 1
# while i <= 5_0:
#     print(i * "*")
#     i = i + 1

# names = ["Babatunde", "Ismail", "Bale"]
# # names[0] = "Babs"
# print(names[0:2])
# print(names[-1])

# numbers = [1,2,3,4,5]
# numbers.insert(0, -1)
# print(numbers)

# numbers = [1,2,3,4,5,6]
# numbers.remove(3)
# print(numbers)

# numbers = [1,2,3,4,5]
# numbers.clear()
# print(numbers)

# numbers = [1,2,3,4,5]
# print(4 in numbers)

# numbers = [1,2,3,4,5]
# print(len(numbers))

# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# numbers = range(5, 10)
# for number in numbers:
#     print(number)

# for number in range(1, 20, 4):
#     print(number)

# numbers = (1,2,3,4,5,3)
# print(numbers.index(4))
# print(numbers)









# mapping type
# dictionary dict() e.g.
# person = {
#     "name": "Babatunde",
#     "age": [20, 40, 30],
#     "isMarried": True
# }
# print(type(person))
# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.pop("age"))
# person.update({"class":"beginner"})
# print(person["age"][1])
# person.pop(["age"][0])
# print(person)

#set() - used to create a normal set (changeable)
#set is cahngeable 
#it does not allow duplicate value
#it does not allow duolicate value
#frozenset cannot be used to modify the data but can be used to do calculation
#it is not order
# myset = {"ope", "ali", "sobuur"}
# myset.add("Ole")
# myset.remove("Femi")
# myset.discard("Femi")
# myset.update
# myset.update(["Pelumi", "Tolu"])
# print(myset)
# print("Names Set:", myset)
# freeze = frozenset(myset)
# freeze.remove("ope")
# print(freeze)

#membership operator (in, not in)
# students = ["Dami", "Ola", "Ope", "Babatunde"]
# print("Babatunde" in students)
# print("Dami" not in students)

#identity operator (is, is not)
#x = [1,2,3]
#y = x
#z = [1, 2, 3]
#print(x is y)
#print(x is z)
#print(x ==y)

# fatimah = False
# camera = True

# if fatimah is True and camera is True:
#     print("   Fatimah is Present but Sleeping")
# elif fatimah:
#     print("   Fatimah is Present")
# else:
#     print("   Fatimah is Absent")            

#Condtional statement

#print(_____Simple Calculator_____)
#operator = ["Add", "Substract", "Multiply", "Divide"]
#val1 = float(input("Enter first value: "))
#val2 = float(input("Enter second value: "))

#operation = input(f'choose your operation from {operator}: ')
#if operation in operators:
    #if operation == "Add":
        #print(f'{val} + {val2} = {val1 + val2})
    #elif operation == "Subtract":
        #print(f'{val} - {val2} = {val1 - val2})
    #elif operation == "Multiply":
        #print(f'{val} * {val2} = {val1 * val2})
    #elif operation == "Divide":
        #print(f'{val} / {val2} = {val1 / val2})
    #else:
        #print("Wrong Operation")
#else:
    #print("Wrong Output")


#print(_____Simple Calculator_____)
#operator = ["Add", "Substract", "Multiply", "Divide"]
#val1 = float(input("Enter first value: "))
#val2 = float(input("Enter second value: "))

#operation = input(f'choose your operation from {operator}: ')
    #if operation in operator and operation == "Add":
        #print(f'{val} + {val2} = {val1 + val2})
    #elif operation in operators and operation == "Subtract":
        #print(f'{val} - {val2} = {val1 - val2})
    #elif operation in operators and operation == "Multiply":
        #print(f'{val} * {val2} = {val1 * val2})
    #elif operation in operators and operation == "Divide":
        #print(f'{val} / {val2} = {val1 / val2})
    #else:
        #print("Wrong Input")

#Youth = int(input("Enter Age: "))
#Vote = True
#if Youth > 17:
    #if vote == True:
        #print("You are eligible")
    #elif vote == False:
        #print("Why dont you vote, you are not qualified")
    #else:
        #print("Wait till you are 18")
#else:
    #print("Wrong input")


#Assignment: Build a simple USSD menu using conditional statements
#1. create a list of different ussd codes you use max of 3
#2. use conditional statements to build a dashboard for ussd menu for each code using membership operator to confirm the ussd
#3. each ussd code should have at least 3 options
#4. each option should have at least 3 inner navigations and a message when selected
#5. use nested conditional statements to achieve this
#6. be mindful of exceptions like when you enter the wrong ussd code or worng option and create code to handle this using "esle"

# print("    _____You are Wecome to Element Network USSD Application_____")

# codes = ["*310#", "*312#", "*321#"]

# print('''
#       *310# - Aritime balance check 
#       *312# - Buy data 
#       *321# - Share data
# ''')

# ussd = input(f"    Enter USSD: ")
# if ussd in codes and ussd ==  "*310#":
#     print('''    
#       SmartTALK Main Bal:N2941.3 .Dial *310*1# for bonus balance
#       Select
#       1) 6GB @ N2500 (7days)
#       2) 100mins @ N1000 (14days)
#       3) Cancel
# ''')
#     choice1 = int(input("    Enter your choice (1-3): "))
#     if choice1 == 1:
#         print("    You have successfully subscribed for 6GB")
#     elif choice1 == 2:
#         print("    You have successfully subscribed for 100mins")
#     elif choice1 == 3:
#         print("    Request cancelled")
#     else:
#         print("    Wrong input, try again")
# elif ussd in codes and ussd == "*312#":
#     print('''
#       1 My Area
#       2 Data Plans
#       3 10GB @N3000
#       4 5GB @N1500
#       5 3GB @N750
#       6 1.5GB @N500
#       7 2GB @N600
#       8 6GB @N2500
#       9 Voice Plans
#       * Next
# ''')
#     choice2 = input("   ")
#     if choice2 == "1":
#         print("    You have successfully migrated to My Area")
#     elif choice2 == "2":
#         print("    You will see data plans shortly...")
#     elif choice2 == "3":
#         print("    You have successfully subscribed for 10GB")
#     elif choice2 == "4":
#         print("    You have successfully subscribed for 5GB")
#     elif choice2 == "5":
#         print("    You have successfully subscribed for 3GB")
#     elif choice2 == "6":
#         print("    You have successfully subscribed for 1.5GB")
#     elif choice2 == "7":
#         print("    You have successfully subscribed for 2GB")
#     elif choice2 == "8":
#         print("    You have successfully subscribed for 6GB")
#     elif choice2 == "9":
#         print("    You will see voice plans shortly...")
#     elif choice2 == "*":
#         print("    You will be shown the next options soon...")
#     else:
#       print("    Wrong input, try again")
# else:
#   print("    Wrong USSD, try again")


#
#




# print("_____Grading App_____")
# score = int(input("Enter Your Exam Score: "))
#if score >= 70 and score <= 100:
    #print(f'your grade is {score} which is A')
#elif score >= 60 and score <= 69:
    #print(f'your grade is {score} which is B')
#elif score >= 50 and score <= 59:
    #print(f'your grade is {score} which is C')
#elif score >= 45 and score <= 49:
    #print(f'your grade is {score} which is D')
#elif score >= 40 and score <= 44:
    #print(f'your grade is {score} which is E')
#elif score >= 0 and score <=39:
    #print(f'your grade is {score} which is F')
#else:
    #print("Invalid score")

#read on: match and case





# student_name = "Daniel"
# print(len(student_name))
# print(student_name[-6])
# print(student_name.strip())

# print("1. What is the capital of Nigeria \n a). Lagos b). Abuja")
# ans = input("Your answer: ")
# if ans.upper().strip() == "B":
#     print("Correct")
# else:
#     print("Wrong")

#Python collections/array
# students = ["mercy", "ope", "daniel", "aliya", "mercy"]
# print(students[::-3])
#Adding Eleemnts
#students.append("Ayomide")
#students.extend({"Aishat", "Pelumi"})
#students.insert(0, "Doc")
#students.insert(1, "Dara")

#arr = [
#   ["Banana", "Apple", "Orange"],
#   ["Rice", "Benas"]
#   ["Yam", "Plantain"]
#  ]
#print(arr)
#print(arr[0])

#Remove Element
#students.remove("ope")
#students.pop(2)
#students.clear()
#print(students)

#For Loop
#student = []
#student_name = input("Enter student name: ")
#reg_st int(input("Number of students: ")
#for student in range(reg_st):
#   print(student_name)

#student = input("Enter student name: ")
#for i in rnage(10)
#print(student)

#name = "Fatimah"
#print("This are the letter that makes up Fatimah: ")
#for letter in name:
#print(letter)

#li_operator = ["*"]
#operator = input("Enter your operator: ")
#if operator in li_operator and operator == "*":
#   for x in range(1, 13)
#       print(f"Multiplication Table of {x}")
#       for y in range(1, 13)
#           print(f"{x} x {y} = {x*y})
#else:
#   print("Invalid operator")
#num_student = int(input("Enter the number of student: "))
#students = str(input("student name: "))
#Question = ["How many color are there in the flag of Nigeria, \n (a) Green and white (b) Green white green",
#       "How many state are there in Nigeria, \n (a) 36 states (b) 12 states"
#           ]
#Answer = 

# fruits = ("Banana", "Grapes", "Apple", "Orange")
# new = list(fruits)
# new[0] = "watermelon"
# print(new)
# fruits = tuple(new)
# print(fruits)

#unpacking
# first_fruit, second_fruit, *remaining, last_fruit = fruits
# print(last_fruit)

# bio_data = ("Adewunmi/15/Nigeria")
# var = bio_data.split("/")
# print(var)
# name, age, country = var
# print(f"{name}, {age}, {country}")

#set operation
# setA = {1,3,4,5,6,7,8,9,10}
# setB = {11,1,13,14,15}
# setC = {3,4}

# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setA - setB)
# print(setA .difference(setB))
# print(setA.symmetric_difference(setB))
# print(setA.issuperset(setC))
# print(setB.issubset(setA))
# print(setB.isdisjoint(setC))






# Assignment
# 1. Build a simple quiz application using the zip class approach
# 2. Ask the user to input their name and take the text
# 3. Display the result of the test for each student
# 4. Find the student with the min score
# 5. Find the student with the max score
# 6. Calculate the average score
# Add grading system to show student that pass and the one that failed






#Dictionary: ordered, changeable, it doesn't allow duplicate
#dict(key=value) or {key:value}

#phone = {
    # "model": "iPhone6",
    # "color": "Black",
    # "rom": "128gb",
    # "version": "ios 18",
    # "owner": {
#         "name": "john doe",
#         "address": "Lagos"
# }
#}
# phone["model"] = "Iphone18"
# phone["sold"] = True
# print(phone["owner"]["name"])
# print(phone)
#
# print(type(phone.keys()))
# print(list(phone.key()))

# for k, v in phone.items():
#     print(k, v)




# students = {}
# students_score = {}
# ques_ans = {
#     "    What is your name \n    a) Babatunde b) Ismail c) Bale": "a",
#     "    What is your surname \n    a) Babatunde b) Ismail c) Bale": "b"
# }
# student_num = int(input("Enter the number of students that will take this quiz: "))
# for num in range(student_num):
#     student_data = {
#         "name": input("Enter your name: "),
#         "Age": input("Enter your age: ")
#     }
#     students.update(student_data)
#     score = 0
#     for ques, ans in ques_ans.items():
#         print(ques)
#         student_answer = str(input("Enter your answer: "))
#         if student_answer == ans.lower():
#             print("Correct!!!")
#             score += 1
#         else: 
#             print("Wrong!!!")

# pass_mark = 50
# percent = (score/len(ques_ans)) * 100
# passed = percent >= pass_mark

# print("    ==Your Results==")
# for s in students:
#     print(f"    Thank you for taking this simple quiz {s['name']}-{s['age']}. You scored: {s['score']} out of {len(ques_ans)} ({s['percent']}%). This means that you {'Passed the quiz' if s['passed'] else 'You failed the quiz'}")



# total_card = 10
# age = 18
# while True:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         print('''
#         1. Register
#         2. Check available card
#         3. Replace
#         4. Check if card is available
#         5. Exit
#      ''')
#         choice = input("Enter choice: ")
#         if choice == "1":
#             print(f"{name} successfully registered")
#             total_card -= 1
#         elif choice == "2":
#             print(f"{total_card} available, hurry before it finishes")
#         else:
#             print("Wrong input")
#     else:
#         print("wait till you are 18.")


#To do List

# tasks = []
# while True:
#         def home():
#             print('''
#             1. Create task
#             2. View 
#             3. Delete task
#             4. Edit task
#             5. Exit
#             ''')
#             choice = int(input("Input your choice: "))
#             if choice == 1:
#                  create_task()
#             elif choice == 2:
#                  view_task()
#             elif choice == 3:
#                  delete_task()
#         def create_task():
#                 task = {
#                     "Activity": input("Enter Activity: "),
#                     "Time": input("Time of Activity: ")
#                 }
#                 tasks.append(task)
#                 print(f"You have successfully created {task}")
#         def view_task():
#                 print("These are your activities")
#                 for x, y in enumerate(tasks, start=1):
#                             print(f"{x}. {y["Activity"]} by {y["Time"]}")
#         def delete_task():
#             print("Which of the activities do you want to remove?")
#             for x, y in enumerate(tasks, start=1):
#                     print(f"{x}. {y["Activity"]} by {y["Time"]}")
#             delete = int(input("Enter the number of the activity you want to remove: "))
#             delete_task = tasks.pop(delete -1)
#             print({tasks})

#             print(f"Your task has been deleted, these are your remianing task:\n {tasks}")
#         home()







# for x in [2,4,5,6,7,8]:
#     if x == 9:
#         print("Found!")
#         break
#     print("Checking", x)
# else:
#     print("Loop Done")

# for x in [2,4,5,6,7,8]:
#     if x == 7:
#         print("Found: ", x)
#         found = True
#     if found:
#         pass

# if not found:
#     print("Did not find")

# items = [5,3,8,1,7]
# target = 1
# i = 6
# n = len(items)
# while i < n and items[i] != target:
#     i += 1
# if i < n:
#     print("Found it: ", items[i])
# else:
#     print("Did not find it")
# fruits = ["apple", "banana", "cherry"]
# for idx, e, a in enumerate(fruits, start=1):
#     print(idx, e)
    






# operators = ["*", "+", "-", "/"]
# operator = input("Enter your operator: ")
# ran = range(1,13)
# if operator in operators and operator == "*":
#     for times in ran:
#         print(f"Multiplication Table of {times}")
#         for num in ran:
#             print(f"{times} x {num} = {times*num}")
# elif operator in operators and operator == "+":
#     for times in ran:
#         print(f"Addition Table of {times}")
#         for num in ran:
#             print(f"{times} plus {num} = {times+num}")
# elif operator in operators and operator == "-":
#     for times in ran:
#         print(f"Subtraction Table of {times}")
#         for num in ran:
#             print(f"{times} - {num} = {times-num}")
# elif operator in operators and operator == "/":
#     for times in ran:
#         print(f"Division Table of {times}")
#         for num in ran:
#             print(f"{times} / {num} = {times/num}")
# else:
#    print("Invalid operator")














# student_scores = {
#     "Alice": 80,
#     "Bob": 75,
#     "Emma": 45
# }
# for name in student_scores:
#     print(name, student_scores[name])
# for score in student_scores.values():
#     print(score)
# for name, score in student_scores.items():
#     print(f"{name} scored {score}")


# First_Number = float(input("What is your first number: "))
# Second_Number = float(input("what is your second number: "))
# Multiply = First_Number * Second_Number
# print("Product: " + str(Multiply))

# python variables
# variables are symbolic names that acts as containers for storing values
# i. variable name 
# ii. assignment operation (funnel)
# iii. value
# box = "clothes"
# box = "Water"
# print(box)

# Rules guiding python variable declarations
# 1. You don't start a variable name with any symbols aside _ or alphabet
# 2. You don't include spaces during variable declaration. You use either camel casing, pascal casing or snake casing
# 3. You don't use python's special keywords
# 4. Your varaible name should be descriptive enough

# User = input("What is your name? ")
# Age = int(input("What is your age: "))
# # print('Welcome to class ' + User + ' you are ' + str(Age) + ' and we are happy to see you!')
# print(f'Welcome to class {User} you are {Age} and we are happy to see you!')


# print("Hello, welcome to Uniosun Teaching Hospital. I'll like to collect your bio-data so that I can be care for you.")
# name = input("What is your name?: ")
# DOB = int(input("What year were you born?: "))
# Age = 2025 - DOB
# gender = input("Are you a male or female?; ")
# blood_group = input("What is your blood group?: ")
# occupation = input("What is your occupation?: ")
# marital_status = input("Are you single or married?: ")
# phone_number = int(input("Phone number: "))
# next_of_kin = input("Who is your next kin?: ")
# print(f"Thank you {name} for providng us with your bio-data details. We understand that you are {Age} and you are a {gender} with {blood_group}, {marital_status} and {occupation}.")


# name = "Babatunde"
# print(name[-3])

# number = 5
# number_1 = 3.3
# print(number + number_1)

# print("Register above 18 years")
# age = int(input("Enter age: "))
# condition = age >= 18
# if condition == True:
#     print("You are eligible to register")
# elif condition == False:
#     print("Wait till you are 18 years")
# else:
#     print("wrong input")

# list_type = ["hello", "world"]
# list_type[0] = "Never"
# print(list_type[0:1])
# first = ["boy", "girl", "man", "woman"]
# first[-1] = 'lesbian'
# print(first)


# car = {
#     "brand": "Benz",
#     "model": "GCL330",
#     "color": "white",
#     "year": "owner",
#     "owner": {
#         "fullname": "Babatude",
#         "age": 12,
#         "addresss": {
#             "city": "Osogbo",
#             "state": "Osun",
#             "country": "Nigeria"
#         }
#     }

# }
# print(car["owner"]["fullname"])
# car.update({"color": "Not valid", "sold": True})
# car.update({'brand': (car["brand"], "Toyota")})
# car.pop()
# car.popitem()
# print(car)


# for i in range(1,6):
#     print(f"{i} Multiplication Table")
#     for x in range(1,6):
#         print(f"{i} X {x} = {i * x}")




# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome onboard!")


# greet("Babatunde", "Bale")
# greet("Zainab", "Bale")

# def greet(name):
    # print(f"Hello {name}")
    # return "..."

# mess = greet("Babatunde")
# print(mess)

#perform a task
#calculate and return a value

# def get_greeting(name):
#     return f"Hi {name}"

# message = get_greeting("Babatunde")


# def increment(number, by=1):
#     return number + by



# print(increment(2,5))


# def multiply(*numbers):
#     for number in numbers:
#         print(number)


# multiply(2,3,4,5)

# function definition
# function declaration
# function invocation

# def greet(name):
#     print(f'welcome {name}')
# greet('bola')

# def home():
        
#     val1 = float(input('Enter val1: '))
#     val2 = float(input('Enter val2: '))
#     while True:
#         print('''
#             1. Addition
#             2. subtract
#             3. divide
#             4. multiply
#             5. exit
                
#             ''')
#         def add():
#             print(val1 + val2)
#         def sub():
#             print(f'{val1 - val2}')
#         def div():
#             print(f'{val1 / val2}')
#         def mul():
#             print(f'{val1 * val2}')
                
#         choice = input('Enter choice: ')
#         if choice == '1':
#             add()
#         elif choice == '2':
#             sub()
#         elif choice == '3':
#             div()
#         elif choice == '4':
#             mul()
#         elif choice == '5':
#                 exit()
# home()

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(1,2,3,4,5))

# def save_user(**user):
#     print(user["course"])

# save_user(id=1, name="Babatunde", course="Optometry")

# message = "a"
# def greet(name):
#     message = "b"

# greet("Mosh")
# print(message)

#Encapsulation and Inheritance in OOP





# x = 0
# while x < 10:
#     print(x)
#     if x == 4:
#         break
#     x += 1

# ticket = 10
# while ticket > 0:
#     age = int(input("What is your age: "))
#     if age <=17:
#         print("You are too young to watch this movie")
#         continue
#     ticket -= 1
#     print(f"You have purchased your ticket and there {ticket} tickets left.")

# true statement: True, 1, "hello", ["Hello"]
# false statement: False, 0, ""

# password = ""
# while password != "open123":
#     password = input("Enter your password: ")
#     if password != "open123":
#         print("Wrong Password!")
#     continue
# print("Access granted!")

# OOP -> object oreinted programming

# class
# properties
# methods
# objects
# instantation
# constructor
# inheritance
# encapsulation

# class car:
# brand = "Toyota"
# model = "Camry"
# color = "Black"
# year = 2020
# def drive(self):
# print(f"The {self.color} {self.brand} {self.model} is driving")
# mycar = car()
# mycar.brand = "Benz"
# mycar.color = "White"
# mycar.drive()
# print(mycar.brand)

# class calculator:
# def __init__(self, brand, color):
# self.brand = brand
# self.color = color
# def on(self):
# print(f'''
# calculator brand {self.brand} with {self.color} color is now on

# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit
# ''')
# choice = input("Enter choice: ")
# if choice == "1":
# self.addition()
# elif choice == "2":
# self.subtraction()
# elif choice == "3":
# self.multiplication()
# elif choice == "4":
# self.division()
# elif choice == "5":
# exit()
# else:
# print("Invalid input")
# self.on()
# def addition(self):
# val1 = int("Enter value 1: ")
# val2 = int("Enter value 2: ")
# return val1 + val2
# def subtraction(self):
# val1 = int("Enter value 1: ")
# val2 = int("Enter value 2: ")
# return val1 - val2
# def multiplication(self):
# val1 = int("Enter value 1: ")
# val2 = int("Enter value 2: ")
# return val1 * val2
# def division(self):
# val1 = int("Enter value 1: ")
# val2 = int("Enter value 2: ")
# return val1 / val2
# mycalc = calculator("Casio", "Black")
# mycalc2 = calculator ("porpo", "white")
# mycalc2.on()
# tasks = []
# class Todo:
#     def __init__(self, tasks):
#         self.tasks = tasks
#     def menu(self):
#         print('''
#         1. Create Task
#         2. View Task
#         3. Delete Task
#         4. Edit Task
#         5. Exit
#         ''')
#         choice = int(input("Input your choice: "))
#         if choice == 1:
#             self.create_task()
#         elif choice == 2:
#             self.view_task()
#         elif choice == 3:
#             self.delete_task()
#         elif choice == 4:
#             self.edit_task()
#         else:
#             print("Invalid input")
#             self.menu()
#     def create_task(self):
#         task = input("Enter task: ")
#         self.tasks.append(task)
#         print(f"Task {task } succesfully added.")
#         self.menu()
#     def view_task(self):
#         for each_task in enumerate(self.tasks, 1):
#             print(f" {each_task}")
#             self.menu()
#     def delete_task(self):
#         self.view_task()
#         act_remove = int(input("Enter activity to remove: "))
#         delete_task = tasks.pop(act_remove -1)
#         print(f"This is the remaining task {tasks}")
#         self.menu()
#     def edit_task(self):
#         self.view_task()
#         act_edit = int(input("Enter activity to edit: "))
#         new_task = input("Enter new task: ")
#         self.task[act_edit - 1] = new_task
#         print(f"Task has been successfully updated to {new_task}")
#         self.menu()

# mytodo = Todo(tasks)
# mytodo.menu()

# 

# class car:
#     def __init__(self, brand, model, YOP, color):
#         self.brand = brand
#         self.model = model
#         self.YOP = YOP
#         self.color = color

#     def drive(self):
#         print(f"This car {self.brand}, {self.model}, build in {self.YOP} with {self.color} color.")
# mycare = car("Toyota", "camry", "2025", "black")
# mycare.drive()

# class father:
#         def __init__(self, Sname, Lname, age, phone):
#             self.surname = Sname
#             self.lastname = Lname
#             self.age = age
#             self.phone_num = phone
#         def details(self):
#             print(f"The father name is {self.surname} {self.lastname} and he is {self.age} years old with the {self.phone_num} phone number")
# myfath = father("Babatunde", "Bale", 50, "08090622572")
# myfath.details()

# class wife(father):
#         def __init__(self):
#             super().__init__("Zainab", "Lukman", "23", "08132338145")
#             self.sur = "Zainab"
#             self.last = "Lukman"
#             self.ag = 23
#             self.phone_nu = "08132338145"
#         def detail(self):
#             print(f"The wife name is {self.sur} {self.last} and she is {self.ag} years old with the {self.phone_nu} phone number")

# mywife = wife()
# mywife.detail()

# class dog:
#     def speak(self):
#         print("Some generic animal sound")
# class animal(dog):
#     pass

# canine = dog()
# canine.speak()


# __PRIVATE ENCAPSULATION__
# class father:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#     def details(self):
#         print(f"{self.__name} and {self.age} years old")
#     def change(self, new):
#         self.__name = new
#         print(f"{self.__name} is {self.age} years old")
        
# my = father("Babatunde", "30")
# # new = "Bale"
# my.change("Bale")
# # my.change(new)
# # my.details()

# __PROTECTED ENCAPSULATION__
# class father:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     def details(self):
#         print(f"{self._name} and {self._age}")

# my = father("Babatunde", "30")
# my._name = "Bale"
# my.details()

from Calculator.calc import sleep

sleep()
print("Hello")