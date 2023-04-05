#!/usr/bin/env python3
import os
import sounddevice as sd
from scipy.io.wavfile import write
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()
pygame.mixer.init()

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