import os
import json
import dotenv
from baseAPICall import getOneQuizData

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
COURSE_ID = os.environ.get('COURSE_ID')
#COURSE_ID = '718488'
BASEURL = 'https://usu.instructure.com'

def getAttemptData(quizID):
    parsedData1 = json.loads(getOneQuizData(quizID))
    quizBlocks = parsedData1["quiz_submissions"]

    attemptData = ""

    for student in quizBlocks:
        for attempt in range(0, student["attempt"]):
            requestURL = BASEURL + "/api/v1/courses/" + COURSE_ID + "/quizzes/" + quizID + "/submissions/" + str(
                student["id"]) + "\?attempt\=" + str(attempt + 1) + " \\"

            shellCommand = f"curl {requestURL} \
                  -X GET \
                  -H 'Authorization: Bearer {TOKEN}'"

            oneAttempt = os.popen(shellCommand)
            attemptData += oneAttempt.read()
            oneAttempt.close()

    return attemptData