#1

user_number = (input("Enter an integer (empty string will stop the loop): "))
running_total = 0
count = 0
if user_number != "":
    while user_number != "":
        count = count + 1
        user_number = int(user_number)
        running_total = running_total + user_number    
        user_number = input("Enter an integer number: ")
    else:
        print("The total of the positive numbers entered was: ",running_total)
else:
    print("The total of the positive numbers entered was: ",running_total)
average = running_total / count
print(f"The average is {average}")

#2

user_number = int(input("Enter another integer ( negative numbers will stop the loop): "))
running_total = 0
count = 0
if user_number >= 0:
    while user_number >= 0:
        count = count + 1
        user_number = int(user_number)
        running_total = running_total + user_number    
        user_number = int(input("Enter an integer number: "))
    else:
        print("The total of the positive numbers entered was: ",running_total)
else:
    print("The total of the positive numbers entered was: ",running_total)
average = running_total / count
print(f"The average is {average}")

#3

user_number = int(input("Enter your test grades: "))
running_total = 0
count = 0
if user_number >= 0:
    while user_number >= 0:
        count = count + 1
        user_number = int(user_number)
        running_total = running_total + user_number    
        user_number = int(input("Enter your test grades: "))
    else:
        print("The total of the positive numbers entered was: ",running_total)
else:
    print("The total of the positive numbers entered was: ",running_total)
average = running_total / count
print(f"The average is {average}")

if average >= 90:
    print ("A")
elif  average >= 80 and average <= 89:
    print("B")
elif  average >= 70 and average <= 79:
    print("C")
elif  average >= 60 and average <= 69:
    print("D")
elif  average <= 59:
    print("F")

#4

user_number = int(input("Enter an integer: "))
print 













































