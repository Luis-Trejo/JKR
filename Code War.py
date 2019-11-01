Problema ---> Definir funcion que devuelva una concatenacion de dos strings sin duplicidades y ordenado

Mi solucion

def longest(s1, s2):
    # your code
    distinct = set(s1+s2) # sets are distinct values! 
    distinctSorted = sorted(distinct) # turn into sorted list
    return ''.join(distinctSorted) # concatenate to string with 'join'

Las mejores soluciones

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))

Hay alguien peor que Yo

def longest(s1, s2):
    # your code
    
    # Defining the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Concatenating the Two Given Strings
    s = s1 + s2
    
    # Declaring the Output Variable
    y = ""
    
    # Comparing whether a letter is in the string
    for x in alphabet:
      if x not in s:
        continue
      if x in s:
        y = y + x
        
    # returning the final output    
    return y