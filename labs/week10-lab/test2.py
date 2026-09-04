# 2 test password strength
# need more than 8l, has char '@', has num
password = input("Set your password: ")
length = len(password)
words = password.split('@')
left = words[0].isalnum()
right = words[1].isalnum()

if length >= 8 and len(words) == 2 and left and right:
    print("your password is strong!")
else:
    print("your password is weak")