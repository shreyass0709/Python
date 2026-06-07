a = "hello world"

b = """This is a multi-line string.
It can span multiple lines. It is enclosed in triple quotes.
This is the end of the multi-line string."""
print(a)
print(b)

print(a[0])  # Accessing the first character of the string
print(a[1:5])  # Slicing the string from index 1 to 4
print(a.upper())  # Converting the string to uppercase

print(a)

for x in "helxo":
    print(x)

print(len(a))  # Getting the length of the string

print("world" in a)  # Checking if "world" is in the string
print("python" in a)  # Checking if "python" is in the strings

if "world" in a:
    print("Yes, 'world' is in the string.")

print("hello" not in a)  # Checking if "hello" is not in the string