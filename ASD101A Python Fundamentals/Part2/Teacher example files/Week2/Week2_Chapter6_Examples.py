## Example of reading all lines into a variable from the file handle (file object)
#myFile = open("AboutText.txt", 'r')
#fileContent = myFile.read()   # reads all lines without the end-of-line character
#print(fileContent)
#myFile.close()

## Example of reading a file that is in a different directory using readlines() method
#myFile = open('rC:\Users\lrey\Documents\humpty.txt','r')
#fileContent = myFile.readlines() # reads all lines and returns a list of each line as an element
#print(fileContent[0].rstrip())
#myFile.close()

## Example of reading a file and iterating through each line
#myFile = open("AboutText.txt")
#for line in myFile:
#    print(line)
#myFile.close()

## Example of reading a file and iterating through each line and printing character by character
#myFile = open("AboutText.txt")
#for line in myFile:
#    for chtr in line:
#        print(chtr)
#myFile.close()


## If a list is required then use readlines()
## If the entire text is needed without newline charaters use read()
## If line by line processing is needed use the for loop

# ----------------------------------------------------------------
## Example of writing to a text file
#myFile = open("output.txt",'w')  # 'w' overwrite the file each time the code is run
#myFile.write("This is my second line.")
#myFile.close()   # You must close the file before seeing the output in your text file

## Example of appending to a text file
myFile = open("output.txt",'a')  # 'a' appends to the file each time the code is run
myFile.write("This is my second line.\n")
myFile.close()   # You must close the file before seeing the output in your text file

####### ----------------- Exception Handling --------------------
## Example of exception handling 
try:
    a = 1/0
except:
    print("Divide by zero error")
else:
    print("Else, runs only if the exception is not thrown")
finally:
    print("Finally, will run no matter what")

## Example of exception handling using raise Exception() to create a conditional error
num = int(input("Please enter a positive number: "))
try:
    if num < 0:
        raise Exception("Please only enter positive numbers!")
except:
    print("Negative number exception")

## Example of exception handling for files that cannot be accessed.
filename = input("Please enter the file name you want to open: ")
try:
    myFile = open(filename)
except:
    print("The file you chose does not exist.")
else:
    print("You file is open now")
myFile.close()