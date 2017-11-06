students = int(input("Number of students: "))
books = int(input("Number of books: "))

books_per_student = books // students
left_over_books = students % books_per_student

print("The number of books per student are", books_per_student)
print("The left over books are", left_over_books)
