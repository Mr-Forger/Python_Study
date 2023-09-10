studentScores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1:student_grades라는 빈 딕셔너리를 만드세요.
studentGrades = {}

#TODO-2:학생들에 대한 새로운 정보가 들어간 딕셔너리를 완성시키세요.👇
for student in studentScores:
    score = studentScores[student]
    if score > 90:
         studentGrades[student] = "Outstanding"
    elif score > 80:
         studentGrades[student] = "Exceeds Expectations"         
    elif score > 70:
         studentGrades[student] = "Acceptable"     
    else:
         studentGrades[student] = "Fail"
         

# 🚨 Don't change the code below 👇
print(studentGrades)





