# Write here the code challenge solution

from collections import Counter

def firstRepeatedWord(sentence):
    ''' this method responsible to add the sentence to created list and split it then count it using dictionary to find 
    the repetion for each word in thr given sentence'''
    lis = list(sentence.split(" "))
    frequency = Counter(lis)

    for i in lis:
        if(frequency[i]>1):
            return i 
        else: 
            return "No Repetition"

if __name__ == "__main__":
    sentence = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    sentence2 = "I am learning programming at ASAC."
    sentence3 = ""
    print(firstRepeatedWord(sentence))
    print(firstRepeatedWord(sentence2))
    print(firstRepeatedWord(sentence3))
