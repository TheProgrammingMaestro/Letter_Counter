word = input("Enter a word: ")
letter = input("Enter a letter: ")
def letter_counter(word, letter):
    count = 0
    for let in word:
        if let == letter:
            count += 1
    return count
print(letter_counter(word, letter))

