

fy = int(input("Enter a Future Year: "))
count = 0

for i in range(2025, fy + 1):

    if i % 400 == 0:
        print(f"{i} is a leap year")
        count += 1
    elif (i % 4 == 0) and (i % 100 != 0):
         print(f"{i} is a leap year")
         count += 1

if count == 0:
    print(f"There is no leap year between 2025 and {fy}")
else:
    print("Total number of leap year is: ", count);
