from classes import Student, Mentor, Lecturer, Reviewer
"""Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:

1. для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса 
(в качестве аргументов принимаем список студентов и название курса);
2. для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список 
лекторов и название курса).
"""

def avg_grades_students_by_course(stud_list, course):
    """Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    (в качестве аргументов принимаем список студентов и название курса)
    """
    sum_grades = 0
    count = 0

    for student in stud_list:
        if course in student.grades:
            for grade in student.grades[course]:
                sum_grades += grade
                count += 1

    avg_grades = round(sum_grades / count, 2)

    return f"Средний балл за домашние задания по всем студентам в рамках курса {course} - {avg_grades} балл\n"

def avg_grades_lectors_by_course(lect_list, course):
    """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
    (в качестве аргумента принимаем список лекторов и название курса).
    """

    sum_grades = 0
    count = 0

    for lector in lect_list:
        if course in lector.grades:
            for grade in lector.grades[course]:
                sum_grades += grade
                count += 1

    avg_grades = round(sum_grades / count, 2)

    return f"Средний балл за лекции всех лекторов в рамках курса {course} - {avg_grades} балл\n"


if __name__ == '__main__':

    # Создаем студентов, заполняем данные о завершенных и изучаемых курсах
    student_1 = Student('Лев', 'Соловьев', 'мужчина')
    student_1.courses_in_progress += ['Python', 'Git']
    student_1.finished_courses += ['Введение в программирование']

    student_2 = Student('Маргарита', 'Лазарева', 'женщина')
    student_2.courses_in_progress += ['Git', 'Java']
    student_2.finished_courses += ['Основы SQL']

    stud_list = [student_1, student_2]

    # Создаем лекторов, заполняем данные о курсах, которые они преподают
    lecturer_1 = Lecturer('Нина', 'Филатова')
    lecturer_1.courses_attached += ['Python', 'Git', 'Введение в программирование']

    lecturer_2 = Lecturer('Максим', 'Басов')
    lecturer_2.courses_attached += ['Основы SQL', 'Git', 'Java']

    lect_list = [lecturer_1, lecturer_2]

    # Создаем проверяющих, заполняем данные о курсах, которые они могут проверять
    reviewer_1 = Reviewer('Антон', 'Панов')
    reviewer_1.courses_attached += ['Python', 'Git']

    reviewer_2 = Reviewer('Полина', 'Григорьева')
    reviewer_2.courses_attached += ['Python', 'Git', 'Java']

    # Заполнение оценок для студентов за домашние задания
    reviewer_1.rate_hw(student_1, 'Python', 10)
    reviewer_1.rate_hw(student_1, 'Python', 8)
    reviewer_1.rate_hw(student_1, 'Python', 10)

    reviewer_1.rate_hw(student_1, 'Git', 10)
    reviewer_1.rate_hw(student_1, 'Git', 7)
    reviewer_1.rate_hw(student_1, 'Git', 9)

    reviewer_2.rate_hw(student_1, 'Python', 9)
    reviewer_2.rate_hw(student_1, 'Python', 10)
    reviewer_2.rate_hw(student_1, 'Python', 10)

    reviewer_2.rate_hw(student_2, 'Git', 10)
    reviewer_2.rate_hw(student_2, 'Git', 7)
    reviewer_2.rate_hw(student_2, 'Git', 9)

    reviewer_1.rate_hw(student_2, 'Git', 9)
    reviewer_1.rate_hw(student_2, 'Git', 8)
    reviewer_1.rate_hw(student_2, 'Git', 10)

    reviewer_2.rate_hw(student_2, 'Java', 9)
    reviewer_2.rate_hw(student_2, 'Java', 10)
    reviewer_2.rate_hw(student_2, 'Java', 10)

    # Проставляем оценки лекторам по курсам
    student_1.rate_lecturer(lecturer_1, 'Git', 5)
    student_1.rate_lecturer(lecturer_1, 'Git', 10)
    student_1.rate_lecturer(lecturer_1, 'Git', 5)
    student_1.rate_lecturer(lecturer_1, 'Git', 7)
    student_2.rate_lecturer(lecturer_1, 'Git', 8)
    student_2.rate_lecturer(lecturer_1, 'Git', 7)
    student_1.rate_lecturer(lecturer_1, 'Python', 5)
    student_1.rate_lecturer(lecturer_1, 'Python', 10)
    student_1.rate_lecturer(lecturer_1, 'Python', 4)

    student_2.rate_lecturer(lecturer_2, 'Git', 5)
    student_2.rate_lecturer(lecturer_2, 'Git', 10)
    student_2.rate_lecturer(lecturer_2, 'Git', 5)
    student_2.rate_lecturer(lecturer_2, 'Git', 7)
    student_1.rate_lecturer(lecturer_2, 'Git', 10)
    student_1.rate_lecturer(lecturer_2, 'Git', 8)
    student_1.rate_lecturer(lecturer_2, 'Git', 9)
    student_2.rate_lecturer(lecturer_2, 'Java', 5)
    student_2.rate_lecturer(lecturer_2, 'Java', 10)
    student_2.rate_lecturer(lecturer_2, 'Java', 4)

    print("Информация по студентам\n")
    print(student_1)
    print(student_2)

    print("Информация о лекторах\n")
    print(lecturer_1)
    print(lecturer_2)

    print("Информация о проверяющих\n")
    print(reviewer_1)
    print(reviewer_2)

    print("Сравнение студента с лектором")
    print(student_1 < lecturer_1)

    print("Сравнение лектора со студентом")
    print(lecturer_1 < student_1)

    print("Сравнение студента со студентом")
    print(student_1 > student_2)
    print(student_1 < student_2)
    print()

    print("Сравнение лектора с лектором")
    print(lecturer_1 < lecturer_2)
    print(lecturer_1 > lecturer_2)
    print()

    # Вывод среднего балла за домашние задания по всем студентам в рамках конкретного курса
    print(avg_grades_students_by_course(stud_list, 'Python'))

    # Вывод среднего балла за лекции всех лекторов в рамках конкретного курса
    print(avg_grades_lectors_by_course(lect_list, 'Git'))
