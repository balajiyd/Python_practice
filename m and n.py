z = int(input("Enter the no.of elements: "))
a = []

for i in range (0,z):
    e = int(input(f"ENter the {i} element: "))
    a.append(e)

a.sort()
print(a)

n = int(input("Enter the nth maximum number: "))
m = int(input("Enter the mth minimum number: "))

print("Nth maximum is: ", a[z-n])
print("Mth minimum is: ", a[m-1])
