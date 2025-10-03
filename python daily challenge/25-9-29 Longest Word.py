def get_longest_word(sentence):
    sentence = sentence.replace(".", "")
    sentence = sentence.split(" ")
    x = len(sentence[0])
    longest_word = sentence[0]
    for i in range(len(sentence) - 1):
        if len(sentence[i + 1]) > x:
            x = len(sentence[i + 1])
            longest_word = sentence[i+1]
    return longest_word
