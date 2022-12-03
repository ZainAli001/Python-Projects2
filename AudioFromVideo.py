import moviepy
import moviepy.editor


video = moviepy.editor.VideoFileClip("Sample.mp4")
audio = video.audio

audio.write_audiofile("ExtractedAudio.mp3")
