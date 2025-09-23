file = input("Enter a file name: ")

a = file[::-1]
b = a.index(".")
c = a[:b]

print(c[::-1])
