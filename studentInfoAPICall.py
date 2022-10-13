import os
import json
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')

BASEURL = 'https://usu.instructure.com'


def getStudentData():
    file = open("canvasData.txt")
    resultOfAPICall1 = file.read()
    file.close()
    parsedData1 = json.loads(resultOfAPICall1)
    quizBlocks = parsedData1["quiz_submissions"]

    studentData = ""

    for student in quizBlocks:
        requestURL = BASEURL + "/api/v1/users/" + str(student["user_id"])

        shellCommand = f'curl {requestURL} -H "Authorization: Bearer {TOKEN}"'

        oneStudent = os.popen(shellCommand)
        studentData += oneStudent.read()
        oneStudent.close()

    return studentData