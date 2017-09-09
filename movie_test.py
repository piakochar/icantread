from moviepy.editor import *

video = VideoFileClip("videos/pancakes.mp4").subclip(10,60)

# Make the text. Many more options are available.
txt_clip = ( TextClip("Pancakes, yoooooooo!!! f wit me!!!",fontsize=60,color='white')
             .set_position('center')
             .set_duration(30) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("videos/edited_pancakes2.mp4") # Many options...