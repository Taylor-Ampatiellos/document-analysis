from docx import Document

def getText(filename):
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        for word in para.text.lower().split():
            fullText.append(word)
    return fullText

# getText('example.docx')

#file = open('testDoc.txt', 'r')
#book = file.read()

sentence = getText('testDocx.docx')
ls = []  
for i in sentence:

    word_count = sentence.count(i)  # Pythons count function, count()
    ls.append((i,word_count))       


dict_ = dict(ls)

print (dict_)
