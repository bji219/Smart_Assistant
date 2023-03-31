import whisper

def speech_to_text(speech_file):

    # Whisper AI model from OpenAI
    model = whisper.load_model('base')

    stt = model.transcribe(speech_file)

    stt_str = stt['text']
    print(stt_str)
    return stt_str