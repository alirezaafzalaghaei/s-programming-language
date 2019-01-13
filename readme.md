
# S Programming Language Compiler


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
- Tested on python 3.6.7 in Kubuntu 18.10 and Lubuntu 16.04

## Requirements

 - Python 3
 - `goto-statement` module in order to add goto support
 - `sympy` module for prime factorization 
 
 To install dependencies just run this:
    
    pip install -r requirements.txt
 
## Usage
 
- Clone (or download) the project.
- Open a terminal (or CMD) and change directory to project folder (via `cd` or ...)
- If you have program source code you just need to compile and run it using this command:
  
      python3 compiler.py example.s inputs_seprated_via_space
- but if you have code (godel number) of program you need first decode the number and then compile the source code.
 
## Important

 Since prime factorization has not a fast straight forward method and based on number of instructions result of Goldel number increases, it's better to input list of #(I) \[instruction codes\] to decoder. also result of encode function is list of instruction codes.     
  
## Example

### Encode/Decode
- First run using this command:
 
      python3 coding.py
      
- Now follow instructions and get your desired output.

      1) Decode 
      2) Encode
      Select an option: (1/2) 1
      1) list of instruction codes 
      2) program code
      Select an option: (1/2) 2
      Enter Program code: 199
      Enter output file name: output.s

- output.s:

      [B1] Y <- Y
      Y <- Y
      Y <- Y + 1
 
 - Now you can use `compiler.py` to compile your program.

### Compile
Here i wrote another program which gets two input and returns sum of them.
 
 - Example2.s:
    
       [A1] IF X1 != 0 GOTO B1
       Z1 <- Z1 + 1
       IF Z1 != 0 GOTO C1
       [B1] X1 <- X1 - 1
       Y <- Y + 1
       Z1 <- Z1 + 1
       IF Z1 != 0 GOTO A1
        
       [C1] IF X2 != 0 GOTO D1
       Z2 <- Z2 + 1
       IF Z2 != 0 GOTO A2
       [D1] X2 <- X2 - 1
       Z3 <- Z3 + 1
       Z2 <- Z2 + 1
       IF Z2 != 0 GOTO C1
       
       [A2] IF Z3 != 0 GOTO B2
       Z4 <- Z4 + 1
       IF Z4 != 0 GOTO E1
       [B2] Z3 <- Z3 - 1
       Y <- Y + 1
       Z5 <- Z5 + 1
       IF Z5 != 0 GOTO A2
        
 - Command:
     
       python compiler.py Example2.s 7 8
  
 - Output:
 
       Should i show snapshot? (y/n) n
       Program output is : 15
    
 - Command:
     
       python compiler.py Example2.s 2 1
  
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
