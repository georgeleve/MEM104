# To programma mou kanei 4 sysgkriseis
def findMax(x, y, z):
    if x > y and x > z:
        max = x
    elif y > x and y > z:
        max = y
    else:
        max = z
    return max

# 3 sygkriseis
def findMax2ndWay():
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    return max


print("Please give 3 integer numbers:\n")
x = int(input("Please give x: "))
y = int(input("Please give y: "))
z = int(input("Please give z: "))
print("max =", findMax(x, y, z))