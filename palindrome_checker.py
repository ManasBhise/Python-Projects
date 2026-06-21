# Input string
string = input("Enter a string: ")


list_of_string = list(string) # Converted the string to a list
rev_list_of_string = [] # Created an empty list

# Traversing a loop through the list and appending the items to empty list
for i in (list_of_string[::-1]):
    rev_list_of_string.append(i)

# Condition to check if new list is same as original list
if (rev_list_of_string == list_of_string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")