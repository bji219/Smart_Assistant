#!/usr/bin/env python3
import whisper

def speech_to_text():

    # Whisper AI model from OpenAI
    model = whisper.load_model('base')

    print("Transcribing speech to text...")
    # Transcribe the speech
    stt = model.transcribe("input.wav", fp16=False)
    stt_str = stt['text']

    print("Prompt:")
    print(stt_str)

    return stt_str