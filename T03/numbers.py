#Create a new Python file called numbers.py.
#Ask the user to enter three different integers.
#Then print out:
#The sum of all the numbers
#The first number minus the second number
#The third number multiplied by the first number
#The sum of all three numbers divided by the third number

import math

print("Enter three different intergers.")
int1=int(input("Enter interger number 1: "))
int2=int(input("Enter interger number 2: "))
int3=int(input("Enter interger number 3: "))


int_list=[int1, int2, int3]
#Then print out:

print(f"You entered {int1}, {int2}, {int3}")

# The sum of all the numbers
print(f"{int1} + {int2} + {int3} = ",int1 + int2 + int3)

#The first number minus the second number
print(f"{int1} - {int2} = ",int1 - int2)

#The third number multiplied by the first number
print(f"{int3} * {int1} = ",int3 * int1)

# The sum of all three numbers divided by the third number
cal3 = (int1 + int2 + int3) / int3
print(f"({int1} + {int2} + {int3}) / {int3} = ",cal3)
