m = int(input("Please give m (0=<m<=10)\n"))
while m>9 or m<0:
    m = int(input("Please give m (0<=m<=10)\n"))

n = int(input("Please give n (0<=n<=10)\n"))
while n>9 or n<0:
    n = int(input("Please give n (0<=n<=10)\n"))

print(str(m*str(m) + n*str(n)))