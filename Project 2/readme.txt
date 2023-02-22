I used Visual Studio Code to write this code and have it interact with the apache library from the download link in the specs.
As such, the opening line of the log file might be vastly different from yours.
I simply copied everything the code printed to the terminal in Visual Studio Code for the logfile.
The code assumes that the user will put in the correct user name, password, and file location.
My log file also prints out the entirety of the execute paper.sql call, feel free to skip over that when viewing it.
For option 1 I printed whatever was in the tables requested.
For option 2 I printed whatever the user requests along with the authors related to the paper and a count of the authors.
For option 3 I print any variation of what the user requests. When papers with multiple authors showed up it just prints them more than once.
I assumed this was okay.

If you want to recreate my logfile, these are the inputs I used (I spaced them out for easier readability):

ctato
xorteeth
C:\User\pikac\Downloads\Project 2

1
N
n
J
K
Y
y

2
8888
56

3
n
n
n
n

n
n
n
n
n
n
n

n

3
n
n
2016
short

y
y
y
y
y
y
y

n


3
n
n
2016
short

y
y
y
y
y
y
y

Author

3
Chris
n
n
n

y
y
y
y
y
y
n

n

3
Chris Dyer
n
n
n

y
y
y
y
y
y
n

n

4