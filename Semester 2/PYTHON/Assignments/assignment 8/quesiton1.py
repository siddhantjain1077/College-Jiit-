def count_word_occurrences(file_path):
    word_count = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip().lower().strip('.,!?')
                if word:
                    word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

def main():
    file_path = input("Enter the path of the text file: ")
    word_count = count_word_occurrences(file_path)
    
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
