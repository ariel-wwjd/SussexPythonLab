# Allow the user to enter an integer number. Determine if the number is prime
# or not. A number is prime if it is only divisible exactly by 1 and itself,
# e.g. 3, 7, 11 and 17. Note, 2 is the only even prime number. 1 is not
# generally regarded as prime.
# Display the answer “prime” or not prime as appropriate.

x = int(input('Enter the number to test: '))
is_prime = True  # boolean data type - note the capital 'T' in 'True
# Your solution here...

index = x - 1

while index > 1 and is_prime == True:
    print(is_prime)
    reminder = x % index
    if reminder == 0:
        is_prime = False
        break
    index -= 1

if is_prime:
    print (f'{x} is prime')
else:
    print (f'{x} is not prime')
