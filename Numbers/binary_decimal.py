"""
Binary to Decimal and Back Converter
Develop a converter to convert a decimal number to binary
or a binary number to its decimal equivalent.
"""
import math
def binary_to_decimal(binary):
    """
    Converts a binary number into a decimal number.
    """
    decimal = 0
    index = 0
    for x in range(len(binary)):
        if int(binary[x]) == 1:
            decimal += math.pow(2,x)
    return decimal

def decimal_to_binary(decimal):
    """
    Converts a decimal number into a binary number.
    """
    binary = ""
    remainders = []
    while decimal > 0:
        remainders.append(str(decimal % 2))
        decimal /= 2
    remainders.reverse()
    binary = "".join(remainders)
    return binary

print """
1. Binary to Decimal
2. Decimal to Binary\n
"""

choice = input("Make a choice: ")

if choice == 1:
    binary = input("Binary to convert: ")
    print "The binary number %d in decimal is %d" % (binary, binary_to_decimal(str(binary)))
elif choice == 2:
    decimal = input("Decimal to convert: ")
    print "The decimal number %d in binary is %s" % (decimal, decimal_to_binary(decimal))
else:
    print "Invalid choice"
