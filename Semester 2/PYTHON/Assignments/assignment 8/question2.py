def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for _ in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

filename = input("Enter the filename: ")
lines = count_lines(filename)
if lines is not None:
    print(f"The file '{filename}' has {lines} lines.")
