print("......")
print(".1.2.3.")
print("......")
print(".4.5.6.")
print("......")
print(".7.8.9.")
print("......")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = int(input("Please enter number you want change: "))
y= y-1
num = int(input("Please new number: "))

x[y] = num
print("......")
print(x[0:3])
print("......")
print(x[3:6])
print("......")
print(x[6:10])
print("......")