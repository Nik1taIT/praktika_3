morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    # Додати решту символів
}

user_input = input("Enter a letter: ").upper()
if user_input in morse:
    print(f"Азбука морза {user_input} є {morse[user_input]}")
