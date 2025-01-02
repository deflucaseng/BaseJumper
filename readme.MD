# BaseJumper
### Developed by Lucas Eng


# About

This was developed as part of my journey learning about compilers. In order to start, I created my own turing complete programming language called basejumper, as well as a compiler to 
32bit x86 Assembly for Linux. It has the name basejumper because of the simplicity of the language, which uses human readable words (a fun choice) rather than mathematical symbols.
The **jumper** portion of the name comes from the fact that rather than using traditional loop structure like you would see in more standard languages like Python or C, it uses a conditional
jump which jumps to a line of code and begins executing from there. This language supports both integer operations, and boolean operations. It currently does not have support for strings or 
arrays. 

Safety checks? You don't need safety checks if you only write correct code.

# Syntax

The syntax is intentionally meant to be very human readable (even more than python), so every line reads almost like a sentence. 

## Variable Assignment

'''
x isnow 3
y isnow x
'''
It uses the **isnow** keyword in order to assign variables.

## Evaluated Assignment

You can additionally use assignment statements which perform basic math or boolean operations. 
*These come in three varieties.*


### Numeric Evaluated Assignment

This language supports addition, subtraction, multiplication, and floor division

'''
x isnow y plus 3
f isnow 7 minus 2
z isnow 3 times 5
k isnow b divided 8
'''


### Boolean Comparative Assignment

This language supports and, or, nor, xnor, nand, and xnor
The case used for true and false do not matter here. 

'''
a isnow true or false
b isnow F and k
c isnow false nor false
d isnow x xnor True
e isnow q nand o
f isnow r xnor g
'''

### Numeric Comparative Assignment

This compares two numbers, and stores a boolean value depending on the comparison of the two numbers
This supports equal to and not equal to

'''
y isnow f is equal to 3
z isnow g is not equal to 7
'''

### Conditional Jump

One of the key aspects of this language which is the **jump** functionality utilizes a syntax which 
requires a variable, and thus this language does not directly support infinite looping (Though I suppose
you could if you wanted)


'''
x isnow True
jump to 3 if x
'''

This code would jump to the third line of written code. 

### Printing

Displaying involves using the display keyword followed by whatever variable name or value you would like to print

'''
display 3
display true
display x
'''

### Ending
At the end of the code block simply write end

'''
end
'''


### Important Notes


All files must be of the .eng format (lol)
Conditional jump to line n will jump to the nth line of WRITTEN code not the nth line of the text file. 

