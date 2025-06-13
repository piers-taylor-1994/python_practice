def tip_converter(a):
    if 1:
        return round((bill * (1 + (tip / 100)) / people), 2)
    else:
        return round((bill / people * (1 + (tip / 100))), 2)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
print(f"Each person should play: ${tip_converter(1)}")

bill / people * (1 + (tip / 100))

#124.56 * (1 + (12 / 100)) / 7 = 19.93