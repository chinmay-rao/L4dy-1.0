#!/usr/bin/env python

CLIENT_ID = '3tS3gR4WDtLoTM7i5ibXVA=='
CLIENT_KEY = 'dNutJKcJ8DuPGvWOHh72cq8oJF8o2J2435q8j8QI3slWbrg5Uz68FxGkWTdcvJTYYlMsoC3_xRHqM4l6BmvcHw=='
user_id = "Leaf"

STRING = ""

import houndify
import sys

if __name__ == '__main__':

    class MyListener(houndify.HoundListener):
        def onPartialTranscript(self, transcript):
            #print "Partial transcript: " + transcript
            pass

        def onFinalResponse(self, response):
            #print "Final response: " + str(response)
            # 'STRING' contains the received string
            string = response['AllResults'][0]['SpokenResponseLong']
            with open('S_to_T-result.txt','w') as result_file:
                result_file.write(string)

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

    with open('S_to_T-result.txt','r') as result_file:
        STRING = result_file.read()   

#-----------------passing the string for context-extraction----------------#
    import process
    REPLY = process.req_processing(STRING)
    print(REPLY)

#-----------------send for TTS conversion , play the result----------------#
    import tts_mod
    tts_mod.TTS_convert(REPLY)
