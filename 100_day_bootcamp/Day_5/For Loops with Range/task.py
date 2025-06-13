total = 0
for number in range(1, 101):
    total += number
print(total)


for number in range(1, 101):
    #if number % 3 == 0 and number % 5 == 0:
        #print("FizzBuzz")
    output = ""
    if number % 3 == 0:
        output = output + "Fizz"
    elif number % 5 == 0:
        output = output + "Buzz"
    else:
        output = str(number)
    print(output)