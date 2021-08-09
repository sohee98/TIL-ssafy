def solution(scores):   
    grades_list = []
    for i in range(len(scores)):
        stu_scores = []
        for stu in range(len(scores)):
            stu_scores.append(scores[stu][i])

        if scores[i][i] == max(stu_scores) or scores[i][i] == min(stu_scores):
            if stu_scores.count(scores[i][i]) == 1:
                stu_scores.remove(scores[i][i])

        score = sum(stu_scores)/len(stu_scores)
        if score >= 90:
            grades = 'A'
        elif score >= 80:
            grades = 'B'
        elif score >= 70:
            grades = 'C'
        elif score >= 50:
            grades = 'D'
        else:
            grades = 'F'
        grades_list.append(grades)
    
    answer = ''.join(grades_list)
    return f"{answer}"

solution([[50,90],[50,87]])