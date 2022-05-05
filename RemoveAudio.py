from moviepy.editor import *

videoclip = VideoFileClip("C:\\Users\\Jyoti\\Downloads\\truestories.mp4")
new_clip = videoclip.without_audio()
new_clip.write_videofile("C:\\Users\\Jyoti\\Downloads\\final_cut.mp4")
clip = VideoFileClip("C:\\Users\\Jyoti\\Downloads\\final_cut.mp4")
clip = clip.subclip(0, 182)
audioclip = AudioFileClip("C:\\Users\\Jyoti\\Downloads\\y2mate.com - Audiomachine  We Are Gods Epic Extension Black Widow Trailer Music.mp3").subclip(0, 182)
videoclip = clip.set_audio(audioclip)
videoclip.write_videofile("C:\\Users\\Jyoti\\Downloads\\final_cut_3.mp4")
#videoclip.ipython_display()
