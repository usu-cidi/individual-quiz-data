# Copyright (C) 2022  Emma Lynn
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, version 3 of the License.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import csv
from getAllData import getAllQuizIDs
from parseData import getStudents

quizIDs = getAllQuizIDs()

def writeToReport(object, label):
    f = open("contextReport8747525.txt", "a")
    f.write(f"{label}: {object}\n")
    f.close()

writeToReport(quizIDs, "QuizIDs")


fields = ["Student", "ID", "SIS User ID", "SIS Login ID", "Email", "Quiz", "Score", "Attempt", "Time"]
rows = []

allTheStudents = {}

for quiz in quizIDs:
    writeToReport(quiz, "On quiz")
    callResult = getStudents(str(quiz), allTheStudents)
    if callResult != None:
        students = callResult[0]
        allTheStudents = callResult[1]
        for student in students:
            writeToReport(student, "On student")
            for attempt in range(0, students[student].getNumAttempts()):
                writeToReport(attempt, "On attempt")
                rowToAdd = [students[student].getName(), students[student].getCanvasID(),
                            students[student].getSisUser(), students[student].getSisLogin(),
                            students[student].getEmail(), quizIDs[quiz], students[student].getScore(attempt),
                            attempt + 1, students[student].getTimeSpent(attempt)]
                rows.append(rowToAdd)
                writeToReport(rowToAdd, "Row added")


outFile = "quizData.csv"

with open(outFile, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

os.remove("canvasData4737187.txt")
os.remove("contextReport8747525.txt")

os.system('open "quizData.csv"')

