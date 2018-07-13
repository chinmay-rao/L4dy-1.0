# Lady-Leaf
Speech-enabled goal-oriented dialogue system with rule-based context determination and very limited features (for now). 


[Phase-1]:STT conversion
[Phase-2]:Context extraction
[Phase-3]:TTS conversion
[chain]:All the phases chained

![alt text](https://raw.githubusercontent.com/chinmay-rao/L4dy-1.0/master/%5Bblock-diagram%5D.png)

The system’s working can be broken down into a sequence of three fundamental processes:
1. Speech-to-text conversion of the user’s query
2. Processing stage: Rule-based context determination and app interaction
3. Text-to-Speech conversion of the reply string 



Breakdown of the system operation:

A. Speech data acquisition:
The system first has to acquire the speech data from the user for further processing. In order to do this, a microphone is needed. In order to make the system design simple, a specialized USB microphone can be used, as shown in the block diagram. But, an inexpensive alternative is to use a generic head-set (having an inbuilt mic) with an external USB sound card. The sound card is required as the Raspberry Pi board doesn’t have a 3.5mm audio-in channel, and since the head-sets come with 3.5mm audio plugs, the sound card helps interface one with the board via USB. An external button, interfaced with the board’s GPIO pins, has to be pressed by the user before issuing a query, after which the system opens the input device port for capturing the speech data. 

B. Raspberry Pi system block:
This section is where the main operations of the system take place. This section is further divided into the following three stages:
i. Speech-to-Text conversion:
The audio data captured from the microphone has to be converted to a character string before doing any further processing. Speech to text conversion tasks can be done in a number of different ways – using a conversion engine (such as PocketSphinx), deploying trained neural models (such as RNNs and LSTMs) locally, or using cloud services.
Since the Raspberry Pi board is evidently scarce of enough memory and computational power to carry out the computationally intensive speech to text conversion task, utilizing cloud services appears to be a much better option than the rest. The only mandate, here, is that the system should always be connected to the internet to be functional.
Some of the best cloud conversion service providers include Google Cloud, IBM Watson, Amazon Transcribe and Houndify. Each one of them provides Python libraries and SDKs to interact with the conversion service APIs. The service used in this project is Houndify.
A Python script obtains the recorded audio and transfers it to the cloud API by utilizing various classes provided by the houndify Python library. After the conversion, the cloud API returns a string which is the transcript of the user’s speech query. This string is now ready for further processing.

ii. Request processing:
Once we have the transcript of the user’s query, there are two ways one can go to make the system understand what action to take based on the given text: deploying a trained language model (artificial intelligence technique), or using a rule-based approach.
The latter approach has been used in this project to keep the system’s complexity lower, initially. In order to determine the nature of the user’s query, a set of rules and words are written using which the transcript string is parsed and broken down into its essence.  During parsing, the system decides which predefined task or “app” should be called, and the extracted essence of the string is passed to the particular app.
Predefined tasks / Apps - The aforementioned predefined tasks or “apps” are, basically, Python scripts each having a unique function. Initially, the system has three apps, meaning the number of diverse tasks it can perform is just three. They are as follows:
a. English Word Dictionary – This app is invoked when the user asks the system the word meaning of any English word. A word meaning database is present locally in the system, using which the script returns the corresponding word meaning(s) of the asked English word.
b. Web search – This app takes a word or a phrase as a parameter and searches predefined informative websites for the same, returning at least a paragraph long of information regarding it. The domain to which the system interacts now is Wikipedia, but it can be extended to search blog sites too for information.
c. Message logging – This app is a form of a reminder, and the user can use it to record important information such as schedules, lists, tasks-to-do, etc. It records the given information into a text file along with the corresponding time and date.
