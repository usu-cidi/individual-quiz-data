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
import sys
import Student
import csv
from getAllData import getAllQuizIDs
from parseData import getStudents

quizIDs = getAllQuizIDs()


fields = ["Student", "ID", "SIS User ID", "SIS Login ID", "Email", "Quiz", "Score", "Attempt", "Time"]
rows = []

allTheStudents = {}

for quiz in quizIDs:
    print(quiz)
    print(f"quiz: {quiz}")
    callResult = getStudents(str(quiz), allTheStudents)
    if callResult != None:
        students = callResult[0]
        allTheStudents = callResult[1]
        for student in students:
            for attempt in range(0, students[student].getNumAttempts()):
                rowToAdd = [students[student].getName(), students[student].getCanvasID(),
                            students[student].getSisUser(), students[student].getSisLogin(),
                            students[student].getEmail(), quizIDs[quiz], students[student].getScore(attempt),
                            attempt + 1, students[student].getTimeSpent(attempt)]
                rows.append(rowToAdd)

    print(f"Output: {rows}")

outFile = "quizData.csv"

with open(outFile, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

os.remove("canvasData.txt")

os.system('open "quizData.csv"')

