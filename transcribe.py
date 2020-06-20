import sphinxbase as sb
import pyaudio
import speech_recognition as sr
import subprocess
import os

def get_audio(in_file,out_file):
    command = "ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn %s" %(in_file,out_file)

    subprocess.call(command,shell=True)

def transcribe_audio(in_file):
    recog = sr.Recognizer()
    audio_file = sr.AudioFile(in_file)
    with audio_file as source:
        sound = recog.record(source)
        out = recog.recognize_sphinx(sound)
    return out

    

def main():
    get_audio('files/vid.mp4','files/vid.flac')
    print("The audio is: ")
    print(transcribe_audio('files/vid.flac'))
    #os.remove('files/vid.wav')


if __name__ == "__main__":
    main()