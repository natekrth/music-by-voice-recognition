import speech_recognition as sr
import pyttsx3
import pywhatkit
import slowclap as sc

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_accent = "com.apple.speech.synthesis.voice.Alex"
engine.setProperty('voice', voice_accent)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('Hello, what song you want me to play')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Jarvis' in command:
                command = command.reaplace('Jarvis', '')
    except:
        pass
    return command


def run_play():
    command = take_command()
    print(command)
    if 'Play' or 'play' in command:
        song = command.replace("Play" or "play", '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

def play():
    command = take_command()
    print(command)
    song = command.replace("Play" or "play", '')
    talk('playing' + song)
    pywhatkit.playonyt(song)

feed = sc.MicrophoneFeed()
detector = sc.AmplitudeDetector(feed, threshold=10000)
for clap in detector:
    play()
    break