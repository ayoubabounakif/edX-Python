my_course = [["Bunny", 90, 87, 95], ["Duck", 78, 96, 89], ["Rubb", 83, 95, 92]]
for student_data in my_course:
    total_grades = 0
    print(student_data)
    for index in range(1, len(student_data)):
        total_grades = total_grades + student_data[index]
        total_grades = total_grades
    print ("Average grade of", student_data[0],"is:", total_grades / 3)
