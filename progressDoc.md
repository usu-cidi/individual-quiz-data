# Individual Quiz Data Project
Center for Instructional Design and Innovation - Utah State University
* Created by Emma Lynn (a02391851@usu.edu)
* Supervised by Neal Legler, CIDI Director (neal.legler@usu.edu)
* On request from Justin Heavilin, Math Dept. (justin.heavilin@usu.edu)


**_Documentation of progress on the project, if anyone is interested_**

## Project Goals
* Generate a report for each attempt for each student of their score and time they took to take the quiz
* Output into .csv file
* Get data for all quizzes in course
* Get identifying information for all students
* Get ahold of students who are failing the course

### Data to retrieve
* For all quizzes in a course
  * For each student
  * Name, Canvas ID, SIS User ID, A number, email?
      * For each attempt
        * Time spent
        * Score


## Progress Report

### 9.28.2022
* Began looking into Canvas API
* Added test students to sandbox course to begin generating data for testing

### 9.30.2022
* Began experimenting with making calls to the Canvas API
* Looked into parsing the returned JSON into a usable format
* Successfully made a call to the Canvas API from the command line, retrieving my user data
* Began figuring out making calls to the API from a python script
* Created initial GitHub repository to store progress

### 10.3.2022
* Continued to work on Python script to put data into usable format
* Found new API call to get all attempts on quiz
* Generated test student data

### 10.4.2022
* Neal and I met with Justin Heavilin to discuss the project
  * I showed him what I had done so far and he liked the direction I have been going
  * Specific requests for features:
    * Output that is able to be pulled into MatLab
      * A .csv file would be good
    * List students' A-numbers with their data
    * Provide a way to get ahold of all students failing the course
      * See note in project goals
    * Get the data for all quizzes in a course
* Finished implementing API call to get individual quiz attempts
* Beginning to get a little worried about runtime complexity, there is going to be quite a bit of clean up needed once the program is functional.

### 10.5.2022
* Created a Student class to hold the data from all attempts for each of the students
* Successfully added the data to instances of the class
* Successfully output a simple report with most of the necessary data
```buildoutcfg
-------- 1754612 --------
--Attempt 1--
Score: 2.0
Time begun: 2022-09-26T15:03:13Z
Time ended: 2022-09-26T15:03:35Z
Time spent: 22 seconds
--Attempt 2--
Score: 0.0
Time begun: 2022-09-26T15:04:21Z
Time ended: 2022-09-26T15:04:28Z
Time spent: 8 seconds
--Total--
Final score: 2.0
Total attempts: 2
Total time spent: 30.0 seconds
---------------------------

-------- 1262069 --------
--Attempt 1--
Score: 4.0
Time begun: 2022-09-27T23:00:41Z
Time ended: 2022-09-27T23:01:04Z
Time spent: 23 seconds
--Total--
Final score: 4.0
Total attempts: 1
Total time spent: 23.0 seconds
---------------------------
```
* Began creating documentation for the project

Can currently be run with these commands in the terminal:

    $ python apiCall4.py > attemptData.txt
    $ python interpreting_data.py

### 10.6.2022
* Created interpreting_data.py file to generate the aggregate data
* Successfully generated report listing average quiz score, average time spent per student, average attempts made per student, and the average time and attempts taken for each letter grade
```buildoutcfg
Average score: 66.67%
Average total time spent per student: 1.391 minutes (83.43 seconds)
Average attempts made per student: 1.29
-----------------------------------
A (100+ - 93%):
---Grade received by 2 students
---They took an average of 193.0 total seconds on the assignment
---They used an average of 1.0 attempts
D (66.9 - 60%):
---Grade received by 3 students
---They took an average of 45.0 total seconds on the assignment
---They used an average of 1.33 attempts
F (59.9 - 0%):
---Grade received by 2 students
---They took an average of 31.5 total seconds on the assignment
---They used an average of 1.5 attempts
```

* Fixed the number of attempts problem as well as the student ID problem I forgot about
* Put output into requested format and file type
* Can currently be run with these commands in the terminal:
```commandline
    $ python apiCall3.py > canvasData.txt
    $ python apiCall4.py > attemptData.txt
    $ python interpreting_data.py
```
Results will be contained in quizData.csv file.
* Worked to optimize runtime: currently acceptable. Will have to be monitored as the problem size grows.

### 10.7.22
* dotenv is working again, although today I'm on the machine that it was working the whole time on, so I'll probably need to do more work with it when I'm back on one of my other two computers I work on.
* Created clean copies of the source code, adding to new git repository - this should be the one I eventually give out with the finished product
* Creation of new git repository was successful - tagged commit with addedFiles
* Can now be run with these commands in the terminal:
```commandline
    $ python baseAPICall.py > canvasData.txt
    $ python mainAPICall.py > attemptData.txt
    $ python generateReport.py
```
Results will be contained in quizData.csv file.
* Began creating larger data set for testing

