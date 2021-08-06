""">>>
This is mainly pertaining context. We'll test out copilot's ability to both develop classes and see if it can figure which relationships to use in classes. This is considered simple because no actual behavior is implemented. This is essentially a data structure.

Remarks: 
    -copilot figured the inheritance relationship between the classes, I never specified any super class relationship.
    -same goes for lists of objects
    -methods without any description were generated automatically by copilot (in this script only, this is not a genereal case)
"""

from __future__ import annotations

class Subject:
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self) -> str:
        return f"{self.name} is {self.age} years old."
        

class Teacher(Person):
    """>>>
    A teacher is specialized on a single or multiple subjects. Subjects parameter can be any iterable and will be stored as a set
    """
    def __init__(self, name, age, subjects):
        super().__init__(name, age)
        self.subjects = set(subjects)

    def is_qualified(self, course : Course) -> bool:
        return course.subject in self.subjects

    def __str__(self):
        return f"{super().__str__()} and is qualified on {self.subjects}"

    def __repr__(self) -> str:
        return f"{super().__repr__()} and is qualified on {self.subjects}"
        






class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()

class Course:
    """
    Courses have a list of students and a list of teachers assigned to it. Each course belongs to a broader Subject.
    It has a method to add students and teachers to it.
    """
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def __str__(self) -> str:
        return f"{self.name} is a course in {self.subject}"

class School:
    """
    A School is made up of students, teachers and courses
    """
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student(self, student : Student, course : Course) -> bool:
        """>>>
        search for student in student list and add it to the specified course, if this course is also in the course list
        """
        if student in self.students:
            if course in self.courses:
                course.add_student(student)
                return True
        return False

    def assign_teacher(self, teacher : Teacher, course : Course) -> bool:
        """>>>
        search for teacher in teacher list and add it to the specified course, but only if this course is also in the course list. The teacher has to be qualified in the subject of the course
        """
        if teacher in self.teachers:
            if course in self.courses:
                if teacher.is_qualified(course):
                    course.add_teacher(teacher)
                    return True
        return False

    def print_members(self):
        """>>>
        Prints all courses. For each course, the assigned teacher is also printed, and then all enrolled students. Prints are accomplished by iterating over the lists, not printing the lists themselves
        """
        for course in self.courses:
            print(course)
            print(f"Teachers: {course.teachers}")
            print(f"Students: {course.students}")
        #>>> print the following string: "Unassigned students:" and nothing else
        print("Unassigned students:")
        #>>> check if any student is not enrolled in any course. Print it out
        for student in self.students:
            enrolled = False
            for course in self.courses:
                if student in course.students:
                    enrolled = True
            if not enrolled:
                print(student)
        #>>> print "Unassigned teachers:"
        print("Unassigned teachers:")
        #>>> same for teachers
        for teacher in self.teachers:
            enrolled = False
            for course in self.courses:
                if teacher in course.teachers:
                    enrolled = True
            if not enrolled:
                print(teacher)


def test_school():
    """>>>
    Creates a school object with two courses. Creates three teachers, one of which has a random subject specialization; the other two have the same subject specialization of each of the courses. Assign the two qualified teachers to the approppriate courses. Assign 5 random students to each course. Print the school's members
    """
    school = School("The Python School")
    course_1 = Course("Python", "Programming")
    course_2 = Course("Data Structures", "Programming")
    # TWEAKED -> DEL: course_3 = Course("Algorithms", "Programming")
    teacher_1 = Teacher("Sara", 23, ["Programming"])
    teacher_2 = Teacher("John", 24, ["Programming"])
    #>>> the third teacher has a specilization on Biology
    teacher_3 = Teacher("Sara", 23, ["Biology"])
    school.add_course(course_1)
    school.add_course(course_2)
    # TWEAKED -> DEL: school.add_course(course_3)
    school.add_teacher(teacher_1)
    school.add_teacher(teacher_2)
    school.add_teacher(teacher_3)
    for student in range(5):
        #>>> add the student to the school first, then enroll it in all courses
        school.add_student(Student(f"Student {student}", student))
        for course in school.courses:
            school.enroll_student(school.students[student], course)
    school.assign_teacher(teacher_1, course_1)
    school.assign_teacher(teacher_2, course_2)
    # TWEAKED -> DEL: school.assign_teacher(teacher_3, course_3)
    #>>> attempt to assign teacher_3
    school.assign_teacher(teacher_3, course_1)
    school.print_members()
        
#>>> run test
test_school()







