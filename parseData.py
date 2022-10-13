import os
import json
import sys
import Student
from mainAPICall import getAttemptData


def getStudents(quizID):
    f = open("canvasData.txt", "w")
    f.write("")
    f.close()

    resultOfAPICall2 = getAttemptData(quizID)

    from studentInfoAPICall import getStudentData

    resultOfAPICall3 = getStudentData()

    f = open("canvasData.txt", "w")
    f.write("")
    f.close()

    indAttempts = resultOfAPICall2.split("}{")
    studentInfo = resultOfAPICall3.split("}{")

    studentObjs = {}

    # For student data
    for student in range(0, len(studentInfo)):
        if not student == 0:
            studentInfo[student] = "{" + studentInfo[student]
        if not student == (len(studentInfo) - 1):
            studentInfo[student] = studentInfo[student] + "}"

        if studentInfo == ['']:
            return None
        parsedStuData = json.loads(studentInfo[student])
        thisID = parsedStuData["id"]
        studentObjs[thisID] = Student.Student(thisID, parsedStuData["sortable_name"], parsedStuData["sis_user_id"],
                                              parsedStuData["login_id"], parsedStuData["email"])

    # for attempt data
    for attempt in range(0, len(indAttempts)):
        if not attempt == 0:
            indAttempts[attempt] = "{" + indAttempts[attempt]
        if not attempt == (len(indAttempts) - 1):
            indAttempts[attempt] = indAttempts[attempt] + "}"

        if indAttempts[attempt] != '{"errors":[{"message":"The specified resource does not exist."}]}':
            parsedData = json.loads(indAttempts[attempt])
            forInParsedAttempts = parsedData["quiz_submissions"]
            thisID = forInParsedAttempts[0]["user_id"]
            if (thisID in studentObjs):
                studentObjs[thisID].addAttempt(forInParsedAttempts[0], "testQuiz")

    return studentObjs


