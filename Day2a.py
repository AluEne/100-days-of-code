````
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.

n = int(input("Kindly input a number of your choice: ")) # Take the input as an int not a string

fact = 1
i = 1

while i <= n: # when i is less than or equal to n
    fact = fact * i;   # Multipy fact by i
    i = i + 1 # For every loop add 1 to i

print(fact)
