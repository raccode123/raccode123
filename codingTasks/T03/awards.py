#ask user for input in minutes
cycling_time=int(input("Input time for cycling in minutes:"))
swimming_time=int(input("Input time for swimming in minutes:"))
running_time=int(input("Input time for running in minutes:"))

#calculate total time in minutes from user input
time = cycling_time + swimming_time + running_time

#start with best time and move down through the time ranges for awards until time must be above 110. 
if (time <= 100):
    award= "Provincial Colours"
elif(time <= 105):
    award = "Provincial Half Colours"
elif(time <=110):
    award = "Provincial Scroll"
else:
    award = "No Award"

#print total time and award
print(f"Total time to complete triathalon: {time} mins. The award you received is: {award}")

