import json
from difflib import get_close_matches

def word_meaning( word ):
    word = word.lower()
    word_dict = json.load(open('word_data.json','r'))

    match_list =  get_close_matches(word,word_dict.keys())

    if word in word_dict:
        [ print(str(i+1) + ' ' + word_dict[word][i]) for i in range(0,len(word_dict[word])) ]
    elif len( match_list ) > 0:
        print("Did you mean   {}    ? [y/n]".format(match_list[0] ))
        prompt = input()
        if prompt == 'y' or prompt == 'Y':
             [ print(str(i+1) + ' ' + word_dict[match_list[0]][i]) for i in range(0,len(word_dict[match_list[0]])) ]
        elif prompt == 'n' or prompt == 'N':
            print("enter a valid word")
        else:
            print("unknown prompt input")
    else:
        print("wrong input")


while True:
    w = input('\nSearch for : ')
    word_meaning(w)
