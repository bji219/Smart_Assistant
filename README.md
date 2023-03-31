# Smart Assistant (Jarvis)
Using OpenAI Whisper API, ChatGPT 3.5 turbo API, and Google Cloud Text to Speech API to create a better Siri!

## Workflow
### Record speech --> Speech to text --> Text to ChatGPT --> Text to Voice --> Play audio

## Python packages used (in no particular order)
```python
import time
import os
import sounddevice as sd
from scipy.io.wavfile import write
import openai
import whisper
from google.cloud import texttospeech
import pygame
```

## Background and Inspiration
Inspired by [this post]()

## Record Speech (sounddevice)

## Whisper API

## ChatGPT API

## Google Cloud Texttospeech API

# Improvements/To-Do
- Recording length is set to 8 seconds, but ideally it would be arbitrary and dependent on the query length. A user would press and hold a button, speak the query, then release to end recording.
