# put your python code here
A = float(input())
B = float(input())
op = input()

if B == 0 and op in ("/", "mod", "div"):
    print("Division by 0!")
    
elif op == "+":
    print(A + B)
    
elif op == "-":
    print(A - B)
    
elif op == "/":
    print(A / B)
    
elif op == "*":
    print(A * B)
    
elif op == "mod":
    print(A % B)
    
elif op == "pow":
    print(A ** B)
    
elif op == "div":
    print(A // B)
