import random

def randomize_sentence(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    # Shuffle the list of words
    random.shuffle(words)
    # Join the list of words back into a sentence
    return ' '.join(words)

# Get a sentence from the user
sentence = input("Enter a sentence: ")
# Call the randomize_sentence function and print the result
print(randomize_sentence(sentence))
