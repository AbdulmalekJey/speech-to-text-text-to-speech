# Text-to-speech-and-speech-to-text
Implementing the text to speech and speech to text using python and IBM services

## Contents : 
1- The text to speech code ( TTS.py)    

2- The mp3 recording using the TTS service

3- Screenshots for the TTS implementation 

4- The speech to text code ( since it is a clone of an existing code I will post the needed files and show the rest as screenshots)

5- The text file created by the STT service

6- Screenshots for the STT implementation

## Details :
The text to speech and speech to text features are widely used. In this task IBM services were used in order to help implementing these features with python.
The main idea behind these features for this project is to make the chatbot interactive by making it capable of recognizing speech and giving it the ability to speak.
To do that there are general steps for both features and some specific steps for each one.

### General steps : 
First of all in order to use the IBM service you need to have an account on IBM cloud and choose the service you want then create it.
After creating the service you need, you will be provided with the API key and the URL which gives you the ability to use the service in your python code.
Second, you need a python editor, you can use Jupyter or VS code. I used VS code.
Third, the codes start with authenticating and creating the server.

### STT :
Since I decided to implement this feature using my microphone instead of an audio file I had to clone Watson-streaming-stt code by Nicholas Renotte.
For this service the steps include :
- Installing pyaudio

- Importing required packages

- Determining the default input device 

- Determining the region ( must match the model ) 


### TTS :

For this service the steps include : 
- Importing TextToSpeechV1

- Using the file created from the speech to text feature named (user_speech.txt) and modifying it (removing \n )

- Creating an mp3 file to save the speech and determining the voice (en-GB_JamesV3Voice in this case)
