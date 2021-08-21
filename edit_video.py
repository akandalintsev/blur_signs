from moviepy.video.fx.headblur import headblur

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.interpolators import Trajectory

if __name__ == "__main__":
    clip = VideoFileClip("input/Gorod_2.mp4")
    tr = Trajectory.from_file("gorod_track")

    processed = clip.fx(headblur, tr.xi, tr.yi, 100, 50)
    #
    processed.write_videofile('output/out.mp4')
