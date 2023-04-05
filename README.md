# Smart Assistant (Jarvis)
Using OpenAI Whisper API, ChatGPT 3.5 turbo API, and Google Cloud Text to Speech API to create a better Siri!

## Workflow and Main Execution 
### Record speech --> Speech to text --> Text to ChatGPT --> Text to Voice --> Play audio

Notice that these are custom functions (just importing the functions from the other py files).
```python
def main():

    # Get WAV from microphone
    record_wav()

    # Convert audio into text
    query = stt("input.wav")

    # Send text to ChatGPT.
    gpt_response = ask_gpt(query)

    # Convert ChatGPT response into audio
    ttv(gpt_response)

    # Play audio of reponse using pygame
    play_sound()

if __name__ == "__main__":
    main()
```

## Python packages used (in no particular order):
```python
import time
import os
import sounddevice as sd
from scipy.io.wavfile import write
import openai
import whisper
from google.cloud import texttospeech
import pygame
import math
```

## Background and Inspiration
Inspired by [this post](https://www.hackster.io/nickbild/voicegpt-f88f8f) by Nick Bild on Hackster.io. His original project used a raspberry pi, but I decided to use my Mac and make a replacement for Siri!

## Record Speech (sounddevice)
The function plays a 'bleep' sound to indicate when recording has started and finished (bleep not included! You'll have to download your own). It saves a .wav file of the input to the working directory.

```python
def record_wav():
    # Sample rate + duration of recording
    fs = 44100
    seconds = 8

    # Get length of recording
    print("Recording for " + str(seconds) + " seconds...")

    # Play noise to indicate recording for Siri
    sounda = pygame.mixer.Sound("start_rec.wav")
    sounda.play()

    # Record input audio
    myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1)
    sd.wait() # Wait until recording is finished

    print("Recording complete.")

    # Noise to indicate end of recording
    soundb = pygame.mixer.Sound("stop_rec.wav")
    soundb.play()

    # Save input audio file
    write('input.wav', fs, myrecording) # Save as WAV file

    return
```

## Whisper API
```python
def speech_to_text(speech_file):

    # Whisper AI model from OpenAI
    model = whisper.load_model('base')

    stt = model.transcribe(speech_file)

    stt_str = stt['text']
    print(stt_str)
    return stt_str
```

## ChatGPT API
```python
import openai

def ask_gpt(query):
# query = " What's the biggest difference between a champion, formula one driver and all the others?"

    # example with a system message
    MODEL = "gpt-3.5-turbo"

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You must answer concisely as a helpful assistant."},
            {"role": "user", "content": query},
        ],
        temperature=0,
    )
    gpt_response = response['choices'][0]['message']['content']
    print(gpt_response)

    return gpt_response
```

## Google Cloud Texttospeech API
```python
from google.cloud import texttospeech
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/credentials/creds.json'

def ttv(input_text):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text= input_text) # tts)

    # Build the voice request, select the language code ("en-US") and the ssml
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Neural2-F",ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("result.wav", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)

    return
```

# Improvements/To-Do
- Recording length is set to 8 seconds, but ideally it would be arbitrary and dependent on the query length. A user would press and hold a button, speak the query, then release to end recording.
