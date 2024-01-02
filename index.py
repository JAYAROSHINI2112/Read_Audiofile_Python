import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Specify the path to your audio file
audio_file_path = 'audio_file.wav'

# Load the audio file
with sr.AudioFile(audio_file_path) as source:
    # Adjust for ambient noise and record the audio
    recognizer.adjust_for_ambient_noise(source)
    audio_data = recognizer.record(source)

    # Perform speech recognition
    try:
        text = recognizer.recognize_google(audio_data)
        print(f"Transcription: {text}")
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
