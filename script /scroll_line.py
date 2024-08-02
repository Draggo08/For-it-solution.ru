import os
from moviepy.editor import TextClip, CompositeVideoClip

# Размер видео
width, height = 100, 100
duration = 3  # Продолжительность в секундах

# Создание текста
text = 'Hello world'
text_clip = TextClip(text, fontsize=24, color='blue', size=(width * 2, height)).set_duration(duration)

# Устанавливаем скорость движения надписи
def scroll_text(t):
    return (-width + width * 2 * t / duration, 'center')

# Создание видео
video = CompositeVideoClip([text_clip.set_pos(scroll_text)]).set_duration(duration)

# Сохраняем видео
video.write_videofile("scrolling_text.mp4", fps=24)
