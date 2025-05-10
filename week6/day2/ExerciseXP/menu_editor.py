from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n--- Menu Editor ---")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("X - Exit")
        choice = input("Choose an option: ").strip().upper()

        if choice == "V":
            view_item()
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "X":
            print("\nExiting and showing final menu:")
            show_restaurant_menu()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def add_item_to_menu():
    name = input("Enter item name: ").strip()
    try:
        price = int(input("Enter item price: "))
        item = MenuItem(name, price)
        item.save()
        print("Item added successfully.")
    except Exception as e:
        print(f"Error adding item: {e}")

def remove_item_from_menu():
    name = input("Enter the name of the item to delete: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        try:
            item.delete()
            print("Item deleted successfully.")
        except Exception as e:
            print(f"Error deleting item: {e}")
    else:
        print("Item not found.")

def update_item_from_menu():
    current_name = input("Enter current item name: ").strip()
    item = MenuManager.get_by_name(current_name)
    if item:
        new_name = input("Enter new item name: ").strip()
        try:
            new_price = int(input("Enter new item price: "))
            item.update(new_name, new_price)
            print("Item updated successfully.")
        except Exception as e:
            print(f"Error updating item: {e}")
    else:
        print("Item not found.")

def view_item():
    name = input("Enter item name to view: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        print(f"{item.item_name} - ${item.item_price}")
    else:
        print("Item not found.")

def show_restaurant_menu():
    print("\n--- Restaurant Menu ---")
    items = MenuManager.all_items()
    if not items:
        print("Menu is empty.")
    for item in items:
        print(f"{item.item_name} - ${item.item_price}")

if __name__ == "__main__":
    show_user_menu()