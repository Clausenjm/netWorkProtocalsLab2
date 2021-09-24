"""
- NOTE: REPLACE 'N' Below with your section, year, and lab number
- CS2911 - 0NN
- Fall 202N
- Lab N
- Names:
  - Josiah Clausen
  - Elise
"The Machine" implementation of parsing and executing a program.

The application reads a file name from the user and executes the contents of the file or sends an error if the file format is not valid.

The file format is describe in "The Machine" exercise and the lab description.


Introduction: (Describe the lab in your own words)




Summary: (Summarize your experience with the lab, what you learned, what you liked, what you disliked, and any suggestions you have for improvement)




"""

# import the readfile modules to read bytes from a file
import codecs

import readfile
operation_amount = 0
hex_array =[]
def main():
    """
    - Input and execute a file formatted for "The Machine"
    """
    # Get chosen file from the user.
    program_file = input('Enter the name of the program to execute: ')
    # Execute the chosen file.
    execute(program_file)


def execute(program_file):

    """
    - Execute a program file formatted for "The Machine"
    :param str program_file: name of the file to execute
    """
    readfile.set_file(program_file)
    read_file()


    #hex_array.append(readfile.read_byte())

    """
    - created by: Josiah Clausen
    - Reads the file and stores its bytes in array
    """
def read_file():

    if verify_magic_number():
           operation_amount = get_operation_amount()
           print(operation_amount)
    else: print("file does not have required magic number")

"""
- created by: Josiah Clausen
 - Reads the file and stores its bytes in array
"""
def verify_magic_number():
    index = 0
    magic_number = [b'\x31', b'\x41', b'\xfa', b'\xce']
    while index < 4:
        b = readfile.read_byte()
        if b != magic_number[index]:
            return False
        index = index + 1

    return True

def get_operation_amount():
    first_byte = int.from_bytes(readfile.read_byte() , 'big')
    second_byte = int.from_bytes(readfile.read_byte() , 'big')
    amount_of_operators = first_byte + second_byte
    return amount_of_operators
# Invoke the main method to run the program.
main()


