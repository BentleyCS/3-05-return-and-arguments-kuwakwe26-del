#Below you will find several older homework questions done correctly using input
#and print statements. our task is to take each one and convert it to arguments and returns instead.


#modify the below function such that it asks the user for 2 numbers as input.
#Then have it print out the larger number
def larger(a,b):
    if( a > b):
        return (a)
    else:
        return (b)
larger(2,3)
#Modify the below function such that it asks for the users score as an input.
#Then based on the score print out a letter grade.
# 90+ A
# 80+ B
# 70+ C
# 60+ D
# 59- F
def grade(g):
    if( g>=90):
        return ("A")
    elif( g>= 80):
        return ("B")
    elif(g >= 70):
        return ("C")
    elif(g >= 60):
        return ("D")
    else:
        return ("F")
grade(65)
#Modify the below function such that it asks the user for a number then
#if the number is divisible by 3 print "fizz"
#if the number is divisible by 5 print "buzz"
#if both are the case then print "Fizzbuzz" instead of the prior two
#if niether are the case print the number.
def fizzBuzz(m):
    if(m%5==0 and m%3==0):
        return( "FizzBuzz")
    elif(m%3==0):
        return ("fizz")
    elif(m%5==0):
        return ("buzz")
    else:
        return(m)

fizzBuzz(15)
#modify the below function such that it asks the user for an input number.
#if the number is even divide it by two.
#if the number is odd multiply it by 3 and add 1
#then print the new number.
def collatz(z):
    if(z==1):
        return (z)
    if(z%2==0):
        return (z/2)
    else:
        return (3*z+1)



collatz(6)

#Modify the below function such that it asks the user for a temperature.
#The format for temperature should end in F For Fahrenheit and C for Celcius
#Then given the temperature if it is in Fahrenheit convert it to Celsius on vice versa
#Example 32F -> 0C  20C -> 68F
def convertTemperature(temp):
    #input = input("Give me a temperature")
    if(temp[len(temp)-1]=="C"):
        temp = int(temp[0:len(temp)-1])
        out = temp*(9/5)+32
        return (str(int(out))+"F")
    elif(temp[len(temp)-1]=="F"):
        temp = int(temp[0:len(temp)-1])
        out = (temp-32)*5/9
        return (str(int(out))+"C")

convertTemperature("86F")