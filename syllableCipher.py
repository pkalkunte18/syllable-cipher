# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 11:18:14 2022

@author: saipr
"""
import string as stringg

#syllables code from syllapy (Note the install failed so I copied the code)
#source: https://medium.com/@mholtzscher/programmatically-counting-syllables-ca760435fab4
def syllables(word):
    syllable_count = 0
    vowels = 'aeiouy'
    if word[0] in vowels:
        syllable_count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllable_count += 1
    if word.endswith('e'):
        syllable_count -= 1
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
    return syllable_count

def encodeSentence(string):
    words = string.split(" ")
    letters = 'abcdefghijklmnopqrstuvwxyz'
    #count the total syllables in the string
    totalSyl = 0
    for w in words:
        totalSyl += syllables(w)
    newSent = ""
    punctuation = stringg.punctuation
    for s in words:
        s = s.lower()
        for l in s:
            if l in punctuation:
                newSent += l 
            else:
                oldIndex = letters.index(l)
                newIndex = (oldIndex + totalSyl) % 25
                newLetter = letters[newIndex]
                newSent += newLetter
        newSent += " "
    return (newSent, totalSyl)

def decodeSentence(string, totalSyl):
    words = string.split(" ")
    letters = 'abcdefghijklmnopqrstuvwxyz'
    newSent = ""
    punctuation = stringg.punctuation
    for s in words:
        s = s.lower()
        for l in s:
            if l in punctuation:
                newSent += l 
            else:
                oldIndex = letters.index(l)
                newIndex = (oldIndex - totalSyl) % 25
                newLetter = letters[newIndex]
                newSent += newLetter
        newSent += " "
    return newSent

def encodePoem(poem):
    sents = poem.split("\n")
    encoding  = [encodeSentence(s) for s in sents]
    newSents = [i[0] for i in encoding]
    sylList = [i[1] for i in encoding]
    newPoem = ""
    for n in newSents:
        add = n + "..."
        newPoem = newPoem + add
    return (newPoem, sylList)

def decodeParagraph(poem, sylList):
    sents = poem.split("\n")
    newSents = [decodeSentence(sents[i], sylList[i]) for i in range(0, len(sents))]
    newPoem = ""
    for n in newSents:
        newPoem =+ (n + "\n")
    return newPoem
    
print(encodePoem("Orange scent soaks skin\nLike the warmth of dear mother\nLove in little things"))