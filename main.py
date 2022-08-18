from audio_to_text import *
from vid_to_audio import *
from split_audio import *
import os


filename = 'speech.mp4'
tempdir = 'temp'
sec_name = 'sec'

def main():

    audio = vid_to_audio(filename)
    split(audio=audio, sec_size=5, tempdir=tempdir, sec_name=sec_name)

    files = sorted(os.listdir(tempdir))

    for file in files:
        transcription = transcribe(os.path.join(tempdir, file))

        print(file + ': ' + transcription)
        print(file)


def clean_temp():
    shutil.rmtree(tempdir)


if __name__ == '__main__':
    main()
    clean_temp()