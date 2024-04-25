def add_entry(name, phone, phonebook_file):
    with open(phonebook_file, 'a') as file:
        file.write(f"{name},{phone}\n")
    print("Entry added successfully!")

def search_entry(name, phonebook_file):
    found = False
    with open(phonebook_file, 'r') as file:
        for line in file:
            entry_name, entry_phone = line.strip().split(',')
            if name.lower() == entry_name.lower():
                print(f"Name: {entry_name}, Phone: {entry_phone}")
                found = True
    if not found:
        print("Entry not found.")

def display_phonebook(phonebook_file):
    with open(phonebook_file, 'r') as file:
        for line in file:
            name, phone = line.strip().split(',')
            print(f"Name: {name}, Phone: {phone}")

def main():
    phonebook_file = "phonebook.txt"

    while True:
        print("\n1. Add new entry")
        print("2. Search for a name")
        print("3. Display entire phonebook")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_entry(name, phone, phonebook_file)
        elif choice == '2':
            name = input("Enter name to search: ")
            search_entry(name, phonebook_file)
        elif choice == '3':
            display_phonebook(phonebook_file)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
