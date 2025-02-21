def palindrome(word):
    word = str(word)
    if word == word[::-1]:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is NOT a palindrome.")