
"""
variables are names that can be assigned a value and used
to reference that value throughout your code. Variables are fundamental to programming for two reasons:
1. Variables keep values accessible: For example, the result of
some time-consuming operation can be assigned to a variable so
that the operation does not need to be performed each time you
need to use the result.

2. Variables give values context: The number 28 could mean lots
of different things, such as the number of students in a class, or the
number of times a user has accessed a website, and so on. Naming
the value 28 something like num_students makes the meaning of the
value clear.


"""

""" 
Variables are containers for a storing data value, 
            it can store data of different types, and different types can do different things.

"""

"""
The Assignment Operator
Values are assigned to a variable using a special symbol = called the
assignment operator. An operator is a symbol, like = or +, that
performs some operation on one or more values.

Although = looks like the equals sign from mathematics, it has
a different meaning in Python. Distinguishing the = operator
from the equals sign is important, and can be a source of frustration for beginner programmers.
Just remember, whenever you see the = operator, whatever is to
the right of it is being assigned to a variable on the left.

"""


# Rules for a valid Variable names

"""
         Do not need to be declared by any particular type, since type can be changed even after setting it.
         
    01. The name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
            They can't have spaces (E.x, test var is not allowed)
                                    (E.x, test_var! is not allowed)
    02. The name of the variable must begin with a letter
    03. The underscore character is a letter
                    _vart = 23
                    tyyt = 21
                    print(_vart)
                    print(tyyt)
    04. Variables are Case-sensitive which means,
                upper- and lower-case letters are treated as different
                      (a little differently than in the real world where Saint and SAINT are the same first names,
                        but in Python they are two different variable names, and consequently, two different variables)

    05. The name of the variable must not be any of Python's reserved keywords or predefined.
                ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 
                'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
                  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
                  'return', 'try', 'while', 'with', 'yield']
Then, to create the variable, you need to use = to assign the value that you want it to have.

You can always take a look at the value assigned to the variable by using print() and putting the name of the variable in parentheses.

"""

#Examples of Variables
number = 2    #int
name = "Saint"  #string
decimal = 3.5   #float
bool = True     #boolean can be True or False depending on the condition

#print(number)
#print(name)
#print(decimal)
#print(bool)





# Implementation of Rules for a valid Variable names

"""
Variable names are case-sensitive, so a variable named phrase is distinct from a variable named Phrase (note the capital P). For instance,
the following code produces a NameError:

So is adviced to double-check that every character in your code—including
spaces—exactly matches. Computers can’t use common
sense to interpret what you meant to say, so being almost correct
won’t get a computer to do the right thing!

"""
phrase = "Hello, World"
print(Phrase)




#assingment
test_var = 4 + 5
#print(test_var)

#manipulating a variable
New_var = 3
#print(New_var)

New_var = 700   #manipulation
#print(New_var)

#print(test_var)
#print(New_var)


New_var = New_var ** 2
#print(New_var)




#Using multiple variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

days_per_year = 365.25
#Calculating the number of seconds for 4 years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
#print(total_secs)

#print(total_secs)






#global variables 
"""
Any variable created outside a function can be accessed within any function and so they have global scope.

"""

x = 5   #global variable
y = 10  #global variable
def sum():
    sum = x + y
    return sum
#print(sum())

#another example
second_word = "Awesome" #global variable

"""
def message():
    print(f"Python is, {second_word}")
message()
"""

# local variable 
"""
a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
"""
def message():
    second_word = "Fantastic" #local variable
    print(f"Python is, {second_word}")
message()

#print(f"Python is, {second_word}")





#Solving simple mathematical problems
"""
        pythagorean theorem
        √ (x)  = x(½) == x**0.5
        c = √ a2 + b2 ==  c = ((a**2) + (b**2)) **0.5
       
"""
#simple pythagorean theorem calculator
#a = float(input("Enter value of a:"))
#b = float(input("Enter value of b:"))
#c = ((a ** 2) + (b ** 2)) ** 0.5
#print("c =", c)






#some calc
john = 3
mary = 5
adam = 6

#print(john, mary, adam, sep = ",")

total_apples = john + mary + adam
#print(total_apples)

total_apples = john - mary - adam
#print(total_apples)

total_apples = john * mary * adam
#print(total_apples)

total_apples = john / mary / adam
#print(total_apples)

total_apples = john // mary // adam
#print(total_apples)

total_apples = john % mary % adam
#print(total_apples)






#Shortcut operators
"""
        variable = variable op expression

        ...then it can be simplified and shown as follows:

        variable op= expression
        Example:
        x = x * 2
        sheep = sheep + 1
    Python offers you a shortened way of writing operations like these, which can be coded as:
        x *= 2
        sheep += 1

    In which the operator should be close to the equal sign
"""
x = 2
x *= 2
#print(x)

sheep = 5
sheep += 2
#print(sheep)

#i = float(input("Enter value of i:"))
#j = float(input("Enter value of j:"))
#i = i + 2 * j   #normally
#i += 2 * j  #Simplified

#var = float(input("Enter VAR:"))
#var = var/2 #normally
#var /= 2    #simplified

#rem = float(input("Enter REM:"))
#rem = rem % 10  #normally
#rem %= 10   #simplified

#j = j - (i + var + rem) #normally
#j -= (i + var + rem) #Simplified

#print(j)






#LAB
kilometers = 12.25
miles = 7.38

miles_to_kilometers = 10.23445
kilometers_to_miles = 20.45543345

#print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
#print(f"{miles} miles is {round(miles_to_kilometers,2)} kilometers")

#print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#print(f"{kilometers} kilometers is {round(kilometers_to_miles,3)} miles")


#Summary
"""
        A variable is a named location reserved to store values in the memory.
                     A variable is created or initialized automatically when you assign a value to it for the first time.
                                            E.x  a = 1
                                                 b = "Saint"
                                                 c = 1.2

        Variable must have a unique name or an identifier.
                     A legal identifier name must be a non-empty sequence of characters,
                      can with the underscore(_), or a letter, and it cannot be a Python keyword. 
                      The first character may be followed by underscores, letters, and digits.
                       Identifiers in Python are case-sensitive.

        Python is a dynamically-typed language,
                     which means you don't need to declare variables in it.
                     To assign values to variables, you can use a simple assignment operator in the form of the equal (=) sign.

        03. compound assignment operators (shortcut operators) can be used to modify/ format values assigned to variables,
                     for example: var += 1,
                                  var /= 5 * 2.

        04. You can assign new values to already existing variables using the assignment operator or one of the compound operators,
         for example:
            var = 2
            print(var)

            var = 3
            print(var)

            var += 1
            print(var)


"""


a = 6
b = 3
a /= 2 * b # a = a / 2 * b
#print(a)
"""
the answer is 1.0, atleast for what i know is because
     of the fact that The result produced by the division operator is always a float
"""