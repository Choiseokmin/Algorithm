x = int(input())
n = int(input())
y = int()

for i in range(n): 
    a,b = map(int, input().split())
    y += a*b
    
if y == x:
    print("Yes")
else:
    print("No")
