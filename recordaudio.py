# import pyaudio
import wave
import sounddevice as sd
from scipy.io.wavfile import write
import datetime
import time

def record_wav():

    fs = 44100 # Sample rate
    seconds = 8 # Duration of recording

    # Get length of recording
    print("Recording for " + str(seconds) + " seconds.")
    print("Ask away!")
    myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1)
    sd.wait() # Wait until recording is finished

    print("Recording complete.")

    write('input.wav', fs, myrecording) # Save as WAV file

    return