import os
import sys
import Student
import LetterGrade
import csv
from getAllData import getAllQuizIDs
from parseData import getStudents

quizIDs = getAllQuizIDs()


fields = ["Student", "ID", "SIS User ID", "SIS Login ID", "Email", "Quiz", "Score", "Attempt", "Time"]
rows = []

for quiz in quizIDs:
    students = getStudents(str(quiz))
    if students != None:
        for student in students:
            for attempt in range(0, students[student].getNumAttempts()):
                rowToAdd = [students[student].getName(), students[student].getCanvasID(),
                            students[student].getSisUser(), students[student].getSisLogin(),
                            students[student].getEmail(), quizIDs[quiz], students[student].getScore(attempt),
                            attempt + 1, students[student].getTimeSpent(attempt)]
                rows.append(rowToAdd)

outFile = "quizData.csv"

with open(outFile, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

os.remove("canvasData.txt")

os.system('open "quizData.csv"')

