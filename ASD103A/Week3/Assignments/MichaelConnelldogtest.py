"""Michael Connell Week3 Assignment - Inheritance 2023-06-09"""

from dogs import Poodle, GoldenRetriever, Samoyed

poodle = Poodle("Fifi")
golden_retriever = GoldenRetriever("Goldie")
samoyed = Samoyed("Sammy")

def test_speak(dog):
    dog.speak()

def test_likes_walks(dog):
    print(f"Does the {dog.__class__.__name__} named {dog.name} like walks? {'Yes' if dog.likes_walks() else 'No'}")

def test_name(dog):
    print(f"The dog's name is {dog.name}")

for dog in [poodle, golden_retriever, samoyed]:
    test_speak(dog)
    test_likes_walks(dog)
    test_name(dog)
    print("-------------------------")

