codenumber_as_integer = None
while number_as_integer is None:
    try:
        number_as_integer = int(input("Please enter an integer: "))
    except ValueError:
        print("Invalid integer!")

print(f"The integer you entered was {number_as_integer}")
