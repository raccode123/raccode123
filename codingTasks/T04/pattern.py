'''write code to output pattern shown below using if else statements 
in combination with a single for loop

*
**
***
****
*****
****
***
**
*
'''
#for loop to iterate from 1 to 9, as there are 9 seperate lines
#of input

#2nd attempt.
#added

# Suggestions from reviewer 
##Improve
# Unfortunately I cannot mark this task as complete because you did not follow the task brief. For practical task 2, you were # # # #supposed to use a single for loop with an if/else statement, however you have used 6 conditionals.
# One way to think about this task is to divide it into two halves. The first 5 rows, and the last 4 rows. The if statement can #handle the first 5 rows, while the else block handles all rows greater than 5.

#ATTEMPT that was marked
#range starts on 1 and ends on 10.
for n in range(1,10):  
    if n <= 5:
        print(n * '*')
    else: 
        helper = n - ((n - 5 ) * 2)
        print(helper * '*')


#more dynamic program
#range starts on 1 and ends on 10.
#update from workshop. This was done after marking the above as correct.
num_line = 9

if num_line % 2 != 0:
        print("warning pattern will not print correctly\n")
for n in range(1,num_line): 
      
    if n <= num_line / 2:
        print(n * '*')
    else: 
        invert = num_line - n
        print(invert * '*')