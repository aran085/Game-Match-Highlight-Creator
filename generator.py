
import librosa 
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import IPython.display as ipd 
import os,shutil
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips


#Load the audio file of the sports clip.
filename='M27 KKR vs RCB  – Match Highlights.mp3' #Enter your audio file name of match here. .wav,.mp3, etc. are supported.
vid, sample_rate = librosa.load(filename,sr=16000)
print(int(librosa.get_duration(vid, sample_rate)/60))

#Breaking down video into chunks of 5 seconds so that rise in energy can be found.
chunk_size=5 
window_length = chunk_size * sample_rate

#seeing an audio sample and it's time-amplitude graph
a=vid[5*window_length:6*window_length] 