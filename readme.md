# S Programming Language


There is a Programming language that provided in the second section of `Computability,Complexity, and Languages Fundamentals of Theoretical Computer Science` book by `Martin D. Davis, Ron Sigal and Elaine J. Weyuker`

This programming language has 3 statements:

    [A] X1 <- X1 + 1 # addition
    X1 <- X1 - 1 # subtraction 
    IF X1 != 0 GOTO A # jump

Which `[A]` is label.

## Variable naming

- Inputs are X1, X2, ...
- Temporary variables are Z1, Z2, ... which all of them initialized to `0`.
- Program result will save in variable `Y` which this also initialized to `0`.
- Label names include A1, B1, C1, D1, E1, A2, B2, ... . Special label `E` refers to the end of program.

## Other tips

- All variables values are members of Natural numbers.
- Tested on python 3.6.7 in Kubuntu 18.10

## Requirements

 - Python 3
 - `goto-statement` module. Install it via `pip install goto-statement`
 
 
## Usage
 
- Clone (or download) the project.
- Open a terminal (or CMD) and change directory to project folder (via `cd` or ...)
- Compile and Run your program using this command:
  
      python3 compiler.py example.s inputs_seprated_via_space
 
 
## Example
 
Here i wrote a program which gets two input and returns sum of them.
 
 - Example.s:
    
        [A] IF X1 != 0 GOTO B
        Z1 <- Z1 + 1
        IF Z1 != 0 GOTO C
        [B] X1 <- X1 - 1
        Y <- Y + 1
        Z1 <- Z1 + 1
        IF Z1 != 0 GOTO A
        
        [C] IF X2 != 0 GOTO D
        Z2 <- Z2 + 1
        IF Z2 != 0 GOTO A2
        [D] X2 <- X2 - 1
        Z3 <- Z3 + 1
        Z2 <- Z2 + 1
        IF Z2 != 0 GOTO C
        
        [A2] IF Z3 != 0 GOTO B2
        Z4 <- Z4 + 1
        IF Z4 != 0 GOTO E
        [B2] Z3 <- Z3 - 1
        Y <- Y + 1
        Z5 <- Z5 + 1
        IF Z5 != 0 GOTO A2
        
 - Command:
     
         python3 compiler.py Example.s 7 8
  
 - Output:
       
       15
     
     
## Other implementations:

 - https://github.com/siyanew/PMG
