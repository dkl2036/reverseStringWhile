message = input("Enter message to reverse: ")

translated = ''

i = len(message) - 1

while 1 >= 0:
    translated += message[i]
    i -= 1
print(translated)
