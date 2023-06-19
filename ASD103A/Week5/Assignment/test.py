# Student: Michael Connell Date: 2023-06-19

# Import the functions from your files
from ReverseWordToDo import reverse_word

def test_reverse_word():
    """
    This function tests the reverse_word function with some funny phrases.
    """
    # List of test phrases
    test_phrases = [
        "Python is fun",
        "I love coding",
        "Stacks are great",
        "Last week of class",
        "No more homework"
    ]

    # Iterate over each phrase
    for phrase in test_phrases:
        # Reverse each word in the phrase
        reversed_words = [reverse_word(word) for word in phrase.split()]
        # Join the reversed words back into a phrase
        reversed_phrase = ' '.join(reversed_words)
        print(f"Original phrase: {phrase}")
        print(f"Reversed phrase: {reversed_phrase}")
        print("-"*30)

    print("And remember folks, always keep your code clean, just like how you would keep your room (not like my room).")
    print("Stay curious, keep learning, and don't forget to reverse your words sometimes for fun!")
    print("Have a great year and remember, you're all amazing!")

test_reverse_word()
