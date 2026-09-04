print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert your text: ")
char = input("input your search: ")
for char in text:
    if char == char:
        count += 1
print(f"{count} letters {char} found in '{text}'")


