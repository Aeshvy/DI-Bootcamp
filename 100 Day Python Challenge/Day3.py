# Ride Height Calculator

height = (int(input("Welcome aboard!\nHow tall are you? ")))
price = 0

if height >= 120:
    age = (int(input("You're tall enough to enter.\nHow old are you? ")))
    if age <= 12:
        price = 5
        print("Child tickets are $5")
    elif 12 <= age <=18:
        price = 10
        print("Youth tickets are $10")
    elif 44 <= age <= 55:
        price = 0
        print("Seens like you're having a midlife crisis. The price is free!")
    else:
        price = 15
        print("Adult tickets are $15")

    photo = input("Would you like a photo? (Type 'y' for Yes or 'n' for No): ")
    if photo.lower() == 'y':
        price += 3
        print(f"Your total price is ${price}.")
    else:
        print(f"Your total price is ${price}.")

else:
    print("You are not tall enough!")


# Pizza Place

print("Welcome to Little Rome Pizza Deliveries!")

size = input("What size pizza would you like? S, M or L: ")
pepperoni = input("Do you want extra pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0

if size.lower() == "s":
    print("Small pizza is $15")
    price += 15
elif size.lower() == 'm':
    print("Medium pizza is $20")
    price += 20
elif size.lower() == 'l':
    print("Large pizza is $25")
    price += 25
else:
    print("Input error!")

if pepperoni.lower() == 'y':
    if size == 's':
        price += 2
    else:
        price += 3

if extra_cheese.lower() == 'y':
    price += 1

    
print(f'your total is ${price}. Enjoy your meal!')
