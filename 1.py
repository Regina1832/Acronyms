# Acronyms
# input a phrase
phrase=str(input('input a phrase:'))
text=phrase.split()
Acronyms=''
for i in text:
    Acronyms+=str(i[0].upper())
print(Acronyms)


