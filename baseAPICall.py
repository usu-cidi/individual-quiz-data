import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
COURSE_ID = os.environ.get('COURSE_ID')
STUDENTS_IN_COURSE = os.environ.get('STUDENTS_IN_COURSE')

BASEURL = 'https://usu.instructure.com'

def getOneQuizData(quizID):
    REQUEST_URL = BASEURL + "/api/v1/courses/" + COURSE_ID + "/quizzes/" + quizID + "/submissions" + "?per_page=" + STUDENTS_IN_COURSE

    shellCommand = f"curl {REQUEST_URL} \
      -X GET \
      -H 'Authorization: Bearer {TOKEN}'"

    oneQuizData = os.popen(shellCommand)

    parsedData = oneQuizData.read()
    oneQuizData.close()

    f = open("canvasData.txt", "w")
    f.write(parsedData)
    f.close()

    return parsedData

