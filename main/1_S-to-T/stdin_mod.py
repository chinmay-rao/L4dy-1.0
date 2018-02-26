#!/usr/bin/env python

client_id = '3tS3gR4WDtLoTM7i5ibXVA=='
client_key = 'dNutJKcJ8DuPGvWOHh72cq8oJF8o2J2435q8j8QI3slWbrg5Uz68FxGkWTdcvJTYYlMsoC3_xRHqM4l6BmvcHw=='
user_id = "Leaf"

import houndify
import sys

if __name__ == '__main__':

    #CLIENT_ID = sys.argv[1]
    #CLIENT_KEY = sys.argv[2]

    CLIENT_ID = client_id
    CLIENT_KEY = client_key

    #
    # Simplest HoundListener; just print out what we receive.
    #
    # You can use these callbacks to interact with your UI.
    #
    class MyListener(houndify.HoundListener):
        def onPartialTranscript(self, transcript):
            #print "Partial transcript: " + transcript
            pass

        def onFinalResponse(self, response):
            #print "Final response: " + str(response)
            #response_list = zip(response.keys(),response.values())
            #STRING = response_list[3][1]['ChoiceData'][0]['Transcription']        # 'STRING' contains the received string
            STRING = response['AllResults'][0]['SpokenResponseLong']
            print(STRING)

        def onError(self, err):
            print("Error: " + str(err))

    client = houndify.StreamingHoundClient(CLIENT_ID, CLIENT_KEY, user_id)
    listener = MyListener()

    BUFFER_SIZE = 512
    samples = sys.stdin.read(BUFFER_SIZE)
    finished = False
    client.start(listener)

    while not finished:
        finished = client.fill(samples)
        samples = sys.stdin.read(BUFFER_SIZE)   #read samples from the audio from mic given during execution
        if len(samples) == 0:
            break
    client.finish()
