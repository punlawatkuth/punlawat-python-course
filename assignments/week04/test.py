# receive texts or name from user
# count every letters in that sentence or text
#use only for-loop

#examples
# What is your name? : blablabla
# Your text has 4 vovwels.


name = str(input("please input your name here:  "))
vowels = "aeiou"
count = 0
for char in name:
    if char.lower() in vowels:
        count += 1
print(f"your text has {count} vowels")

    
# ver 2
name = str(input("please input your name here:  "))
vowels = ['a','e','i','o','u']
count = 0
for char in name:
    if char.lower() in vowels:
        count += 1
print(f"your text has {count} vowels")

# ver3


