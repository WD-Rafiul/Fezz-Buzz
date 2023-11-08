# number / 3 = feez
# number / 5 = buzz
# number / 3,5 = feezbuzz
number = int(input("Enter a number:"))
if number % 3 == 0 and number % 5 == 0:
    print("FezzBuzz")

elif number % 3 == 0:
    print("Feez")

elif number % 5 == 0:
    print("Buzz");

