def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    if not line.startswith('#'):
                        destination.write(line)
        print("File copied successfully!")
    except FileNotFoundError:
        print("Error: One of the files does not exist.")

source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

copy_file(source_file, destination_file)
