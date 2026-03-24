"""In this exercise you will write a program for printing
out grade statistics for a university course.

The program asks the user for results from different students
on the course. These include exam points and numbers of exercises
completed. The program then prints out statistics based on the results.

Exam points are integers between 0 and 20. The number of exercises
completed is an integer between 0 and 100.

The program keeps asking for input until the user types in an empty
line. You may assume all lines contain valid input, which means that
there are two integers on each line, or the line is empty."""


def input_data() -> list[int]:
    data: list[int] = []
    input_data: list = []

    while True:
        input_values = input("Exam point and exercises completed: ")
        value = input_values.split()
        if input_values == "":
            break
        input_data.append(value)
    for value in input_data:
        for string in value:
            data.append(int(string))

    return data


def exam_points(data: list[int]) -> list[int]:
    points: list[int] = []
    index: int = 0
    for number in data:
        if index == 0 or index % 2 == 0:
            points.append(number)
        index += 1

    return points


def completed_exercises(data: list[int]) -> list[int]:
    points: list[int] = []
    index: int = 1
    for number in data[1:]:
        if not index % 2 == 0:
            points.append(number)
        index += 1
    return points


def exercise_points(completed_exercises: list[int]) -> list[int]:
    points: list[int] = []
    for value in completed_exercises:
        points.append(value // 10)

    return points


def total_points(exam_points: list[int], exercise_points: list[int]) -> list[int]:
    points: list[int] = []
    index: int = 0
    for point in exam_points:
        result: int = point + exercise_points[index]
        points.append(result)
        index += 1

    return points


def passed_or_not(exam_points: list[int]) -> list[bool]:
    passed: list[bool] = []
    for value in exam_points:
        if value < 10:
            passed.append(False)
        else:
            passed.append(True)
    return passed


def grades(total_points: list[int], passed_or_not: list[bool]) -> list[int]:
    grades: list[int] = []
    for value in total_points:
        if value <= 14:
            grades.append(0)
        elif value <= 17:
            grades.append(1)
        elif value <= 20:
            grades.append(2)
        elif value <= 23:
            grades.append(3)
        elif value <= 27:
            grades.append(4)
        elif value <= 30:
            grades.append(5)

    # Update final grade if exam_points < 10
    index = 0
    for value in grades:
        if not passed_or_not[index]:
            grades[index] = 0
        index += 1

    return grades


def points_average(total_points: list[int]) -> float:
    average: float = sum(total_points) / len(total_points)
    return average


def pass_percentage(grades: list[int]) -> float:
    sum_passed: int = 0
    for grade in grades:
        if grade != 0:
            sum_passed += 1
    percentage: float = (sum_passed / len(grades)) * 100
    return percentage


def distribution(grades: list[int]) -> None:
    values: list[int] = [5, 4, 3, 2, 1, 0]
    print("Grade distribution: ")
    for value in values:
        print(f"{value:>2}: {'*' * grades.count(value)}")


def main():
    data = input_data()
    # print(data)
    # exams = exam_points([15, 87, 10, 55, 11, 40, 4, 17])  # hard coded for testing
    # data = [15, 87, 10, 55, 11, 40, 4, 17]  # hard coded for testing
    exams = exam_points(data)
    completed = completed_exercises(data)
    # print(f"Exercises completed: {completed}")
    # print(f"Exams points: {exams}")
    exercises = exercise_points(completed)
    # print(f"Exercise points: {exercises}")
    total = total_points(exam_points=exams, exercise_points=exercises)
    # print(f"Total points: {total}")
    approved = passed_or_not(exam_points=exams)
    final_grades = grades(total, approved)
    # print(f"Passed by exam: {approved}")
    # print(f"Grades: {final_grades}")
    print("Statistics: ")
    print(f"Points average: {points_average(total):.1f}")
    print(f"Pass percentage: {pass_percentage(final_grades):.1f}")
    distribution(final_grades)


# main()
data = input_data()
exams_points = exam_points(data)
completed = completed_exercises(data)
exers_points = exercise_points(completed)
total = total_points(exams_points, exers_points)
aproved = passed_or_not(exams_points)
final_grades = grades(total, aproved)
print("Statistics: ")
print(f"Points average: {points_average(total):.1f}")
print(f"Pass percentage: {pass_percentage(final_grades):.1f}")
distribution(final_grades)
