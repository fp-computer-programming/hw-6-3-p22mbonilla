# Author MB 11/12/2021

word = input('give me a word: ')
word2 = input('give me another word: ')

word = list(word)
word2 = list(word2)

word.sort()
word2.sort()

if word == word2:
    print('the words are anagrams')
else:
    print('the words are not anagrams')
