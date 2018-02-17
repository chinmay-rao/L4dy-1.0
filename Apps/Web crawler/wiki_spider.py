import wikipedia

def search_wiki(STRING_IP):
    response = wikipedia.page(STRING_IP)
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
        sentence = sentence + str(each_sentence) + '.'
    print(sentence)


search_wiki("elon musk")
