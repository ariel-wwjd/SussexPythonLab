# Generate a sequence of integer numbers in the pattern 0, 2, 4, ..., up to 20
# inclusive and display the numbers on the screen.

x = 0
# Your solution here...
while x <= 20:
    print(x)
    x += 2


# Allow the user to enter a string, and then print out each letter
# in the string one at a time on a separate line.

string = input('Enter some text: ')
# Your solution here...
for c in string:
    print(c)


# As above, but print out the letters in the string in reverse order.

string = input('Enter some text: ')
# Your solution here...
index = -1
for c in string:
    print(string[index])
    index -= 1


# Starting with the initial value 0 and 1, generate a Fibonacci sequence.
# Each element in a Fibonacci sequence is the sum of the two previous
# elements e.g. 0, 1, 1, 2, 3, 5, 8, ...
# Allow the user to specify how many elements should be generated.

x = int(input('How many fibonacci elements? '))
# Your solution here...
fibonacci = [0, 1]
print(fibonacci[0])
print(fibonacci[1])
index = len(fibonacci)
while index < x:
    new_fibonacci = fibonacci[index - 1] + fibonacci[index - 2]
    fibonacci.append(new_fibonacci)
    print(new_fibonacci)
    index += 1

# print (fibonacci)