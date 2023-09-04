# MIKHAILA JASMIN PANTOJA - F2_PYTHONEXERCISE
# 1. Write a program that asks for a float number as Celsius and converts this number into its Fahrenheit equivalent in to two decimal places.

c = float(input("Enter desired Celsius to convert into Fahrenheit: "))

f = (c * 9/5) + 32

print(f"{c} degree Celsius is equivalent to {f:.2f} in degree Fahrenheit")
print("\n")

# 2. Write a program that take three integers as input and find the maximum among them.
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

temp = num1
if num2 > temp:
    temp = num2
if num3 > temp:
    temp = num3

print(f"The biggest number among the three numbers provided is {temp}.")
print("\n")

# 3. Write a program that counts the number of digits in a given integer. Display also the smallest and highest integer.
#Sample Output:
#Please enter a number: 12345
#Number of digits in the given number is: 5
#Smallest number is: 1
#Highest number is: 5

num = int(input("Please enter a number: "))

count = 0
min = None
max = None

if num == 0:
    count = 1
    min = 0
    max = 0

while num > 0:
    digits = num % 10
    count += 1

    if min is None or digits < min:
        min = digits

    if max is None or digits > max:
        max = digits

    num //= 10

print(f"Number of digits in the given number is: {count}")
print(f"Smallest number is: {min}")
print(f"Highest number is: {max}")
print("\n")

# 4. Write a program that calculates the sum of all numbers from 1 to a given number. Print the resulting sum after.
num = int(input("Enter a number: "))

sum = 0

for i in range(1, num + 1):
    sum += i

print(f"The sum of all numbers from 1 to {num} is: {sum}")
print("\n")

# 5. Write the following functions
def decToBinary(dec):
    if dec == 0:
        return '0'

    binary = ''
    while dec > 0:
        remainder = dec % 2
        binary = str(remainder) + binary
        dec //= 2

    return binary

def binaryToN(binary, base):
    if base not in (2, 8, 16):
        return "Invalid base"

    result = 0
    binary_length = len(binary)
    power = 0
    i = binary_length - 1
    while i >= 0:
        digit = int(binary[i])
        result += digit * (base ** power)
        power += 1
        i -= 1

    return result

def decToOctal(dec):
    if dec == 0:
        return '0'

    octal = ''
    while dec > 0:
        remainder = dec % 8
        octal = str(remainder) + octal
        dec //= 8

    return octal

def decToHex(dec):
    if dec == 0:
        return '0'

    hex_chars = '0123456789ABCDEF'
    hex_value = ''

    while dec > 0:
        remainder = dec % 16
        hex_value = hex_chars[remainder] + hex_value
        dec //= 16

    return hex_value

def reverseString(string):
    reversed_str = ''
    i = len(string) - 1
    while i >= 0:
        reversed_str += string[i]
        i -= 1
    return reversed_str

def main():
    dec_num = 23
    print(f"Decimal: {dec_num}")
    bin_val = decToBinary(dec_num)
    print(f"Binary: {bin_val}")
    oct_val = decToOctal(dec_num)
    print(f"Octal: {oct_val}")
    hex_val = decToHex(dec_num)
    print(f"Hexadecimal: {hex_val}")
    con_dec = binaryToN(reverseString(bin_val), 2)
    print(f"Converted Binary to Decimal: {con_dec}")


if _name_ == "_main_":
    main()