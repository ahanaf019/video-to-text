import os
import moviepy.editor as mp


def vid_to_audio(filename):
    clip = mp.VideoFileClip(filename)
    # clip.audio.write_audiofile("my_result_16000.mp3", fps=16000)
    # print(clip.audio)
    return clip.audio
