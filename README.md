# student_schedule_tracker
Motivation and Task Description: As a student of IUT, I have multiple classes of different courses like Mathematics, Computer 
programing, Microeconomics, Financial Management, Statistics. Also, I have few lab classes 
to attend. I often forget about these classes timing, rooms especially during busy week.
Instead of manually checking the class timing and rooms, I came up a solution of Automating
Today’s Class & Lab Schedule with python programming
It's worth automating because it is more efficient, less time consuming, more convenient and 
it reduces the possibility of missing classes(error-reduction).
Previous Approach: Previously, I used to open the class routine PDF/PNG/Excel sheet manually every single time 
or ask my friends in WhatsApp/Messenger or memorize the schedule.
This manual approach of checking the routine wasted time, or sometimes led to forget a class
or created confusion or led to arrive late. This makes the previous approach inefficient.
Proposed Automation: The proposed automation is Class & Lab Schedule Reminder with python programing.
This automates the whole process by reading a CSV file that contains course name, day, 
time, room, and type (Classes or Labs). The python program will automatically detect the 
current date and show the scheduled activities for that day. What the automation brings:
• Will always be notified about the scheduled classes and labs for that day.
• No need to check multiple sources (PDF/WhatsApp/Messenger) manually.
• It enhances time management and helps avoiding missing classes and labs and 
reduces the confusion.
Pseudo-code (Step by step):
1. Create a CSV file and store the schedule there with columns: Day, Course, Time, 
Room, Type.
2. Using Python’s csv.DictReader and store each of the row as a dictionary read the CSV 
file.
3. By using the Python’s datetime module detect today’s day.
4. Filter schedule to get only rows where day == today.
5. If there’s no classes/labs are found, print “No Classes Today”.
6. If classes or labs are found, iterate through each item and print: Course name, Type 
(Lecture or Lab), Time, Room
7. End the program.
