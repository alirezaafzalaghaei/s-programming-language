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
 
       Should i show snapshot? (y/n) n
       Program output is : 15
    
 - Command:
     
       python3 compiler.py Example.s 2 1
  
 - Output:
 
        Should i show snapshot? (y/n) y
        | i | X1 | X2 | Z1 | Z2 | Z3 | Z4 | Z5 |  Y |
        |-------------------------------------------|
        |0  | 2  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
        |1  | 2  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
        |4  | 2  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
        |5  | 1  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
        |6  | 1  | 1  | 0  | 0  | 0  | 0  | 0  | 1  |
        |7  | 1  | 1  | 1  | 0  | 0  | 0  | 0  | 1  |
        |1  | 1  | 1  | 1  | 0  | 0  | 0  | 0  | 1  |
        |4  | 1  | 1  | 1  | 0  | 0  | 0  | 0  | 1  |
        |5  | 0  | 1  | 1  | 0  | 0  | 0  | 0  | 1  |
        |6  | 0  | 1  | 1  | 0  | 0  | 0  | 0  | 2  |
        |7  | 0  | 1  | 2  | 0  | 0  | 0  | 0  | 2  |
        |1  | 0  | 1  | 2  | 0  | 0  | 0  | 0  | 2  |
        |2  | 0  | 1  | 2  | 0  | 0  | 0  | 0  | 2  |
        |3  | 0  | 1  | 3  | 0  | 0  | 0  | 0  | 2  |
        |9  | 0  | 1  | 3  | 0  | 0  | 0  | 0  | 2  |
        |12 | 0  | 1  | 3  | 0  | 0  | 0  | 0  | 2  |
        |13 | 0  | 0  | 3  | 0  | 0  | 0  | 0  | 2  |
        |14 | 0  | 0  | 3  | 0  | 1  | 0  | 0  | 2  |
        |15 | 0  | 0  | 3  | 1  | 1  | 0  | 0  | 2  |
        |9  | 0  | 0  | 3  | 1  | 1  | 0  | 0  | 2  |
        |10 | 0  | 0  | 3  | 1  | 1  | 0  | 0  | 2  |
        |11 | 0  | 0  | 3  | 2  | 1  | 0  | 0  | 2  |
        |17 | 0  | 0  | 3  | 2  | 1  | 0  | 0  | 2  |
        |20 | 0  | 0  | 3  | 2  | 1  | 0  | 0  | 2  |
        |21 | 0  | 0  | 3  | 2  | 0  | 0  | 0  | 2  |
        |22 | 0  | 0  | 3  | 2  | 0  | 0  | 0  | 3  |
        |23 | 0  | 0  | 3  | 2  | 0  | 0  | 1  | 3  |
        |17 | 0  | 0  | 3  | 2  | 0  | 0  | 1  | 3  |
        |18 | 0  | 0  | 3  | 2  | 0  | 0  | 1  | 3  |
        |19 | 0  | 0  | 3  | 2  | 0  | 1  | 1  | 3  |
        
        Program output is :  3

     
## Other implementations:

 - https://github.com/siyanew/PMG
