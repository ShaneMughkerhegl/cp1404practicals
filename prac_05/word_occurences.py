"""
Word Occurrences Counter
Estimate: 20 minutes
Actual:   25 minutes
"""

def main():
    text = input("Text: ")
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    longest_word = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:{longest_word}} : {word_counts[word]}")


if __name__ == "__main__":
    main()