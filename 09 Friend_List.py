friends = {}

n = int(input("Enter the number of friends: "))

for _ in range(n):
    name = input("\nEnter name: ")
    phone = int(input(f"Enter {name}'s phone number: "))
    friends[name] = phone
   

def display():
    if(not friends):
        print("\nNo friends in the list")
        return
    print("\nFriends List: ")
    for i, (x, y) in enumerate(friends.items(), start=1):
        print(f"{i}. {x}: {y}")

def add_friend():
    while True:
        name = input("\nEnter name of the friend you want to add: ")
        phone = int(input(f"Enter {name}'s phone number: "))
        if name in friends:
            print("Friend already exists")
        else:
            friends[name] = phone
            break

def delete_friend():
    while True:
        name = input("\nEnter name of the friend you want to delete: ")
        if name in friends:
            del friends[name]
            break
        else:
            print("Friend does not exists please enter a valid friend")

def modify_phone(name):
    if name in friends:
        friends[name] = int(input(f"Enter the new number of {name} :"))
    else:
        print("Friend does not exists.")

def isPresent(name):
    if name in friends:
        print(f"Yes {name} is present.")
    else:
        print(f"No {name} is not present.")

def sort_and_display():
    global friends
    friends_sorted = dict(sorted(friends.items()))
    friends = friends_sorted
    display()


display()
add_friend()
display()
delete_friend()

name = input("Enter the the name whose number you want to modify: ")
modify_phone(name)
name = input("Enter the name you want to check he exists or not: ")
isPresent(name)

sort_and_display()