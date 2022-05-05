from pydub import AudioSegment
import os

# assign files
input_file = "C:\\Users\\Jyoti\\Downloads\\y2mate.com - Zack Hemsey The Way Instrumental.mp3"
output_file = "C:\\Users\\Jyoti\\Downloads\\result1.wav"
input_2 = "C:\\Users\\Jyoti\\Downloads\\y2mate.com - Audiomachine  We Are Gods Epic Extension Black Widow Trailer Music.mp3"
output_file2 = "C:\\Users\\Jyoti\\Downloads\\result2.wav"

# convert mp3 file to wav file
sound = AudioSegment.from_mp3(input_file)
sound.export(output_file, format="wav")
sound = AudioSegment.from_mp3(input_2)
sound.export(output_file2, format="wav")
sound1 = AudioSegment.from_file("C:\\Users\\Jyoti\\Downloads\\result1.wav", format="wav")
sound2 = AudioSegment.from_file("C:\\Users\\Jyoti\\Downloads\\result1.wav", format="wav")

# sound1 6 dB louder
louder = sound1 + 6

# Overlay sound2 over sound1 at position 0  (use louder instead of sound1 to use the louder version)
overlay = sound1.overlay(sound2, position=0)


# simple export
file_handle = overlay.export("C:\\Users\\Jyoti\\Downloads\\combined_audio.mp3", format="mp3")