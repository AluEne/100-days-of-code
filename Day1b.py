# Write a program which can compute the factorial of a given numbers.
# he results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program

n = int(input())

fact = 1
i = 1
while i <= n:
    fact = fact * i;
    i = i + 1
print(fact)
