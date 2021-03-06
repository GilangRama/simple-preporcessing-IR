import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def readTxt(fileName):
    textFile = open(fileName, "r")
    lines = textFile.readlines()
    lines2 = []
    for i in lines:
        i = i.replace('\n', '')
        lines2.append(i)
    return lines2

# Input Dokumen
stringText = input("Input text : ")

# Case Folding
lower_document = stringText.lower()
print("Lowcase Document : ", lower_document)

dltNumber = ''.join([i for i in lower_document if not i.isdigit()])
print("Document with no number : ", dltNumber)

punctuation = set(string.punctuation)
noPunctuation = ''.join(ch for ch in dltNumber if ch not in punctuation)
print("Document with no punctuation : ", noPunctuation)

noWhitespace = noPunctuation.strip();
print("Dokumen with no whitespace: ", noWhitespace)

#Tokenizing
word = noWhitespace.split()
print("Split: ", word)
print(len(word), " word")

removeMultipleWord = list(set(word))
print("Tokenizing: ", removeMultipleWord)
print(len(removeMultipleWord), " word")

#Filtering / Stop Removal
stopRemoval = readTxt('StopWord.txt')
withoutStopword = [x for x in removeMultipleWord if x not in stopRemoval]
print("Filtering Document : ",withoutStopword)

factory = StemmerFactory()
stemmer = factory.create_stemmer()

withoutStopword = ' '.join(withoutStopword) #Convert list to string

hasil = stemmer.stem(withoutStopword)
print("Result: ", hasil)

