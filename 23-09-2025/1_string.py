s = input("Enter a String: ")

a = s[0] + s[1:].replace(s[0], "$")

print(a)
