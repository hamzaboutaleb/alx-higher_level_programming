#!/use/bin/pyhton3

def multiple_returns(sentence):
    new_tuple = (len(sentence), None if (len(sentence) == 0) else sentence[0])
    return new_tuple