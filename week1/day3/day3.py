# ✅1. Sequences Overview :

#List	    ✅ Yes	✅ Yes	✅ Yes	[1, 2, 3]
#Tuple	    ✅ Yes	❌ No	✅ Yes	(1, 2, 3)
#Set        ❌ No	✅ Yes	❌ No	{1, 2, 3}

#  ✅2. List Example :

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[1]) 

# ✅3. Tuple Example :

dimensions = (1920, 1080)
print(dimensions[0])

# ✅4. Set Example :

colors = {"red", "green", "blue", "green"}
print(colors) # Sets automatically remove duplicates

# ✅5. Loops :

# For Loops:
for fruit in fruits:
    print(fruit)

# While Loops:
count = 0
while count < 3:
    print(count)
    count += 1

# For a program that should run only as long as many conditions are True, you can define one variable that determines whether the entire program is active. This variable, called a flag, acts as a signal to the program.
active = True

while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)

print("Goodbye !")

# break exit the while loop immediately without running any remaining code in the loop, regardless of the results of any conditional.
while True: 
    city = input("Please enter the name of a city you have visited (enter 'quit'  when you are finished): ")
    if city == 'quit':
        break
    else:
        print("I'd love to go to", city)

print("Goodbye !")