with open("employee.txt") as f:
    lines = f.readlines()

id = input("Enter ID: ")
for i, line in enumerate(lines):
    if(id == line.split(',')[0]):
        for x in line.split(","):
            print(x, end=" ")
        break

old = input("\nEnter the text for edit: ")
new = input("Enter the text to replace: ")

if(line.find(old) != -1):
    lines[i] = line.replace(old, new)
else:
    print("not founded")

with open("employee.txt", "w") as f:
    f.writelines(lines)