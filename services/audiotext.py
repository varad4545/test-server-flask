import speech_recognition as sr
import pyaudio
import openai
import io
from dotenv import load_dotenv
load_dotenv()
import os
openai.api_key = os.getenv('OPEN_AI_KEY')

def transcribe_audio(audio_data):
    r = sr.Recognizer()
    audio = sr.AudioData(audio_data, sample_rate=44100, 
                         sample_width=2)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002", # specify the GPT-3 engine to use
        prompt=prompt,
        max_tokens=1024, # set the maximum number of tokens in the generated text
        n=1, # generate a single response
        stop=None, # let the API decide when to stop generating text
        temperature=0.5, # control the "creativity" of the generated text
    )
    return response.choices[0].text.strip()

def record_audio():
    r = sr.Recognizer()

    # Parameters for recording
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    
    # Start recording
    audio_data = io.BytesIO()
    with sr.Microphone() as source:
        print("Recording started...")
        audio_stream = r.listen(source, phrase_time_limit=RECORD_SECONDS)
        audio_data = audio_stream.get_raw_data(convert_rate=RATE, convert_width=2)

    return audio_data