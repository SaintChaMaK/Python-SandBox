"""
Docstring for The-First-Python-Program.Errors

Mistakes made in a program are called errors, and there are two
main types of errors you’ll experience:
1. Syntax errors
2. Run-time errors
In this section you’ll see some examples of code errors and learn how
to use the output Python displays when an error occurs to understand
what error occurred and which piece of code caused it.

"""

# Syntax errors
"""
 a syntax error occurs when you write some code that
isn’t allowed in the Python language. 

"""
# Examples

#print("Hello, World)

"""
Upon running the code an error is displayed which is known as EOL which stands for End Of Line, so this message tells you that Python
read all the way to the end of the line without finding the end of something called a string literal.
A string literal is text contained in-between two double quotation
marks. The text "Hello, world" is an example of a string literal.  

"""

"""
Back in the script window, notice that the line containing with "Hello,
world is highlighted in red. This handy features helps you quickly find
which line of code caused the syntax error.

"""





# Run-time errors

"""
IDLE catches syntax errors before a program starts running, but some
errors can’t be caught until a program is executed. These errors are
known as run-time errors because they only occur at the time that
a program is run.

"""
#print(Hello, World)

"""
Now both quotation marks from the phrase "Hello, world" have been
removed. Did you notice how the text color changes to black when
you removed the quotation marks? IDLE no longer recognizes Hello,
world as a string.

"""

"""
What happened? While trying to execute the program Python raised
an error. Whenever an error occurs, Python stops executing the program and displays the error in IDLE’s interactive window.
The text that gets displayed for an error is called a traceback. Tracebacks give you some useful information about the error. The traceback above tells us all of the following:
• The error happened on what line of the script.py.
• The line that generated the error was: print(Hello, World).
• A NameError occurred.
• The specific error was name 'Hello' is not defined
The quotation marks around Hello, world are missing, so Python
doesn’t understand that it is a string of text. Instead, Python thinks
that Hello and world are the names of something else in the code.
Since names Hello and world haven’t been defined anywhere, the
program crashes.

"""
