def amount_of_words(text):
    return len(text.split())

def amount_of_characters(text):
    characters = {}
    parsedText = text.lower()

    for i in range(0, len(parsedText)):
        character = parsedText[i]
        if (character in characters):
            characters[character] += 1
        else:
            characters[character] = 1

    return characters

def sort_on(items):
    return items["num"]

def sorted_characters(characters):
    sorted_dict = []
    for char in characters:
        sorted_dict.append({"char": char, "num": characters[char]})

    print(sorted_dict)
        
    sorted_dict.sort(reverse=True, key=sort_on)
  
    return sorted_dict