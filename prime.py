# Program to find prime numbers in a given range

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to square root
        if num % i == 0:
            return False
    return True

# Take input range from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")

# Loop through range and print prime numbers
for number in range(start, end + 1):
    if is_prime(number):
        print(number, end=" ")
