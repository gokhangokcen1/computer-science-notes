def smash(words):
    """ ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great' """
    sentence = ""
    for word in words:
        sentence += word + " "
    return sentence.strip()
    
