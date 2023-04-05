'''Packages'''
# Record Audio
import os
import sounddevice as sd
from scipy.io.wavfile import write

# Whisper
import whisper

# Ask GPT
import openai

# Text to Voice
from google.cloud import texttospeech

# Play sound
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()
pygame.mixer.init()
import math

'''User Functions'''
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

def speech_to_text(speech_file):

    # Whisper AI model from OpenAI
    model = whisper.load_model('base')

    print("Transcribing speech to text...")
    # Transcribe the speech
    stt = model.transcribe(speech_file, fp16=False)
    stt_str = stt['text']

    print("Prompt:")
    print(stt_str)
    return stt_str

def ask_gpt(query):
# query = " What's the biggest difference between a champion, formula one driver and all the others?"

    print("Asking GPT...")
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
    print("GPT response:")
    print(gpt_response)

    return gpt_response

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/BrendanInglis/PycharmProjects/Whisper/gpt-voice-assistant-381804-f8132be95ba7.json'

def ttv(input_text):

    print("Transcribing text to voice...")

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

def play_sound():
    pygame.init()
    pygame.mixer.init()
    sounda = pygame.mixer.Sound("result.wav")

    # Query length of the response so that the computer can play it
    rest_time = "length", sounda.get_length()
    # rt = round(rest_time[1])
    rt = math.floor(rest_time[1])
    sounda.play()
    time.sleep(rt)

    return

def main():

    # Get WAV from microphone.
    record_wav()

    # Convert audio into text.
    query = speech_to_text("input.wav")

    # Send text to ChatGPT.
    gpt_response = ask_gpt(query)

    # Convert ChatGPT response into audio.
    ttv(gpt_response)

    # Play audio of reponse using pygame.
    play_sound()

if __name__ == "__main__":
    main()