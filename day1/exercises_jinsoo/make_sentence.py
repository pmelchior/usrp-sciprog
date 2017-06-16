sentence = ""
while True:
    word = input("Enter a word (. ! or ? to end): ")
    if (word=="!" or word=="?" or word=="."):
        sentence = sentence.rstrip()
        sentence = sentence + word
        print(sentence)
        exit()
    else:
        sentence += word + " "
