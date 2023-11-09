#example of for loop with string 
#count words in string
# sentence = "the quick brown fox jumps over the lazy dog"
sentence = input("enter one sentence")
words = 1
for letter in sentence:
    if letter == ' ':
        words = words + 1
print("word count =",words)