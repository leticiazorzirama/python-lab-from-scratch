# Linguistic Signature-Based Plagiarism Detector (COH-PIAH Virus Simulation)

# Main idea:
# Each text has a "signature" – a set of 6 linguistic traits (like avg word length, etc.).
# We compare the signature of each student's text to a known "infected" signature.
# The closest match is most likely "infected".

# Key Functions:
# - split_sentences / split_phrases / split_words: break text into parts
# - count_different_words: count unique words (case-insensitive)
# - count_unique_words: count words that appear only once
# - calculate_signature: compute the 6 linguistic traits of a text
# - compare_signatures: calculate similarity score between two signatures
# - evaluate_texts: find which of the input texts is most similar to the infected signature

# Execution flow (main):
# 1. User inputs the infected signature.
# 2. User inputs multiple texts.
# 3. For each text:
#    - Calculate its signature.
#    - Compare to the infected signature.
# 4. The text with the lowest similarity score is flagged as "infected".

import re

def split_sentences(text):
    """Splits a text into a list of sentences."""
    sentences = re.split(r'[.!?]+', text)
    if sentences and sentences[-1] == '':
        sentences.pop()
    return sentences

def split_phrases(sentence):
    """Splits a sentence into a list of phrases."""
    return re.split(r'[,:;]+', sentence)

def split_words(phrase):
    """Splits a phrase into a list of words."""
    return phrase.split()

def count_different_words(word_list):
    """Returns the number of different words used in a list of words."""
    freq = {}
    for word in word_list:
        word_lower = word.lower()
        freq[word_lower] = freq.get(word_lower, 0) + 1
    return len(freq)

def count_unique_words(word_list):
    """Returns the number of words that appear only once in a list of words."""
    freq = {}
    unique = 0
    for word in word_list:
        word_lower = word.lower()
        if word_lower in freq:
            if freq[word_lower] == 1:
                unique -= 1
            freq[word_lower] += 1
        else:
            freq[word_lower] = 1
            unique += 1
    return unique

def calculate_signature(text):
    """Calculates the linguistic signature of a text.
    
    Returns a list with the six linguistic traits.
    """
    word_lengths = []
    all_words = []
    phrase_lengths = []
    all_phrases = []
    sentence_lengths = []

    sentences = split_sentences(text)

    for sentence in sentences:
        phrases = split_phrases(sentence)
        all_phrases.extend(phrases)

    for phrase in all_phrases:
        words = split_words(phrase)
        all_words.extend(words)

    for word in all_words:
        word_lengths.append(len(word))

    for phrase in all_phrases:
        phrase_lengths.append(len(phrase))

    for sentence in sentences:
        sentence_lengths.append(len(sentence))

    try:
        wal = sum(word_lengths) / len(word_lengths)
        ttr = count_different_words(all_words) / len(all_words)
        hlr = count_unique_words(all_words) / len(all_words)
        sal = sum(sentence_lengths) / len(sentences)
        sac = len(all_phrases) / len(sentences)
        pal = sum(phrase_lengths) / len(all_phrases)
    except ZeroDivisionError:
        return [0, 0, 0, 0, 0, 0]

    return [wal, ttr, hlr, sal, sac, pal]

def read_signature():
    """Reads and returns the infected signature as a list of linguistic traits."""
    print("Welcome to the automatic COH-PIAH detector.")
    print("Please enter the typical signature of an infected student [default signatures are suggested]:")

    try:
        wal = float(input("Enter average word length[4.51]: "))
        ttr = float(input("Enter Type-Token ratio[0.693]: "))
        hlr = float(input("Enter Hapax Legomena ratio[0.55]: "))
        sal = float(input("Enter average sentence length[70.82]: "))
        sac = float(input("Enter average sentence complexity[1.82]: "))
        pal = float(input("Enter average phrase length[38.5]: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return read_signature()

    return [wal, ttr, hlr, sal, sac, pal]

def read_texts():
    """Reads and returns a list of texts entered by the user."""
    i = 1
    texts = []
    while True:
        text = input(f"Enter text {i} (press enter to finish): ")
        if not text:
            break
        texts.append(text)
        i += 1
    return texts

def compare_signatures(sig_a, sig_b):
    """Calculates and returns the similarity degree between two linguistic signatures."""
    differences = [abs(sig_a[i] - sig_b[i]) for i in range(6)]
    return sum(differences) / 6

def evaluate_texts(texts, infected_signature):
    """Evaluates and returns the index of the text most similar to the infected signature."""
    similarity_scores = []

    for text in texts:
        signature = calculate_signature(text)
        similarity = compare_signatures(signature, infected_signature)
        similarity_scores.append(similarity)

    most_similar_index = similarity_scores.index(min(similarity_scores))
    return most_similar_index + 1

def restart():
    """
    Asks the user if they want to restart the detector.
    Returns True if yes, False otherwise.
    """
    answer = input("Do you want to restart the detector? (y/n): ").strip().lower()
    if answer == 'y':
        return True
    elif answer == 'n':
        print("Thanks! Goodbye.")
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return restart()

def main():
    try:
        infected_signature = read_signature()
        texts = read_texts()
        if not texts:
            print("No texts were entered.")
            return
        most_similar = evaluate_texts(texts, infected_signature)
        print(f"\nText {most_similar} is most likely infected with COH-PIAH.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    if restart():
        return main()

if __name__ == "__main__":
    main()
