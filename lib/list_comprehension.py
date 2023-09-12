#!/usr/bin/env python3

def return_evens(num_list):
    pass
    # returnValue iterator conditional
    # evenElements lengthOfList ifNumIsEven
    evens = [num for num in num_list if num % 2 == 0]
    return evens 

def make_exclamation(sentence_list):
    pass
    # returnValue iterator
    exclamation = [string + "!" for string in sentence_list]
    return exclamation