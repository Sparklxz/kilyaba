import random

# ADDING OR MODIFYING IS ALLOWED | Dictionary for Kilyaba, updates for the dictionary go here.
conlang_dict = {
    # 0.1.0 Alpha Dict [+]
    "kdefdegiuga": "hello",
    "Kdefdegiuga": "Hello",
    "lyal": "i",
    "Lyal": "I",
    "lyal.OBJ1": "me",
    "Lyal.OBJ": "Me",
    "lyal.POSS1": "my",
    "Lyal.POSS1": "My",
    "lyal.REF1": "myself",
    "Lyal.REF1": "Myself",
    "zpeev": "be",
    "Zpeev": "Be",
    "zpeev.COP3SG": "is",
    "Zpeev.COP3SG": "Is",
    "zpeev.PRES3SG": "is.PRES3SG",
    "Zpeev.PRES3SG": "Is.PRES3SG",
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
    # 0.2 Alpha Dict [+]
    "gkygfgiz": "who",
    "Gkygfgiz": "Who",
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
    "vgoys": "ash",
    "Vgoys": "Ash",
    "vgoyszy": "ashes",
    "Vgoyszy": "Ashes",
    "pbez": "ass",
    "Pbez": "Ass",
    "pbezzy": "asses",
    "Pbezzy": "Asses",
    "ftuugt": "backpack",
    "Ftuugt": "Backpack",
    "ftuugtzy": "backpacks",
    "Ftuugtzy": "Backpacks",
    "kaadn": "bacon",
    "Kaadn": "Bacon",
    "kaadnzy": "bacons",
    "Kaadnzy": "Bacons",
    "lopo": "bag",
    "Lopo": "Bag",
    "lopozy": "bags",
    "Lopozy": "Bags",
    "subo": "blood",
    "Subo": "Blood",
    "subozy": "bloods",
    "Subozy": "Bloods",
    "fyfo": "book",
    "Fyfo": "Book",
    "fyfozy": "books",
    "Fyfozy": "Books",
    "skuv": "car",
    "Skuv": "Car",
    "skuvzy": "cars",
    "Skuvzy": "Cars",
    "mfulu": "cat",
    "Mfulu": "Cat",
    "mfuluzy": "cats",
    "Mfuluzy": "Cats",
    "kduta": "data",
    "Kduta": "Data",
    "kdutazy": "datas",
    "Kdutazy": "Datas",
    "baob": "friend",
    "Baob": "Friend",
    "baobzy": "friends",
    "Baobzy": "Friends",
    "miep": "game",
    "Miep": "Game",
    "miepzy": "games",
    "Miepzy": "Games",
    "bgid": "god",
    "Bgid": "God",
    "bgidzy": "gods",
    "Bgidzy": "Gods",
    "fivi": "hat",
    "Fivi": "Hat",
    "fivizy": "hats",
    "Fivizy": "Hats",
    "meonn": "hoe",
    "Meonn": "Hoe",
    "meonnzy": "hoes",
    "Meonnzy": "Hoes",
    "dlegy": "lettuce",
    "Dlegy": "Lettuce",
    "dlegyzy": "lettuces",
    "Dlegyzy": "Lettuces",
    "mluinzu": "level",
    "Mluinzu": "Level",
    "mluinzuzy": "levels",
    "Mluinzuzy": "Levels",
    "fluto": "nut",
    "Fluto": "Nut",
    "flutozy": "nuts",
    "Flutozy": "Nuts",
    "knaudg": "onion",
    "Knaudg": "Onion",
    "knaudgzy": "onions",
    "Knaudgzy": "Onions",
    "ttyupm": "orange",
    "Ttyupm": "Orange",
    "ttyupmzy": "oranges",
    "Ttyupmzy": "Oranges",
    "nimy": "pencil",
    "Nimy": "Pencil",
    "nimyzy": "pencils",
    "Nimyzy": "Pencils",
    "fod": "salad",
    "Fod": "Salad",
    "fodzy": "salads",
    "Fodzy": "Salads",
    "geolo": "spoon",
    "Geolo": "Spoon",
    "geolozy": "spoons",
    "Geolozy": "Spoons",
    "gmet": "translate",
    "Gmet": "Translate",
    "gmetzof": "translated",
    "Gmetzof": "Translated",
    "gmetfgiz": "translater",
    "Gmetfgiz": "Translater",
    "gmetfgizzy": "translaters",
    "Gmetfgizzy": "Translaters",
    "lyle": "ask",
    "Lyle": "Ask",
    "lylezof": "asked",
    "Lylezof": "Asked",
    "ziez": "bite",
    "Ziez": "Bite",
    "ziezzof": "bit",
    "Ziezzof": "Bit",
    "nazi": "born",
    "Nazi": "Born",
    "ksof": "build",
    "Ksof": "Build",
    "ksofzof": "built",
    "Ksofzof": "Built",
    "zfyopi": "burn",
    "Zfyopi": "Burn",
    "zfyopizof": "burnt",
    "Zfyopizof": "Burnt",
    "vsueva": "buy",
    "Vsueva": "Buy",
    "vsuevazof": "bought",
    "Vsuevazof": "Bought",
    "liyno": "can",
    "Liyno": "Can",
    "liynozof": "could",
    "Liynozof": "Could",
    "zzav": "collect",
    "Zzav": "Collect",
    "zzavzof": "collected",
    "Zzavzof": "Collected",
    "ndipy": "create",
    "Ndipy": "Create",
    "ndipyzof": "created",
    "Ndipyzof": "Created",
    "mvap": "drink",
    "Mvap": "Drink",
    "mvapzof": "drank",
    "Mvapzof": "Drank",
    "kuso": "fall",
    "Kuso": "Fall",
    "kusozof": "fell",
    "Kusozof": "Fell",
    "deyba": "fuck",
    "Deyba": "Fuck",
    "deybazof": "fucked",
    "Deybazof": "Fucked",
    "nzepy": "hate",
    "Nzepy": "Hate",
    "nzepyzof": "hated",
    "Nzepyzof": "Hated",
    "zilaz": "hear",
    "Zilaz": "Hear",
    "zilazzof": "heard",
    "Zilazzof": "Heard",
    "kiizdi": "help",
    "Kiizdi": "Help",
    "kiizdizof": "helped",
    "Kiizdizof": "Helped",
    "sep": "jump",
    "Sep": "Jump",
    "sepzof": "jumped",
    "Sepzof": "Jumped",
    "ttaovzy": "learn",
    "Ttaovzy": "Learn",
    "ttaovzyzof": "learned",
    "Ttaovzyzof": "Learned",
    "dyko": "like",
    "Dyko": "Like",
    "dykozof": "liked",
    "Dykozof": "Liked",
    "fyn": "live",
    "Fyn": "Live",
    "fynzof": "lived",
    "Fynzof": "Lived",
    "liso": "look",
    "Liso": "Look",
    "lisozof": "looked",
    "Lisozof": "Looked",
    "znamo": "love",
    "Znamo": "Love",
    "znamozof": "loved",
    "Znamozof": "Loved",
    "nmysa": "make",
    "Nmysa": "Make",
    "nmysazof": "made",
    "Nmysazof": "Made",
    "ssid": "need",
    "Ssid": "Need",
    "ssidzof": "needed",
    "Ssidzof": "Needed",
    "tbuidzy": "play",
    "Tbuidzy": "Play",
    "tbuidzyzof": "played",
    "Tbuidzyzof": "Played",
    "bleg": "read",
    "Bleg": "Read",
    "nkib": "run",
    "Nkib": "Run",
    "nkibzof": "ran",
    "Nkibzof": "Ran",
    "gosgo": "say",
    "Gosgo": "Say",
    "gosgozof": "said",
    "Gosgozof": "Said",
    "gkyim": "see",
    "Gkyim": "See",
    "gkyimzof": "seen",
    "Gkyimzof": "Seen",
    "tyn": "sit",
    "Tyn": "Sit",
    "tynzof": "sat",
    "Tynzof": "Sat",
    "vubu": "sleep",
    "Vubu": "Sleep",
    "vubuzof": "slept",
    "Vubuzof": "Slept",
    "zmyal": "start",
    "Zmyal": "Start",
    "zmyalzof": "started",
    "Zmyalzof": "Started",
    "mlez": "stop",
    "Mlez": "Stop",
    "mlezzof": "stopped",
    "Mlezzof": "Stopped",
    "tuivu": "talk",
    "Tuivu": "Talk",
    "tuivuzof": "talked",
    "Tuivuzof": "Talked",
    "pmium": "think",
    "Pmium": "Think",
    "pmiumzof": "thought",
    "Pmiumzof": "Thought",
    "zfip": "understand",
    "Zfip": "Understand",
    "zfipzof": "understood",
    "Zfipzof": "Understood",
    "glyada": "use",
    "Glyada": "Use",
    "glyadazof": "used",
    "Glyadazof": "Used",
    "pgif": "write",
    "Pgif": "Write",
    "pgifzof": "wrote",
    "Pgifzof": "Wrote",
    "tasde": "all",
    "Tasde": "All",
    "lvyeve": "available",
    "Lvyeve": "Available",
    "tif": "bad",
    "Tif": "Bad",
    "fyne": "beautiful",
    "Fyne": "Beautiful",
    "loobde": "best",
    "Loobde": "Best",
    "zianta": "better",
    "Zianta": "Better",
    "lsyty": "bright",
    "Lsyty": "Bright",
    "buyg": "cold",
    "Buyg": "Cold",
    "buesgy": "common",
    "Buesgy": "Common",
    "mpeb": "difficult",
    "Mpeb": "Difficult",
    "fnaokz": "easy",
    "Fnaokz": "Easy",
    "miagp": "favourite",
    "Miagp": "Favourite",
    "byen": "happy",
    "Byen": "Happy",
    "geolvy": "hot",
    "Geolvy": "Hot",
    "mdoez": "important",
    "Mdoez": "Important",
    "dip": "new",
    "Dip": "New",
    "vas": "nice",
    "Vas": "Nice",
    "tefge": "old",
    "Tefge": "Old",
    "pyva": "real",
    "Pyva": "Real",
    "lziusi": "young",
    "Lziusi": "Young",
    "Kily": "Kilyaba",
    "kily": "kilyaba",
    "vup": "he",
    "Vup": "He",
    "kyly": "she",
    "Kyly": "She",
    "vaely": "they",
    "Vaely": "They",
    "ngyiski": "english",
    "Ngyiski": "English",
    "teatta": "earth",
    "Teatta": "Earth",
    "maydvi": "madrid",
    "Maydvi": "Madrid",
    "poytga": "portuguese",
    "Poytga": "Portuguese",
    "ruiski": "russian",
    "Ruiski": "Russian",
    "spaynki": "spanish",
    "Spaynki": "Spanish",
}

