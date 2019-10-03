a = int(input())
b = int(input())

c = a*b

with open("hello.txt", "w") as f:
    f.write(str(c))