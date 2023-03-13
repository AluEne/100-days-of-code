# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

## Loops

for i in range (2000, 3201): # Selecting numbers from this range
    if i%7 == 0 and i%5!= 0: 
        print(i,end = ',')



# Write a program which can compute the factorial of a given numbers.
# he results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program

n = int(input())

fact = 1
i = 1
while i <= n:
    fact = fact * i;
    i = i + 1
print(fact)