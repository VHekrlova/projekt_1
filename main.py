"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Veronika Hekrlová
email: VHekrlova@seznam.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Přihlašovací údaje
username = input("username: ")
password = input("password: ")

if username in users and users[username] == password:
    print(f"Welcome to the app {username}!")
    print(f"We have {len(TEXTS)} texts to be analysed.")
else:
    print("unregistered user, terminating the program.")
    exit()

# Výběr textu k analýze
choice = input(f"Enter the number between 1 and {len(TEXTS)} to select: ")    

if not choice.isdigit():
    print("Invalid input. You must enter a number. Terminating the program.")
    exit()

choice = int(choice)

if choice not in range(1, len(TEXTS) + 1):
    print("Invalid input. The number is out of range. Terminating a program.")
    exit()

# Analýza textu

text = TEXTS[choice - 1]
words = text.split()

word_count = 0
titlecase = 0
uppercase = 0
lowercase = 0
digit = 0
digit_sum = 0
length_freq = {}

for word in words:
    word = word.strip('.,?!')
    word_count = word_count + 1
    length = len(word)
    length_freq[length] = length_freq.get(length, 0) + 1

    if word.istitle():
        titlecase = titlecase + 1
    elif word.isupper():
        uppercase = uppercase + 1
    elif word.islower():
        lowercase = lowercase + 1
    elif word.isdigit():
        digit = digit + 1
        digit_sum = digit_sum + int(word)  
           


# Výstup
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {digit} numeric strings.")
print(f"The sum of all the numbers {digit_sum}.")
print("----------------------------------------")

print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")

for length in sorted(length_freq):
    count = length_freq[length]
    stars = "*" * count
    print(f"{length:>3}|{stars:<18}|{count}")