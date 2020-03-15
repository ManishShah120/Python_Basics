#This program is teaching us how to handle error of
#different types
try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(age,income,risk)
except ZeroDivisionError:
    print("Age cannot be Zero")
except ValueError:
    print("Invalid Value")



#use Comments for WHYs? and HOWs? not WHATs










#Exit Code Zero means our program
#compltede sucessfully theere where
#no error

#Exit code 1 means our program crashed