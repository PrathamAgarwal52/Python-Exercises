if __name__ == '__main__':
    
    students = []
    
    n = int(input().strip())
    
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sort the students based on grades
    students.sort(key=lambda x: x[1])
    
    # Find the second lowest grade
    second_lowest_grade = sorted(set(score for name, score in students))[1]
    
    # Find all students with the second lowest grade
    students_with_second_lowest_grade = [name for name, score in students if score == second_lowest_grade]
    
    # Sort and print the names
    students_with_second_lowest_grade.sort()
    
    for name in students_with_second_lowest_grade:
        print(name)
