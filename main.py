num = 121

num_length = len(str(num))

def palindrome(num):
    original_digits = [int(digit) for digit in str(num)]
    reverse_digits = []

    for i in original_digits:
        reverse_digits.insert(0,i)

    #reverse_digits = [int(digit) for digit in str(num)]
    #score = 0
    if original_digits == reverse_digits:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

    print(original_digits)
    print(reverse_digits)

palindrome(num)
