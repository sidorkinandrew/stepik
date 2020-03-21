def process(sentences):
    result = []
    for asentence in sentences:
        processed = []
        for aword in asentence.split():
            if len([letter for letter in aword if letter.isalpha()]) == len(aword):
                processed.append(aword)
        result.append(' '.join(processed))
    return result