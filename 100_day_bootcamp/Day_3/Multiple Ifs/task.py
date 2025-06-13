print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    photo = input("Do you want a photo? Type y for Yes and n for No.")
    if photo == "yes":
        bill += 3
    print(f"Please pay ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