# DO NOT DELETE | Makes the Kilyaba to English translator function.
def translate_sentence(input_sentence, translation_dict):
    input_words = input_sentence.split()
    translated_words = []
    
    for word in input_words:
        if word in translation_dict:
            translated_word = translation_dict[word]
        elif word == "lyal":
            translated_word = random.choice(["i", "me", "my", "myself"])
        elif word == "Lyal":
            translated_word = random.choice(["I", "Me", "My", "Myself"])
        else:
            translated_word = word
        translated_words.append(translated_word)
    
    for word in input_words:
        suffix = get_suffix(word)
        base_word = remove_suffix(word, suffix)

        translated_word = translation_dict.get(base_word, base_word)
        translated_word_with_suffix = apply_suffix(translated_word, suffix)

        translated_words.append(translated_word_with_suffix)

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
    if word.endswith(".PT"):
        suffix = "zof"
    elif word.endswith(".PL"):
        suffix = "zy"
    return suffix

def remove_suffix(word, suffix):
    return word[:-len(suffix)]

def apply_suffix(word, suffix):
    return word + suffix

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
    print("Syntax:\n\n '+' - Combines words to create compounds, used for adjective+noun.\n '.PT' - Makes the word past-tense, use it only when the past tensed word doesn't work.\n '.PL' - Makes the word pluralized, use it only when the pluralized word doesn't work.\n '.OBJ1' - Makes it a First Person Singular Object Pronoun.\n '.POSS1' - Makes it a First Person Singular Possessive Pronoun\n '.REF1' - Makes it a Reflexive Pronoun\n 'PRES3SG' - Makes it a Third Person Singular Present Tense \n '.COP3SG' - Makes it a Third person singular copula.\n '.EXIST3SG' - Makes it a Third Person Singular Existential Verb")
elif choice == "4":
    issue = input("Please briefly describe the issue: ")
    report_issue(issue)
else:
    print("Invalid choice. Restart the translator.")
