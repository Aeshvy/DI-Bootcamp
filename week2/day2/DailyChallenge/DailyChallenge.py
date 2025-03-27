# Daily challenge: Solve the Matrix

matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

secret_message = ""

rows = len(matrix)
cols = len(matrix[0])

for col in range(cols):
    for row in range(rows):
        char = matrix[row][col]
        if char.isalpha():
            secret_message += char

print(secret_message)
