
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0
    for marks in student_marks[query_name]:
        total = total + marks
    percentage = 0
    if total:
        percentage = (total/3)
    print("%.2f" %percentage)
            # print(get_percentage(query_name))
