import os
from moviepy.editor import AudioFileClip, AudioClip
import moviepy.audio as mpa
import moviepy
import math
import shutil


def split(audio=None, filename=None, sec_size=5,tempdir='temp', sec_name='sec'):
    if filename is not None:
        clip = AudioFileClip(filename)

    if audio is not None:
        clip = audio
 
    try:
        shutil.rmtree(tempdir)
    except:
        pass

    try:
        os.makedirs(tempdir)
    except:
        pass

    duration = clip.duration
    sections = math.ceil(duration/sec_size)

    i = 0
    for i in range(0, sections - 1):
        start = i * sec_size
        end = (i+1) * sec_size
        copy = clip.subclip(start, end)

        if i < 9:
            fname = sec_name + '(0' + str(i+1) + ').mp3'
        else:
            fname = sec_name + '(' + str(i+1) + ').mp3'

        path = os.path.join(tempdir, fname)
        copy.write_audiofile(path)

    start = end
    end = clip.end
    copy = clip.subclip(start, end)
    path = os.path.join(tempdir, sec_name + '(' + str(i+2) + ').mp3')
    copy.write_audiofile(path)
