mainSentence = input("Please enter the sentence you want to analyze: ")
length = len(mainSentence)
res = len(mainSentence.split())
print("Word Count: "+str(res))
print("Total characters: " + str(length))