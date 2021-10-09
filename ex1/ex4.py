def translateGrade(grade):
    if grade>=90:
        return "A"
    elif grade>=80:
        return "B"
    elif grade>=70:
        return "C"
    elif grade>=60:
        return "D"
    else:
        return "F"

grade = int(input("Please give grade between 0 and 100\n"))
while grade>100 or grade<0:
    grade = int(input("Please give grade between 0 and 100\n"))

print("Your grade is", translateGrade(grade))