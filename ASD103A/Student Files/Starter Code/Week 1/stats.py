# Write your code below:




def main():
    """Tests the functions."""
    lyst = []
    for i in range(6):
      lyst.append(int(input('Enter a Value for the list: ')))
    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))
    print("Mean:", mean(lyst))

if __name__ == "__main__":
    main()
