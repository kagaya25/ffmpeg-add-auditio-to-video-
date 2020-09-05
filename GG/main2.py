import moviepy.editor as mpe
clip = mpe.VideoFileClip("C:/laragon/www/GG/1.avi")
audio_bg = mpe.AudioFileClip("C:/laragon/www/GG/main.mp3")
final_audio = mpe.CompositeAudioClip([audio_bg, clip.audio])
final_clip = clip.set_audio(final_audio)
final_clip.write_videofile("out/output.mp4")