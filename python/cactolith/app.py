# This function counts all the syllables of a word
def syllables(word):
    word = word.lower()
    counter = 0
    vowels = "aeiou"
    if word[0] in vowels:
        counter += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            counter += 1
    if word.endswith("e"):
        counter -= 1
    if counter == 0:
        counter += 1
    return counter

# This function generates statistics
def statistics(location):
    complex = 0
    sentences = 0
    words = 0
    f = open(location, "r")
    lns = f.readlines()
    for i in lns:
        i = i.strip()
        array = []
        toArray = i.replace(",", "")
        toArray = toArray.replace(".", "")
        toArray = toArray.replace("(", "")
        toArray = toArray.replace(")", "")
        toArray = toArray.split(" ")
        for x in toArray:
            array.append(x)
            words += 1
        for w in array:
           ltrg = syllables(w)
           if ltrg >= 3:
               complex += 1
    sentences = len(lns)
    f.close()
    return (sentences, words, complex)

# What is gunningfog?
# This is a tool that tries to calculate the Gunning Fog Index.
# It is a weighted average of the number of words per sentence, and the number
# of long words per word. An interpretation is that the text can be understood
# by someone who left full-time education at a later age than the index.
# Source: http://gunning-fog-index.com/

def gunningfog(location):
    stats = statistics(location)
    sentences = int(stats[0])
    words = int(stats[1])
    complex = int(stats[2])
    formula = 0.4 * ((words/sentences) + 100 * (complex/sentences))
    return formula

# This is the main of the file.
def main():
    print(syllables('cactolith'))
    print(statistics('maths.txt'))

# This runs the main function
if __name__ == "__main__":
    main()
