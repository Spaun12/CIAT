from arraybag import ArrayBag

def main():
    bag = ArrayBag()  # create a new empty bag
    for i in range(15):  # add more items than the initial capacity
        bag.add(i)
        print("Added", i, "to the bag. Bag size is now", len(bag))

    print("Here's what's in the bag:")
    for item in bag:
        print(item)

if __name__ == "__main__":
    main()
