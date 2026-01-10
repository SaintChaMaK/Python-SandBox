"""
Typecasting is process of converting a variable from one data type to another.
    It uses functions such as str(), int(), float(), bool()
    It's very useful when handling user inputs

"""
Name = "Saint"
Age = 72
Gpa = 7.2
Graduated = True

## Checking datatypes of the above variables
print(type(Name))
print(type(Age))
print(type(Gpa))
print(type(Graduated))

##Typecasting the above variables
#Int and float typecasting
Age = float(Age)
Gpa = int(Gpa)

print(f"{Age} value is {type(Age)}")
print(f"{Gpa} value is {type(Gpa)}")

#Another way of printing out results using print()
print(f"{float(Age)} value is a {type(Age)}")
print(f"{int(Gpa)} value is a {type(Gpa)}")




#Strings typecasting
""" 
#String do behave differently compare to other datatypes such as "int" and "float" datatypes and 
#            strings can not be int or float

"""
Age = str(Age)
Gpa = str(Gpa)

print(f"{Age} value is {type(Age)}")
print(f"{Gpa} value is a {type(Gpa)}")

#Another way of printing out results using print()
print(f"{str(Age)} is a {type(Age)}")
print(f"{str(Gpa)} is a {type(Gpa)}")



#Bolean typecasting
"""
#This is kind different as it can only be True and False
#           so if there is no value it print False and if there is a value it prints True, 
#                                      For example this can be used to check a user have provided an in an input required field
"""

Name = bool(Name)

print(f"{Name} is a {type(Name)}")

#Another way of printing out results using print()

print(f"{bool(Name)} is a {type(Name)}")