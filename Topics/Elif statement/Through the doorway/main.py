A = int(input())
B = int(input())
C = int(input())
X = int(input())
Y = int(input())

if A * B < X * Y or A * C < X * Y or B * C < X * Y:
    print("The box can be carried")
else:
    print("The box cannot be carried")
