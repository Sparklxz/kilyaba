# DO NOT DELETE | Makes the Kilyaba to English translator function.
def translate_sentence(input_sentence, translation_dict):
    input_words = input_sentence.split()
    translated_words = []
    
    for word in input_words:
        suffix = get_suffix(word)
        base_word = remove_suffix(word, suffix)

        translated_word = translation_dict.get(base_word, base_word)
        translated_word_with_suffix = apply_suffix(translated_word, suffix)

        translated_words.append(translated_word_with_suffix)

    for word in input_words:
        translated_word = translation_dict.get(word, word)
        translated_words.append(translated_word)

    translated_sentence = ' '.join(translated_words)

    if "+" in translated_sentence:
        combined_words = translated_sentence.split("+")
        translated_sentence = "".join(combined_words)

    return translated_sentence

# DO NOT DELETE | Makes the English to Kilyaba translator function.
def reverse_translate_sentence(input_sentence, translation_dict):
    input_words = input_sentence.split()
    translated_words = []

    for word in input_words:
        for conlang_word, eng_translation in translation_dict.items():
            if eng_translation == word:
                translated_words.append(conlang_word)
                break
        else:
            translated_words.append(word)
            
    for word in input_words:
        suffix = get_suffix(word)
        base_word = remove_suffix(word, suffix)

        translated_word = reverse_translation_dict.get(base_word, base_word)
        translated_word_with_suffix = apply_suffix(translated_word, suffix)

        translated_words.append(translated_word_with_suffix)
    
    translated_sentence = ' '.join(translated_words)

    if "+" in translated_sentence:
        combined_words = translated_sentence.split("+")
        translated_sentence = "".join(combined_words)

    return translated_sentence
    
# DELETING THIS IS NOT RECCOMENDED | When the user reports an issue, it goes to the issue report file.
def report_issue(issue):
    ticket_number = generate_ticket_number()
    report_info = f"Ticket Number: {ticket_number}\nIssue: {issue}\n"

    with open("issue_report.txt", "a") as file:
        file.write(report_info + "\n")
    print("Thank you for reporting the issue. We will look into it.")

def generate_ticket_number():
    # Logic to generate a unique ticket number
    import random
    return random.randint(1000000000, 9999999999)

# DELETING THIS IS NOT RECCOMENDED | Makes the suffixes function properly.
def get_suffix(word):
    suffix = ""
    if word.endswith(".PAST"):
        suffix = "zof"
    elif word.endswith(".PL"):
        suffix = "zy"
    return suffix

def remove_suffix(word, suffix):
    return word[:-len(suffix)]

def apply_suffix(word, suffix):
    return word + suffix


