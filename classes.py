class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = 0.0

    def rate_lecturer(self, lecturer, course, grade):
        """Функция дает возможность студентам выставить лекторам оценки за лекции.
        Лектор при этом должен быть закреплен за тем курсом, на который записан студент"""

        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        """Поиск среднего балла по лекции для студентов
        count_grade - общее количество оценок у студента
        total_sum_grade - сумма оценок студента
        avg_grade - средний балл студента
        """

        count_grade = 0
        total_sum_grade = 0
        for item in self.grades:
            count_grade += len(self.grades[item])

        for item in self.grades.values():
            for grade in item:
                total_sum_grade += grade

        self.avg_grade = round((total_sum_grade / count_grade), 2)

        return self.avg_grade

    def __str__(self):
        """Перегрузите магический метод __str__ у всех классов.
         У студентов он должен выводить информацию в следующем виде:

        print(some_student)
        Имя: Ruoy
        Фамилия: Eman
        Средняя оценка за домашние задания: 9.9
        Курсы в процессе изучения: Python, Git
        Завершенные курсы: Введение в программирование"""

        result = f"Имя: {self.name}\n" \
                 f"Фамилия: {self.surname}\n" \
                 f"Средняя оценка за домашние задания: {self.get_avg_grade()}\n" \
                 f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
                 f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
        return result

    def __lt__(self, other):
        """Реализуйте возможность сравнивать (через операторы сравнения) между собой
        студентов по средней оценке за домашние задания."""

        if not isinstance(other, Student):
            return f"{other.name} {other.surname} не является студентом\n"
        else:
            return self.avg_grade < other.avg_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс Mentor должен стать родительским классом, а от него нужно реализовать наследование
    класса Lecturer (лекторы).
    Имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса

    Лекторы получают оценки за лекции от студентов
    Лектор при этом должен быть закреплен за тем курсом, на который записан студент"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = 0.0

    def get_avg_grade(self):
        """Поиск среднего балла по лекции для лекторов
        count_grade - общее количество оценок у лектора
        total_sum_grade - сумма оценок лектора
        avg_grade - средний балл по лекциям
        """

        count_grade = 0
        total_sum_grade = 0
        for item in self.grades:
            count_grade += len(self.grades[item])

        for item in self.grades.values():
            for grade in item:
                total_sum_grade += grade

        self.avg_grade = round((total_sum_grade / count_grade), 2)

        return self.avg_grade

    def __str__(self):
        """Перегрузите магический метод __str__ у всех классов.
        У лекторов он должен выводить информацию в следующем виде:

        print(some_lecturer)
        Имя: Some
        Фамилия: Buddy
        Средняя оценка за лекции: 9.9
        """
        result = f"Имя: {self.name} \n" \
                 f"Фамилия: {self.surname}\n" \
                 f"Средняя оценка за лекции: {self.get_avg_grade()}\n"
        return result

    def __lt__(self, other):
        """ Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов
        по средней оценке за лекции."""

        if not isinstance(other, Lecturer):
            return f"{other.name} {other.surname} не является лектором\n"
        else:
            return self.avg_grade < other.avg_grade


class Reviewer(Mentor):
    """Класс Mentor должен стать родительским классом, а от него нужно реализовать наследование
    класса Reviewer (эксперты, проверяющие домашние задания).
    Имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса"""

    def rate_hw(self, student, course, grade):
        """Функция дает возможность выставлять студентам оценки за домашние задания"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """
        Перегрузите магический метод __str__ у всех классов.
        У проверяющих он должен выводить информацию в следующем виде:

        print(some_reviewer)
        Имя: Some
        Фамилия: Buddy
        """
        result = f"Имя: {self.name}\n" \
                 f"Фамилия: {self.surname}\n"

        return result
