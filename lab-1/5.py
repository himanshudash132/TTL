number = int(input("Enter a number: "))
if abs(number - 1000) <= 100 or abs(number - 2000) <= 100:
    print("The number is within 100 of 1000 or 2000.")
else:
    print("The number is not within 100 of 1000 or 2000.")

