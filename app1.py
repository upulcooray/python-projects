import json
import os
import difflib


data= json.load(open("dictionary.json"))

def def_finder(word):
    if word in data:
        return data[word]

    elif word.lower() in data:
        return data[word.lower()]

    elif word.upper() in data:
        return data[word.upper()]

    elif word.title() in data:
        return data[word.title()]
    
    elif word not in data:
         matches= difflib.get_close_matches(word,possibilities=data.keys(), cutoff= 0.8)
         if len(matches)>0:
             yn= input("Did you mean '{}' instead of '{}', press 'y' if yes and 'n' if not: ".format(matches[0],word))
             if yn== "y" or yn== "Y":
                 return data[matches[0]]
             else:
                 return "The word '%s' doesn't exist. Please re-check!" % word
    
         else:
             return "The word '%s' doesn't exist. Please re-check..!" % word
    # else:
    #     return "The word '%s' doesn't exist. Please re-check!" % word



input_word = input("Enter a word to find the definition: ")

definitions= def_finder(input_word)

# print(definitions)

if type(definitions)== list and len(definitions)>1:
    for i,val in enumerate(definitions, start=1):
         print("Definition {}: ".format(i),val)

elif type(definitions)== list and len(definitions)==1 :
    print("Definition: "+definitions[0])

else:
    print(definitions)
    
#     elif :
#     print(definitions)