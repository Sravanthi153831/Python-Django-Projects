print("----- Student Project -----")
name = input("Enter student name:   ")
roll = int(input("Enter roll number:  "))
m1 = float(input("Enter Telugu marks:  "))
m2 = float(input("Enter English marks: "))
m3 = float(input("Enter Maths marks:  "))
total = m1 + m2 + m3
average = total / 3
print("\n -----Report Card -----")
print("Name:", name)
print("Roll No:", roll)
print("Total:", total)
print("Average:", average)
if average >= 90:
	print("Grade: A")
elif average  >= 75:
	print("Grade: B")
elif average  >= 50:
	print("Grade: C")
else:
	print("Grade: Fail")
