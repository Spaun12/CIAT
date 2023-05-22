"""
Author: Michael D. Connell Jr.
Date: 2023-05-22
Week1 Chapter 1 Assignment OOP Coding Project"""

from random import randint

class Student:
    def __init__(self, name, numScores):
        """
        Using constructor method that initializes the student with a name and a number of scores,
        all of which will be 0 at startup.
        """
        self.name = name
        self.scores = [0] * numScores
    
    def getName(self):
        """Returns the student's name."""
        return self.name
    
    def getScore(self, index):
        """Returns the score at the given index."""
        return self.scores[index]
    
    def setScore(self, index, score):
        """Sets a score at the given index."""
        self.scores[index] = score
    
    def numScores(self):
        """Returns the number of scores."""
        return len(self.scores)
    
    def highestScore(self):
        """Returns the highest score."""
        return max(self.scores)
    
    def averageScore(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def __str__(self):
        """
        Returns a string representation of the student including their name and scores.
        """
        result = f"Name: {self.name}\n"
        for i, score in enumerate(self.scores, 1):
            result += f"Score {i}: {score}\n"
        return result

def main(numScores = 3):
    """Tests sorting."""
    # Create the list and put 5 students into it
    students = list()
    names = ("Mike", "Donovan", "Irina", "Maria", "Charley")
    for name in names:
        s = Student(name, numScores)
        for index in range(numScores):
            s.setScore(index, randint(70, 100))
        students.append(s)
    # Print the contents
    print("The list of students:")
    for s in students:
        print(s)
        
if __name__ == "__main__":
    main()