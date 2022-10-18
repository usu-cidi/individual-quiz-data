# Individual Quiz Data Project
### cidi-individual-quiz-data
Center for Instructional Design and Innovation - Utah State University

* Created by Emma Lynn (a02391851@usu.edu)
* Supervised by Neal Legler, CIDI Director (neal.legler@usu.edu)
* On request from Justin Heavilin, Math Dept. (justin.heavilin@usu.edu)

This repository contains the code necessary to generate a report showing student data from Canvas quiz attempts.

## Start here!
In these instructions, I will walk you through the entire process of running this program to generate your course data.
We will be running the program using the Command Line. When I give you a command to run, it will look like this:
```
$ COMMAND
```
You should not include the $ symbol in the commands you type, that should already display on your command line prompt. Press enter on your keyboard to run the commands once they have been entered.

Commands may or may not output text. Do not worry if some commands do not display anything.

### Instructions

First you will need to get a copy of this project onto your computer.

* Click the green Code button on GitHub. In the dropdown, click Download ZIP

* Navigate to the Launchpad and open the Terminal application
* Navigate to the downloaded project with the following command
```
$ cd Downloads/cidi-individual-quiz-data-master
```

Now we need to set up your environment with your specific settings.
  *  Run the following command
```commandline
$ nano .env
```

  *  Your command line has now been turned into a simple text editor. Copy the text below and paste into the file, filling in your information.
  ```commandline
CANVAS_API_TOKEN=token
COURSE_ID=course-id
STUDENTS_IN_COURSE=upper-limit-of-students
```

* token should be replaced with your personal API key. If you don't have one, see the bottom of this page.
* course-id should be replaced with the id number for your course. It can be found by navigating to the home page of your course on canvas and copying the last part of the url:
  * For example, if your course URL is https://usu.instructure.com/courses/123456, 123456 is the course ID
* upper-limit-of-students should be replaced with a rough estimate of number of students in your course. It is fine if it is greater than the number of students in the course, but should not be less.

* _A note: the terminal is an entirely text based application, thus you won't be able to navigate the text with your mouse, you will need to use the arrows on the keyboard._


* Once you have correctly filled in the text, press _^X_ on your keyboard, followed by the _y_ key, and then the enter key


* Now, run the following command:
```commandline
$ pip3 install python-dotenv --user
```

* Your environment has now been set up!

Running the program:

Run the following command:
```commandline
$ python3 generateReport.py
```
* The program will now begin running. Depending on the amount of students and quizzes in your course, it may take a while because of all the neccesary API calls.
  * My estimation is that it will take around .55 * (number of students * number of quizzes) seconds to run, depending on the number of attempts students are making on the quizzes
* When the program is complete, the generated file should be opened in your default .csv application

If you would like to run the program again for a different course, repeat the above steps, beginning at the command:
```commandline
$ nano .env
```

## Bug Reports
If something behaves unexpectedly or you run into a problem with the program, please let me know.

Send bug reports to A02391851@usu.edu with the subject line "Bug Report - Individual Quiz Data".

Please include:
* What you expected to happen
* What actually happened
* As much output from the terminal as possible - copy and pasted, not in a screenshot
* Your course ID (and specific quiz ID, if applicable)
* What OS you're using (Windows, Mac, etc)
* Any other information that you think could be useful

I will get back to you with an update, most likely within 2 business days. Thank you.

## Getting an API key
https://learninganalytics.ubc.ca/for-students/canvas-api/ is a really great resource that walks you through creating an API key.
 Log in to canvas at usu.instructure.com instead of the ubc.ca link, and everything else in the Generate your Canvas access token section should be applicable.
 
Canvas will only show you your token once. Be sure to copy it down somewhere secure. 

**DO NOT share your access token with anyone.**

Anyone with your token has the ability to act as you in Canvas. If you believe your token may have been exposed, delete it right away. (Link to deletion instructions below.)
 Your token should be password protected at the very least.

Deletion instructions: https://community.canvaslms.com/t5/Student-Guide/How-do-I-manage-API-access-tokens-as-a-student/ta-p/273