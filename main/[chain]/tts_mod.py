import voicerss_tts
import os
#import playsound

#text_data = 'in love may you find the next'
def TTS_convert(text_data):
    
    voice = voicerss_tts.speech({
        'key': 'c1ba0e652b814a2da2a20b0133d82afa',
        'hl': 'en-us',
        'src': text_data,
        'r': '0',
        'c': 'wav',                # 'mp3' changed to 'wav'
        'f': '44khz_16bit_stereo',
        'ssml': 'false',
        'b64': 'false'
        })

    with open('audio_op.wav','w') as aud:
      aud.write(voice['response'])

    #playsound.playsound('audop.wav', True)
    print("playing")
    os.system("aplay -D plughw:0,0 audio_op.wav")

    #print(voice['response'])
    #print(voice)
