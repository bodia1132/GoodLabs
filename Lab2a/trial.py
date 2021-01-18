print("First constant", False)
print("Second constant", True)
print("Third constant", None)

print("1", f"in bool function is {bool(1)}")
print("0", f"in bool function is {bool(0)}")
print("Number 21", f"in binary is {bin(21)}")

Flip_flop = True
    for counter in range(4):
        if(Flip_flop):
            print("Hello")
            Flip_flop = False
        else:
            print("there")
            Flip_flop = True

x = 1
try:
    num = input("Please enter a number: ")
    x = int(num)
except ValueError as e:
    print("Oops!", num,"was no valid number.Try again...")
finally:
    print("Problem finally found!")

with open("text.txt", "r") as text:
    for line in text:
        print(line)

test_lambda = lambda item: item+2
var_number = 8
print(test_lambda(var_number))