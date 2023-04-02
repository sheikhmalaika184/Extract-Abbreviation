import docx
import re

# Load the document
doc = docx.Document('test1.docx')

# Extract the text
full_text = ''
for paragraph in doc.paragraphs:
    full_text += paragraph.text
full_text = full_text.replace("."," ")
full_text = full_text.replace(","," ")
full_text = full_text.replace("-"," ")
full_text = full_text.replace("("," ")
full_text = full_text.replace(")"," ")
abbreviations = re.findall(r'\b[A-Z]{2,}\w*\b', full_text)
full_text = full_text.split(" ")
words_list = []
for word in full_text:
    for l in range(0,len(word)):
        if(word[0].isupper() or word[l].islower() or word[0].isdigit()):
            continue
        elif(word[l].isupper()):
            words_list.append(word)
            break
abbreviations.extend(words_list)
abbreviations = list(set(abbreviations))
abbreviations.sort(key=str.lower)
for word in abbreviations:
    if (len(set(word)) == 1 or len(word) > 9):
        abbreviations.remove(word)
print(abbreviations)
# writing output in file 
file = open("output.txt","w")
for word in abbreviations:
    file.write(word + "\n")