import json
import wikipedia
import datetime

def req_processing(STRING_IP):                  # main processing function
    string_ip = STRING_IP
    STRING_OP = ""
    string_list = string_ip.split()
    word_dict_key_words = ["meaning","definition","define"]
    search_key_words = ["search"]
    voice_log_key_words = ["log"]
    for w in string_list:
        if w in word_dict_key_words:              # case : word dictionary
            word,STRING_OP = word_meaning(string_ip)

        elif w in search_key_words:               # case : wikipedia search
            search_string = string_ip.replace("search ","")
            STRING_OP = search_wiki(search_string)

        elif w in voice_log_key_words:            # case : log the voice message into a text file (memo)
            log_string = string_ip.replace("log ","")
            STRING_OP = voice_log(log_string)

    return STRING_OP                # return the final result of the processing stage



def word_meaning( string_for_dict ):                   # APP_1 - word dictionary

    rm = [ "a ","the ","of ","what ","find ","is ","word ","meaning ","definition ","define "," "]


    for r in rm:
        string_for_dict = string_for_dict.replace(r,"")

    word = string_for_dict
    word = word.lower()
    word_dict = json.load(open('word-dictionary/word_data.json','r'))

    empty = " "

    if word in word_dict:
        meaning = word_dict[word][0]
        return word,meaning
    else:
        return word,empty          


def search_wiki(string_ip):                             # APP_2 wikipedia search
    response = wikipedia.page(string_ip)
    #print(response.url)
    #print(response.title)

    content = response.content
    sentence_list = content.split('.')
    sentence_list_new = [' ', ' ', ' ']

    for i in range(0,3):
        sentence_list_new[i] = sentence_list[i]
        sentence_list_new[i] = sentence_list_new[i].encode('utf-8')

    del sentence_list
    sentence = ""
    for each_sentence in sentence_list_new:
        sentence = sentence + each_sentence + '.'
    return sentence


def voice_log(log_string):                               # APP_3 voice log into text memo
    now = datetime.datetime.now()
    now_str = now.strftime("[%d/%m/%Y] - %H:%M:%S  ")
    log_string_new = now_str + log_string

    log_file = open('message-logging/memo.txt','a')
    log_file.write(log_string_new + '\n')
    log_file.close()
    return "recorded"


#req_processing("log fleur de lis")
