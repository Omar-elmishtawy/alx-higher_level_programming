#!/usr/bin/python3
def multiple_returns(sentence):
    """
    return the length of the sentence
    and the first character
    ...

    Parameters
    ---------
    sentence : string

    Return:
        the first character and lenght of the string
    """
    if len(sentence) == 0:
        return 0, None
    else:
        return len(sentence), sentence[0]
