import os
import json
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')

BASEURL = 'https://usu.instructure.com'


def getStudentData(allTheStudents):
    file = open("canvasData.txt")
    resultOfAPICall1 = file.read()
    file.close()
    parsedData1 = json.loads(resultOfAPICall1)
    quizBlocks = parsedData1["quiz_submissions"]

    studentData = ""

    for student in quizBlocks:
        if not student["user_id"] in allTheStudents:
            requestURL = BASEURL + "/api/v1/users/" + str(student["user_id"])

            shellCommand = f'curl {requestURL} -H "Authorization: Bearer {TOKEN}"'

            oneStudent = os.popen(shellCommand)
            readStudent = oneStudent.read()
            studentData += readStudent
            allTheStudents[student["user_id"]] = readStudent
            oneStudent.close()
        else:
            studentData += allTheStudents[student["user_id"]]

    toReturn = (studentData, allTheStudents)
    return toReturn