#!/usr/bin/python3

def multiple_returns(sentence):
    """returns a tuple with the length <sentence>
       and its first character."""
    if len(sentence) == 0:
        return ((len(sentence), None))
    else:
        return ((len(sentence), sentence[0]))
