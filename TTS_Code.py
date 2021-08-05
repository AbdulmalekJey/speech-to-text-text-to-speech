# This file represents the work done to use the text to speech feature using IBM service
# The main code belongs to Nicholas Renotte




# This parts includes the needed imports from ibm_watson module and ibm_cloud_sdk_core module 

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1

# This is the text to speech code, starts by defining API key variable and URL variable taken from IBM service credentials section
# Defining the authenticator and setting the service URL : 

authenticator = IAMAuthenticator('ssGWtvzi0-JIOfamBO-9JcIg-CvUYbHWynYAMr8rd6ez')
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/e87f5614-09d7-40ea-b0bd-d123fd2a13aa')

# Using the file created from the speech to text feature named (user_speech) and modifying it (removing \n )

with open('user_speech.txt', 'r') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)


# Creating an mp3 file to save the speech and determining the voice 

with open('./audio.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)


