import pickle

from moviepy.editor import *
from moviepy.video.tools.tracking import manual_tracking, Trajectory

clip = VideoFileClip("input/Gorod_2.mp4")

if __name__ == "__main__":
    start_frame = 3
    end_frame = 14
    trjectories_count = 1
    trajectories = manual_tracking(
        clip,
        t1=start_frame,
        t2=end_frame,
        nobjects=trjectories_count,
        fps=3,
        savefile="gorod_track"
    )
