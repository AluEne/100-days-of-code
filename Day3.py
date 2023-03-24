# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
# such that is an integral number between 1 and n (both included). 

n = int(input("Kindly input your chosen number: "))

multi = {} # use {} to create a dictionary

for i in range (1, n + 1):
    multi[i] = i * i
print(multi)