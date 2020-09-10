# pip3 install moviepy --user

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import math, os, time

def runBash(command):
	os.system(command)

def crop(start,end,input,output):
	str = "ffmpeg -i " + input + " -ss " + start + " -to " + end + " " + output
	print(str)
	runBash(str)


VIDEO_FILE = 'jellyfish2.m4v'
CLIP_LENGTH_SECONDS = 10

clip = VideoFileClip(VIDEO_FILE)
# END_TIME = int((clip.duration-CLIP_LENGTH_SECONDS))
END_TIME = 1000

buckets=range(30, END_TIME, CLIP_LENGTH_SECONDS)


for starttime in buckets:
    endtime=starttime+CLIP_LENGTH_SECONDS
    targetname=str(starttime) + "-" + str(endtime) +".mp4"

    endtime_stamp = time.strftime('%H:%M:%S', time.gmtime(endtime))
    starttime_stamp = time.strftime('%H:%M:%S', time.gmtime(starttime))


    print(targetname)
    crop(starttime_stamp, endtime_stamp, VIDEO_FILE, targetname)
    # ffmpeg_extract_subclip(VIDEO_FILE, starttime, endtime, targetname=str(starttime) + "-" + str(endtime) +".mp4")
