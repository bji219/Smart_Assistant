from recordaudio import record_wav
from voicetotext import speech_to_text as stt
from texttovoice import ttv
from askgpt import ask_gpt
from play_sound import play_sound # user func

def main():

    # Get WAV from microphone.
    record_wav()

    # Convert audio into text.
    query = stt("input.wav")

    # Send text to ChatGPT.
    gpt_response = ask_gpt(query)

    # Convert ChatGPT response into audio.
    ttv(gpt_response)

    # Play audio of reponse using pygame.
    play_sound()

if __name__ == "__main__":
    main()