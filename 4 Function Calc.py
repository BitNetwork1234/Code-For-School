print("****** Four Function Calculator *******")

number1 = int(input("Enter Your First Number:"))
number2 = int(input("Enter Your Second Number"))
operator = input(" Do you want to +,-,X or /?")

if operator =="+":
    answer = number1 + number2
elif operator =="-":
    answer = number1 - number2
elif operator =="X":
    answer = number1 * number2
elif operator =="/":
    answer = number1 / number2
else:
    print("Sorry I Dont Know How To Do That!")
print("The Answer =" +str(answer))
