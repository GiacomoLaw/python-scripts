test1 = []
test2 = []
test3 = []
pupils = 0
# put the number of students below
students = 30

while pupils <= students:
    student_test1 = int(input("\n\nTest 1 result: "))
    test1.append(student_test1)
    student_test2 = int(input("\nTest 2 result: "))
    test2.append(student_test2)
    student_test3 = int(input("\nTest 3 result: "))
    test3.append(student_test3)
    pupils += 1

total_mark = sum(test1) + sum(test2) + sum(test3)
average1 = sum(test1) // students
average2 = sum(test2) // students
average3 = sum(test3) // students
averageYear = total_mark // students


print("Average for test 1 was", average1, "average for test 2 was", average2, "average for test 3 was", average3, "and the total average was", averageYear, ".")
