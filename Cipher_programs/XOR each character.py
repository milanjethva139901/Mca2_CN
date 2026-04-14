# Q1. XOR each character in "Hello World" with 1
string = "Hello World"
result = ""

for char in string:
    xor_char = chr(ord(char) ^ 1)
    result += xor_char

print("XOR Result:", result)