# ADDING OR MODIFYING IS ALLOWED | Dictionary for Kilyaba, updates for the dictionary go here.
conlang_dict = {
    # 0.1.0 Alpha Dict [+]
    "kdefdegiuga": "hello",
    "Kdefdegiuga": "Hello",
    "zpeev": "be",
    "Zpeev": "Be",
    "lyal": "I",
    "lyal": "i",
    "megmi": "a",
    "Megmi": "A",
    "kbybo": "the",
    "Kbybo": "The",
    "fgiz": "person",
    "Fgiz": "Person",
    "fgizzy": "people",
    "Fgizzy": "People",
    "sfyl": "tree",
    "Sfyl": "Tree",
    "sfylzy": "trees",
    "Sfylzy": "Trees",
    "zal": "house",
    "Zal": "House",
    "zalzy": "houses",
    "Zalzy": "Houses",
    "sdapy": "dog",
    "Sdapy": "Dog",
    "sdapyzy": "dogs",
    "Sdapyzy": "Dogs",
    "vuym": "bird",
    "Vuym": "Bird",
    "vuymzy": "birds",
    "Vuymzy": "Birds",
    "zzyk": "eat",
    "Zzyk": "Eat",
    "zzykzof": "ate",
    "Zzykzof": "Ate",
    "gkyim": "see",
    "Gkyim": "See",
    "gkyimzof": "seen",
    "Gkyimzof": "Seen",
    "lyed": "do",
    "Lyed": "Do",
    "lyedzof": "did",
    "Lyedzof": "Did",
    "kudty": "kill",
    "Kudty": "Kill",
    "kudtyzof": "killed",
    "Kudtyzof": "Killed",
    "gvoemi": "go",
    "Gvoemi": "Go",
    "gvoemizof": "went",
    "Gvoemizof": "Went",
    "mfyani": "you",
    "Mfyani": "You",
    "nyt": "here",
    "Nyt": "Here",
    "vuuvf": "give",
    "Vuuvf": "Give",
    "vuuvfzof": "gave",
    "Vuuvfzof": "Gave",
    "zofo": "and",
    "Zofo": "And",
    "laydgu": "animal",
    "Laydgu": "Animal",
    "laydguzy": "animals",
    "Laydguzy": "Animals",
    "mys": "apple",
    "Mys": "Apple",
    "myszy": "apples",
    "Myszy": "Apples",
    "sek": "at",
    "Sek": "At",
    "sueky": "brother",
    "Sueky": "Brother",
    "suekyzy": "brothers",
    "Suekyzy": "Brothers",
    "ziyge": "no",
    "Ziyge": "No",
    "peg": "yes",
    "Peg": "Yes",
    "gkyg": "what",
    "Gkyg": "What",
    "nuitv": "when",
    "Nuitv": "When",
    "pnane": "where",
    "Pnane": "Where",
    "vbiyso": "why",
    "Vbiyso": "Why",
    "zkugi": "how",
    "Zkugi": "How",
    "geolvy": "hot",
    "Geolvy": "Hot",
    "nobsi": "big",
    "Nobsi": "Big",
    "lsyg": "black",
    "Lsyg": "Black",
    "bsisi": "red",
    "Bsisi": "Red",
    "byem": "small",
    "Byem": "Small",
    "nsok": "blue",
    "Nsok": "Blue",
    "kdefde": "good",
    "Kdefde": "Good",
    "sdyily": "for",
    "Sdyily": "For",
    "nime": "from",
    "Nime": "From",
    "nez": "in",
    "Nez": "In",
    "gvag": "of",
    "Gvag": "Of",
    "givo": "on",
    "Givo": "On",
    "kogu": "to",
    "Kogu": "To",
    "zzalzy": "that",
    "Zzalzy": "That",
    "mzyaso": "this",
    "Mzyaso": "This",
    # 0.1.1 Alpha Dict [+] [WIP]
    "zdod": "air",
    "Zdod": "Air",
    "zdodzy": "airs",
    "Zdodzy": "Airs",
    "vtyislmaf": "airport",
    "Vtyislmaf": "Airport",
    "vtyislmafzy": "airports",
    "Vtyislmafzy": "Airports",
    "fleg": "alphabet",
    "Fleg": "Alphabet",
    "flegzy": "alphabets",
    "Flegzy": "Alphabets",
    "fub": "altitude",
    "Fub": "Altitude",
    "fubzy": "altitudes",
    "Fubzy": "Altitudes",
    "kuols": "art",
    "Kuols": "Art",
    "kuolszy": "arts",
    "Kuolszy": "Arts",
}

# DO NOT DELETE OR MODIFY | Makes the reverse translations work.
reverse_translation_dict = {v: k for k, v in conlang_dict.items()}

# MODIFYING THIS IS ALLOWED
choice = input("Caution: This translator is a work in progress, and translations may not be entirely accurate or reliable. Unexpected errors and inaccuracies may occur. We appreciate your understanding as we continue to improve the system.\n\n Choose an option:\n1. Kilyaba to English\n2. English to Kilyaba\n3. Syntax Info\n4. Report issue\n")

if choice == "1":
    conlang_sentence = input("WARNING: DO NOT USE PUNCTUATION, IT BREAKS THE TRANSLATOR.\n Enter a sentence in Kilyaba: ")
    translated_sentence = translate_sentence(conlang_sentence, conlang_dict)
    print("Translated to English:", translated_sentence)
    report_option = input("Do you want to report an issue? (Y/N) ")
    if report_option.upper() == "Y":
        issue = input("Please briefly describe the issue: ")
        report_issue(issue)
elif choice == "2":
    english_sentence = input("WARNING: DO NOT USE PUNCTUATION, IT BREAKS THE TRANSLATOR.\n Enter the English translation: ")
    reversed_sentence = reverse_translate_sentence(english_sentence, conlang_dict)
    print("Back-translated to Kilyaba:", reversed_sentence)
    report_option = input("Do you want to report an issue? (Y/N) ")
    if report_option.upper() == "Y":
        issue = input("Please briefly describe the issue: ")
        report_issue(issue)
elif choice == "3":
    print("Syntax:\n\n '+' - Combines words to create compounds, used for adjective+noun.\n '.PAST' - Makes the word past-tense, use it only when the past tensed word doesn't work.\n '.PL' - Makes the word pluralized, use it only when the pluralized word doesn't work.'")
elif choice == "4":
    issue = input("Please briefly describe the issue: ")
    report_issue(issue)
else:
    print("Invalid choice. Restart the translator.")
