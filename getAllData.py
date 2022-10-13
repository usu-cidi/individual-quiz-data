import os
import dotenv
import json

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
COURSE_ID = '718488'

BASEURL = 'https://usu.instructure.com'

REQUEST_URL = BASEURL + "/api/v1/courses/" + COURSE_ID + "/quizzes"

shellCommand = f"curl {REQUEST_URL} \
  -X GET \
  -H 'Authorization: Bearer {TOKEN}'"

quizData = os.popen(shellCommand)

parsedData = json.loads(quizData.read())
quizData.close()

allTheQuizzes = {}

for x in range(0, len(parsedData)):
    allTheQuizzes[parsedData[x]["id"]] = parsedData[x]["title"]

def getAllQuizIDs():
    return allTheQuizzes