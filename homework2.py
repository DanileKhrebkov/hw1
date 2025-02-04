

def analyze_grades(students_grades):
   
    average_grade = sum(students_grades.values()) / len(students_grades)
    print(f" Среднее значение оценок: {average_grade:.2f}")

    
    above_average = [name for name, grade in students_grades.items() if grade > average_grade]
    below_average = [name for name, grade in students_grades.items() if grade < average_grade]

    
    highest_student = max(students_grades, key=students_grades.get)
    lowest_student = min(students_grades, key=students_grades.get)

   
    print("Студенты с оценкой выше среднего:", above_average)
    print("Студенты с оценкой ниже среднего:", below_average)
    print(f"Наивысшая оценка: {highest_student} С баллом {students_grades[highest_student]}")
    print(f"Низшая оценка: {lowest_student} С баллом {students_grades[lowest_student]}")


students_grades = {
    'Alice': 7,
    'Billy': 12,
    'Daniel': 10,
    'Oleg': 11,
}


analyze_grades(students_grades)