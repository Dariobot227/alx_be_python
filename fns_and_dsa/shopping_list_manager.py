def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Adding a new item to the shopping list
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.\n")

        elif choice == '2':
            # Remove item from shopping list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.\n")
            else:
                print(f"'{item}' not found in the shopping list.\n")

        elif choice == '3':
            # View list
            if not shopping_list:
                print("Your shopping list is currently empty.\n")
            else:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
                print()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
