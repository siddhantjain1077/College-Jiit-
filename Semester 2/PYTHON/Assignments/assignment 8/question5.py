def copy_file_content():
    while True:
        try:
           
            source_file = input("Enter the name of the source file: ")
            destination_file = input("Enter the name of the destination file: ")
            
           
            with open(source_file, 'r') as src:
                content = src.read()
            
            
            with open(destination_file, 'w') as dest:
                
                dest.write(content)
            
            print(f"Content copied successfully from '{source_file}' to '{destination_file}'")
            break  
        
        except FileNotFoundError:
            print(f"Error: '{source_file}' not found. Please enter a valid filename.")

if __name__ == "__main__":
    copy_file_content()
