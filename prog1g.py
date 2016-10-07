print("This program illustrates a chaotic function")
x = input("Enter a number between 0 and 1:")
for i in range (5):
    x=3.9 * x * (1-x)
    print(x)

print("\n")

print("This program illustrates the chaotic math function")
x = input("Enter the value for x : ")
for i in range(5):
    x = 2.0 * x *(1-x)
    print (x)

print("\n")

print ("This pgm will display the chaos behaviour with the user defined iteration")
n = input("Enter the range of iterations : ")
x = input ("Enter the value to calculate Formula: ")
for f in range(n):
    x = 3.9 * x * (1-x)
    print (x)
          
          
print ("This pgm will display the chaos behaviour with the user defined iteration")
n = input("Enter the range of iterations : ")
x = input("Enter the value to calculate Formula: ")
z = input("Enter the value to calculate Formula: ")
for f in range(n):
    x = 3.9 * x * (1-x)
    z = 3.9 * z * (1-z)
    print (x,z)
