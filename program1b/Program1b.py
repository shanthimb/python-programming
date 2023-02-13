# Develop a Python program to check whether a given number is palindrome or not and
# also count the number of occurrences of each digit in the input number.
if __name__ == "__main__":
    n = int(input("Enter number:"))
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev:
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")
