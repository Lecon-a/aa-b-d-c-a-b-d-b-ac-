"""
Author: Sunday P. Afolabi
Lecturer: Dr. Azeez N.
Course Title: Compiler Construction
Course Code:
University: University of Lagos
Semester: Second

RE: aa(b|d)c*(a|b|d)*b+(ac)

"""

from dfa_trans_table import isVariableIn_abcd, decide

input_string = input("Enter: ")

if isVariableIn_abcd(input_string):
    print(f"The variable '{isVariableIn_abcd(input_string)}' is not recognized")
    exit()

status, path = decide(input_string=input_string)

if status:
    print(f"{input_string} follows the path {' -> '.join(path)} is accepted!")
else: print(f"{input_string} is rejected!")
    

    

