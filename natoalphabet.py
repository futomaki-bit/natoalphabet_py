# Program to convert word into nato alphabet
from string import *

print("Convert your word into nato alphabet")
word = str(input("Enter your word now\n"))
print()

def nato(letter):
    return{
        "a": "Alfa",
        "b": "Bravo",
        "c": "Charlie",
        "d": "Delta",
        "e": "Echo",
        "f": "Foxtrot",
        "g": "Golf",
        "h": "Hotel",
        "i": "India",
        "j": "Juliett",
        "k": "Kilo",
        "l": "Lima",
        "m": "Mike",
        "n": "November",
        "o": "Oscar",
        "p": "Papa",
        "q": "Quebec",
        "r": "Romeo",
        "s": "Sierra",
        "t": "Tango",
        "u": "Uniform",
        "v": "Victor",
        "w": "Whiskey",
        "x": "Xray",
        "y": "Yankee",
        "z": "Zulu",
        " ": ""
    }[letter]


def printnato(letter):
    print(nato(letter.lower()))


print(word + " in nato alphabet:")
for letter in word:
    printnato(letter)
