text = input("Enter a sentence : ")
text = text.split()
bigwordlength = 0
for wrd in text: 
    wordlength = len(wrd)
    if wordlength>bigwordlength:
        bigwordlength = wordlength

print("\n largest word = ")
for wrd in text:
    wordlength = len(wrd)
    if wordlength==bigwordlength:
        print(wrd)        