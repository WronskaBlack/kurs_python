"""
1. wylosuj słowo z słownika
2. zrób z niego anagram
3. użytkownik zgaduje
4. dobrze - komunikat i koniec
5. żle zagduje dalej
"""
import random

dictionery = ["brown", "white", "book", "good"]

word = random.choice(dictionery)
word_shuffle = list(word)   # zamiana słowa na listę
random.shuffle(word_shuffle)     # wymieszanie listy
word_shuffle = "".join(word_shuffle)    #zamiana listy na słowo

while True:
    print(f"Zgadnij jakiego słowa anagramem jest {word_shuffle}? ")
    guess = input()
    if guess == word:
        print("Brawo, udało się!")
        break
    print("Spróbuj jeszcze raz.")


