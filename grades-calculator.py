

def grade(name, homework, assessment, final_exam):
    info = {}
    if homework > 25:
        info["error"] = "The max Homework score is 25"
    if assessment > 50:
        info["error"] = "The max Assessment score is 50" 
    if final_exam > 100:
        info["error"] = "The max Final Exam score is 100"
    total_score = homework + assessment + final_exam
    percent = (total_score/175) * 100
    info["name"] = name
    info["score"] = percent
    if percent > 90: 
        grade = "A"
    elif percent > 70:
        grade = "B"
    elif percent > 50:
        grade = "C"
    else:
        grade = "D"
    info["grade"] = grade
    return info

student_score_homework = int(input("Homework: "))
student_score_assessment = int(input("Assessment: "))
student_score_final_exam = int(input("Final Exam: "))
student_name = input("Your Name: ")

score = grade(student_name, student_score_homework, student_score_assessment, student_score_final_exam)
if "error" in score.keys():
    print(score["error"])
else:
    print(f"{score['name']} got {score['score']}% overall which is a {score['grade']}")
