# using recursive function
 
def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))
num = 5
print(" The Factorial of ", num,"is",factorial(num))

# --------------------------------------------------------------------------------------------------------------------------

#  WAP to use lambda() into a another function

def calculation():
    return lambda a : a*a
d = calculation()
print(d(2))

#----------------------------------------------------------------------------------------------------------------------------- 

# Make file and  use read, write, open, with open and append functions

f = open("AnnuDhull.txt" ,'w')
f.write(" Hello , I am Annu Dhull . \n I am from Haryana. \n I have completed my BSC from Kurukshetra University . \n currently purusing MCA from CU.")
f.close()

# --------------------------------------------------------------------------------------

f = open("AnnuDhull.txt",'r')
data = f.read()
print(data)
f.close()

# -------------------------------------------------------------

with open("AnnuDhull.txt") as f:
    a = f.read()
    print(a)
f.close()

# ------------------------------------------------------------------

f = open("AnnuDhull.txt" , 'a+')
f.write("\n I want to become AWS SOLUTION ARCHITECT ")
f.seek(0)
d=f.read()
print(d)
f.close()