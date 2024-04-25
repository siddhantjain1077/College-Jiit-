def read_text_file_content():
    while True:
        try:
            filename = input("Enter the name of a text file: ")
            with open(filename, 'r') as file:
                content = file.read()
                print("File content:")
                print(content)
                break
        
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please enter a valid filename.")

if __name__ == "__main__":
    read_text_file_content()