### 10.10.22
* Continued creating data set for larger testing

### 10.11.22
* Finished creating the larger data set, adding edge cases
* dontev seems to be working on the computer it wasn't before, so I don't know what that was about
* Tested with new data
* Fixed a few bugs caused by edge cases
* Emailed Justin Heavilin to ask some clarifiying questions about desired output as well as get feedback on the current output
* Tested runtime with the bigger data set
* Began creating usage documentation - README.md

### 10.12.22
* Got an email back from Justin Heavilin clarifying exactly what output he wants. And it is not exactly what we thought he had wanted.
* I think I am going to duplicate this project because I think the current implementation could still be useful, and then change the new file to reflect the data he wants.
* We are now in the new project. I have changed the name from Aggregate Quiz Data to Individual Quiz Data for clarity
* Updated this documentation with the new project requirements
* Changed output to reflect new requirements
* Began pulling student data from API
* Can now be run with these commands in the terminal:
```commandline
    $ python baseAPICall.py > canvasData.txt
    $ python mainAPICall.py > attemptData.txt
    $ python studentInfoAPICall.py > studentData.txt
    $ python generateReport.py
```

### 10.13.22
* Finished getting required user data and formatting correctly
* Utilized os.popen to consolidate commands needed to run program
* Began expanding program to get data from all quizzes
* About every other time the JSON won't work. I don't know why :/
* Can now be run with this command in the terminal:
```commandline
    $ python generateReport.py
```
* Got it working to display correct data from all the quizzes
* Fixed a bug that left off one attempt from every quiz
* Finished first draft of usage docs
* Added to clean repo

### 10.17.22
* Added a dictionary to keep track of student data that has already been retrieved to minimize API calls
  * Updated time complexity docs
  
* Tested on an actual calc 1 course: 707454
```commandline
5.05s user 2.41s system 6% cpu 1:58.33 total
```
  Follows time to run estimation pretty well

* Also tested on course 711908
```commandline
6.54s user 3.22s system 6% cpu 2:34.77 total
```
Was actually much faster than my estimation, I think it was probably because students were only allowed one attempt on every quiz. That's maybe something to factor into my time approximation in the future.


### 10.18.22
* Tested on one of Justin Heavilin's courses (707503)
```commandline
17.58s user 9.27s system 6% cpu 7:15.64 total
```
This was a lot bigger of a data set, but still wasn't terrible.
My current estimation was a little off, a better one for this larger data would probably be .604 * (students * quizzes)



## TODO:
* Test on Windows/Linux



## Runtime optimization:
Using command line argument *time* to measure runtime

Where:
* s is number of students in a course
* q is number of quizzes in a course
* a is the number of attempts made for one student

### Current implementation
#### 10.13.22

    1.29s user 0.65s system 6% cpu 29.394 total
* It's kind of slow, but I don't know if there's much I can do about it, since it's really just the API calls
* 30 seconds for 18 students and 3 (active) quizzes
  * Estimation: .556 seconds * (number of students * number of quizzes in course)
  
#### 10.17.22
```commandline
1.20s user 0.59s system 6% cpu 26.341 total
```
* After removing repeat API calls for student data- doesn't make as much of an impact on my data, but in general I think it will help a lot
* New estimation: .487 seconds * (number of students * number of quizzes)

### Old implementation

#### baseAPICall.py ~~apiCall3.py~~
##### 10.6.22 (Initial - Trying to get stats quiz tiny data): 

    0.03s user 0.01s system 10% cpu 0.452 total
* There's not so much that I think really can be done here. The only thing that would slow it down is that API call and we need to have that.
* Complex elements:
  * One API call per quiz
* O(1) complexity (except maybe the API call)

##### 10.11.22 (Aggregate quiz data project - more data):
    
    0.05s user 0.02s system 11% cpu 0.573 total

* No significant difference in performance (also, will not change based of problem size - O(1))

#### mainAPICall.py ~~apiCall4.py~~
##### 10.6.22 (Initial - Trying to get stats quiz tiny data): 

    0.22s user 0.10s system 6% cpu 4.660 total
* This could be a longer one because the time is going to be directly related to the amount of API calls made.
* To get the data we need, I'm pretty sure we need to make all these calls.
* We're making an API call for every attempt for every student, eventually for every quiz in the course, which will get expensive.
* It's not a big deal with my small data, but as data gets bigger I think this is going to be a big concern for me.
* I have looked through all the documentation for the Canvas API and I really don't think there's another way to get this data, so I think I'm just going to have to make it work
* Complex elements:
  * Reading in the resultant file from apiCall3.py (result of one API call) - O(1)
  * Loading the result of that file with JSON - O(1)
  * Iterating through the quizBlocks dictionary of size s - O(s)
  * Iterating through the quizBlockIDs dictionary of size s - O(sa) (was able to remove)
    * Iterating through attempts for each student of size a
      * API call (one for every attempt made by every student on the quiz)
