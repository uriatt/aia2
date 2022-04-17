number = input("Write your number here:  ")
input("Press <enter> to check if the number is a palindrome.")
if str(number) == str(number)[::-1]:
    print("True")
else:
    print("False")