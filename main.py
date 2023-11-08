from moviepy.editor import VideoFileClip
import os

chemin_fichier_mp4 ="Ninho - Filon (Clip Vidéo).mp4"
video_clip = VideoFileClip(chemin_fichier_mp4)
audio_clip = video_clip.audio

# Extraire le nom du fichier sans extension
nom_fichier_sans_extension = os.path.splitext(os.path.basename(chemin_fichier_mp4))[0]

# Générer le chemin du fichier de sortie MP3 en utilisant le nom extrait
chemin_fichier_sortie = f"{nom_fichier_sans_extension}.mp3"

audio_clip.write_audiofile(chemin_fichier_sortie)

video_clip.close()
audio_clip.close()