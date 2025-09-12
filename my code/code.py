# activty 1
tree1=98
tree2=94
tree3=41
tree4=96
tree5=11
sum=tree1+tree2+tree3+tree4+tree5
print("SUM :",sum)

average= sum/5
print("AVERAGE :",average)
# Activity 2
amount=int(input("Enter the amount: "))
note_1=amount //100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("100 notes :",note_1)
print("50 notes :",note_2)
print("10 notes :",note_3)
# Activity 3
math=40
science=70
hindi=50
english=60
sum=math+science+hindi+english
print("SUM :",sum)
percentage= sum/400*100
print("PERCENTAGE :",percentage)


# project 1
a=20
square=a**2
print("SQUARE :",square)

# activity 1
math=72
science=68
english=80
computer=90
sum=math+science+english+computer
print("SUM :",sum)
average=sum/4
print("AVERAGE :",average)

#activity 2
principal=5000
rate=5
time=3
si=(principal*rate*time)/100
print("SIMPLE INTEREST :",si)
# activity 3
amount=1200
discount=20
dis_amount=(amount*discount)/100
print("DISCOUNT AMOUNT :",dis_amount)
sneha_haw_to_pay=amount-dis_amount
print("SNEHA HAVE TO PAY :",sneha_haw_to_pay)
# project 2
# Store five different dates in separate variables
date1="12/05/2020"
date2="23/08/2021"
date3="15/11/2019"
date4="01/01/2022"
date5="30/09/2023"

# Print the dates
print("Date 1:", date1)
print("Date 2:", date2)
print("Date 3:", date3)
print("Date 4:", date4)
print("Date 5:", date5)
# project 3

# Take user input
name = input("Enter your name: ")
city = input("Enter your city: ")

# Concatenation
greeting = "Hello " + name + " from " + city + "!"
print("\n" + greeting)

# Length of string
print("Length of your name:", len(name))

# Convert cases
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title case:", name.title())

# Indexing and slicing
print("First letter of your name:", name[0])
print("Last letter of your name:", name[-1])
print("First 3 letters of your name:", name[:3])

# Check if string contains something
if "a" in name.lower():
    print("Your name contains the letter 'a'.")
else:
    print("Your name does not contain the letter 'a'.")

# Replace operation
new_city = city.replace("a", "@")
print("Your city name after replacement:", new_city)

# Activity-1 (IF-ELSE Condition)
num=3
if num>0:
    print("num is positive", num)

num=-3
if num>0:
    print("num is  not positive", num)
    
    
# Activity-2 (IF-ELSE Condition)
actual_amount=100
sales_amount=120
if (sales_amount> actual_amount):
    print("Profit")
else:
    print("Loss")

# Activity-3(IF-ELSE Condition)
i=10
if(i<15):
    print("i is smaller than 15")
else:
    print("i is greater than 15")

# Activity-4(IF-ELSE Condition)

no=4
if (num%2)==0:
    print("num is even")
else:
    print("num is odd")

#  project 1 (summmer time)

if temperature > 30:
    print("It's summertime! Have some cold drinks.")
else:
    print("Not too hot, enjoy your day normally!")
# project 2 (odd even flowchart)
print("Welcome to Python Programming!")

# 2. Variables
name = "tarun"
age = 17
print("My name is", name, "and I am", age, "years old.")

# 3. Simple calculation
a = 10
b = 5
print("Sum of a + b =", a + b)

# 4. Odd-Even Program
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")