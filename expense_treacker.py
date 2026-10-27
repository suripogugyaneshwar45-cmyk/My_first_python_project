maths = int(input("Enter the marks in maths"))
physics = int(input("Enter the marks in physics"))
chemistry = int(input("Enter the marks in chemistry"))
aptitude = int(input("Enter the marks in aptitude"))
english = int(input("Enter the marks in english"))
marks = [maths, physics, chemistry, aptitude, english]
total = 0
valid = True
for mark in marks:
     if mark < 0 or mark > 100:
          valid = False
     else:
          total += mark
if not valid:
     print("Invalid marks entered.")
else:
     percentage = total / len(marks)
     if percentage >= 90:
          result = "Grade A"
     elif percentage >= 80:
          result = "Grade B"
     elif percentage >= 70:
          result = "Grade C"
     elif percentage >= 60:
          result = "Grade D"
     elif percentage >= 50:
          result = "Grade E"
     else:
          result = "Grade F"
     passed = True
     for mark in marks:
          if mark < 35:
               passed = False
if passed:
     print("Pass")
else:
     print("Fail")
print(f"Total marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {result}")
