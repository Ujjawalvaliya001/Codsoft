# Contact Book Project

contact_book = {}

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_book[name] = {"phone_number": phone_number, "email": email, "address": address}
    print("Contact added successfully!")

def view_contact_list():
    print("Contact List:")
    for name, details in contact_book.items():
        print(f"{name}: {details['phone_number']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    for name, details in contact_book.items():
        if search_term in name or search_term in details["phone_number"]:
            print(f"Found contact: {name} - {details['phone_number']}")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contact_book:
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contact_book[name] = {"phone_number": phone_number, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def main():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
