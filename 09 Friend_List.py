dic = {}

def display():
    if(not dic):
        print("\nNo friends in the list")
        return

    print("\nFriends List: ")
    for i, (x, y) in enumerate(dic.items(), start=1):
        print(f"{i}. {x}: {y}")

n = int(input("Enter the number of friends: "))

for _ in range(n):
    key = input("\nEnter name: ")
    value = input(f"Enter {key.split(' ')[0]}'s phone number: ")
    dic[key] = value

while True:
    print("\n--- Friend List Menu ---")
    print("1. Display friend list")
    print("2. Update friend list (add more)")
    print("3. Delete a friend")
    print("4. Update phone number")
    print("5. Search a friend")
    print("6. Display sorted friend list")
    print("0. Exit\n")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case "0":
            print("\nThankyou!")
            break
        case "1":
            display()
        case "2":
            n = int(input("How many friends you want to add: "))
            for _ in range(n):
                key = input("\nEnter name: ")
                value = input(f"Enter {key.split(' ')[0]}'s phone number: ")
                dic[key] = value
        case "3":
            key = input("\nEnter the name of the friend you want to delete: ")
            del dic[key]
        case "4":
            key = input("\nEnter the name of the friend: ")
            dic[key] = input(f"Enter {key.split(' ')[0]}'s phone number: ")
        case "5":
            key = input("\nEnter the name of the friend you want to search: ")
            if(key in dic):
                print(f"{key}: {dic[key]}")
            else:
                print("Friend is not present in the list")
        case "6":
            print("\nSorted friend list: ")
            for i, (x, y) in enumerate(sorted(dic.items()), start=1):
                print(f"{i}. {x}: {y}")
        case default:
            print("\nInvalid choice! Please choose again.")