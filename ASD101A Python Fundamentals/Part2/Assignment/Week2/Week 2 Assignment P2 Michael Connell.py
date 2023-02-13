#Week 2 Assignment P2 Michael Connell
# Define the two lists
lst1 = ['salamander','triceratops','cheetah','puma']
lst2 = ['banana','banana','banana','banana','orange you glad I didn\'t say banana?']
# Determine the length of each list
length_lst1 = len(lst1)
length_lst2 = len(lst2)
# Compare the lengths of the two lists to determine which one is shorter
if length_lst1 < length_lst2:
    shorter_list = lst1
else:
    shorter_list = lst2
# Print the last element from the shorter list
# The -1 index is the last element from the shorter
# list so you don't have to know the length of the list
# Kind of a cool trick I learned on the discord server I follow
print("The last element from the shorter list is: ", shorter_list[-1]) 