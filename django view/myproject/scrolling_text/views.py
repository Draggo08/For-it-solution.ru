import os
from django.http import JsonResponse, FileResponse
from django.views import View
from django.shortcuts import render
from moviepy.editor import TextClip, CompositeVideoClip

os.environ['IMAGE_MAGICK_BINARY'] = '/usr/bin/convert'  # Укажите правильный путь, если требуется

class IndexView(View):
    def get(self, request):
        return render(request, 'scrolling_text/index.html')

class CreateScrollingTextView(View):
    def get(self, request):
        # Параметры видео
        width, height = 100, 100
        duration = 3  # Продолжительность в секундах

        text = 'Hello world'
        text_clip = TextClip(text, fontsize=24, color='blue', size=(width * 2, height)).set_duration(duration)

        def scroll_text(t):
            return (-width + width * 2 * t / duration, 'center')

        video = CompositeVideoClip([text_clip.set_position(scroll_text)]).set_duration(duration)
        output_path = os.path.join(os.getcwd(), 'scrolling_text.mp4')
        video.write_videofile(output_path, fps=24)

        response = FileResponse(open(output_path, 'rb'), as_attachment=True, filename='scrolling_text.mp4')
        return response
