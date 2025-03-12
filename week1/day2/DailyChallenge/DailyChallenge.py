task = input("Enter a 10 character-long string: ")
firstchar = task[0]
lastchar = task[-1]


if len(task) < 10:
    print("string not long enough")

elif len(task) > 10:
    print("string is too long")

elif len(task) == 10:
    print("perfect")


print(firstchar)
print(lastchar)

for char in task:
    print(char)


import random

task_list = list(task)
random.shuffle(task_list)
combined_list = ''.join(task_list)
print(combined_list)

