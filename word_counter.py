sentence = input("Enter your desired sentence: ") # User sentence input

list_of_words = list(sentence) # Converting the words of sentence to list of characters

count = 0 # Setting the word counter variable to 0

# Iterating the character in list and count increment
for i in list_of_words:
    if (i == " "):
        count += 1
    else:
        continue

print("Number of words in the sentence are: ",count+1)