* O(sa) complexity
* Do we really need to iterate through quizBlocks and quizBlockIDs??
  * Epic we do not have to! That improves things!!


    0.22s user 0.10s system 6% cpu 4.620 total
* There's not really a noticeable difference now since my data's so small but I think that will be beneficial as the problem size increases.
* Still O(sa) complexity, but we've cut down on an additional O(s)

##### 10.11.22 (Aggregate quiz data project - more data):
    
    0.51s user 0.23s system 6% cpu 11.987 total

* About twice as long, which makes sense because there's about twice as much data
* This isn't ideal because in this situation, runtime is directly proportional to the problem size
* But there's really nothing we can do about it, I don't think because we really have to make all of those API calls
* This example had 30 attempts and 18 students, which means that on average runtime will probably take (.4 * num of attempts) seconds or (.667 * num of students) seconds
  * Which is not ideal, that could get pretty slow, but there's nothing I can really do about it I don't think.

#### generateReport.py ~~interpreting_data.py~~
##### (Contains calls to parseData.py ~~parseJSON.py~~, Student.py, and LetterGrade.py)

##### 10.6.22 (Initial - Trying to get stats quiz tiny data): 

    0.02s user 0.01s system 89% cpu 0.034 total
* This is probably the most complex call to analyze complexity for, but I doubt it will take longer than the previous API calls
* It still is likely going to get a lot of data pushed through it though, so I should work through it
* Complex elements:
  * getStudents() from parseJSON.py - O(as)
    * Complex elements:
      * Reading the result of apiCall4.py of size as - O(as)
      * Splitting up the result of the read in file - O(as)
      * Iterating through the individual attempts - O(as)
      * Iterating through the parsedAttempts - O(as) (was able to remove)
      * Iterating through the students - O(s) (technically not there cause it's just output for me)
    * Attempting to minimize the O(as)s cause that's not ideal
      * Successfully combined iterating through the individual attempts and the parsed attempts!! That should help.
    * Data structures: attempting to change parsedAttempts from a list to a set, order shouldn't matter I don't think
      * Apparently you can't have a set of lists. Damn.
  * Iterating through the letter grades - O(1)
  * Iterating through the students - O(s)
    * getPercentage() from Student.py - O(1)
    * getTotalTimeSpent() from Student.py - O(1)
    * getNumAttempts() from Student.py - O(1)
    * getLetterGrade() from LetterGrade.py - O(1)
    * addStudentData() from LetterGrade.py - O(1)
  * Iterating through the letter grades again - O(1) * (O(a)) + O(s) = O(s)
    * getNumStudents() from LetterGrade.py - O(1)
    * getUpperBound() & getLowerBound() from LetterGrade.py - O(1)
    * getAvgTime() from LetterGrade.py - O(a)
    * getAvgNumAttempts() from LetterGrade.py - O(s in letter grade)
* O(sa) complexity

##### 10.11.22 (Aggregate quiz data project - more data):
    
    0.02s user 0.01s system 89% cpu 0.034 total

* Still very fast. I'm not worried here much at all.


## Sources:
* https://learninganalytics.ubc.ca/for-students/canvas-api/
* https://usu.instructure.com/doc/api/index.html
* https://macblog.org/parse-json-command-line-mac/
* https://github.com/ubccapico/getting-started-with-the-canvas-api-with-python
* https://usu.instructure.com/doc/api/quiz_submissions.html
* https://usu.instructure.com/doc/api/all_resources.html#method.users.api_show
* https://github.com/ubccapico/canvas_api_examples/blob/master/api_scripts/python/simple_env.py
* https://github.com/ubccapico/getting-started-with-the-canvas-api-with-python
* https://community.canvaslms.com/t5/Canvas-Question-Forum/Get-All-Quiz-Submissions-API-not-working/td-p/218389
* https://www.usu.edu/teach/help-topics/teaching-tips/procedural-faqs
* https://www.geeksforgeeks.org/writing-csv-files-in-python/
* https://askubuntu.com/questions/53444/how-can-i-measure-the-execution-time-of-a-terminal-process
* https://www.digitalocean.com/community/tutorials/workflow-timing-command-execution
* https://12factor.net/
* https://pypi.org/project/python-dotenv/
* https://community.canvaslms.com/t5/Canvas-Developers-Group/Submissions-API-not-returning-all-submissions/td-p/51725
* https://canvas.instructure.com/doc/api/file.pagination.html
* https://janakiev.com/blog/python-shell-commands/