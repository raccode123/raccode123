'''write a programme that continually ask the user to enter a number.
When the user enters -1 the program should stop requesting the user to enter a number
The prgram must then calculate the average of the numbers emtered excluding -1
make use of the while loop repition structure to implement the program'''

## ask user to input numbers
#if number does not == -1, add it to list
#set variables 
sum= 0
count = 0 
avg = 0

#while true loop.
#if user number isn't -1 then count iteration, sum user_number and save sum/count into av variable

while True:
    user_number = int(input("Enter number: "))
    if user_number != -1:
        count += 1
        sum += user_number
        avg=sum/count
        continue    #continue allows loop to not break
    else: 
        print(f"The average of the input numebrs is: {avg:.2f}")
        break
