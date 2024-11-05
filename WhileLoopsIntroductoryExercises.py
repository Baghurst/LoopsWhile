user_number = (input("Enter an integer: "))
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










































