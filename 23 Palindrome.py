text = input("Enter a string: ").lower()
flag = True
stack = []

for i in range(len(text)//2):
    stack.append(text[i])

if len(text) % 2 == 0:
    start = len(text)//2
else:
    start = len(text)//2 + 1

for i in range(start, len(text)):
    if text[i] != stack.pop():
        flag = False
        break

if flag:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")