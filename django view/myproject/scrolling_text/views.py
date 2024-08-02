import os
from django.http import JsonResponse, FileResponse
from django.views import View
from django.shortcuts import render
from .forms import TextForm
from .models import TextModel
from moviepy.editor import TextClip, CompositeVideoClip

os.environ['IMAGE_MAGICK_BINARY'] = '/usr/bin/convert'

class IndexView(View):
    def get(self, request):
        form = TextForm()
        return render(request, 'scrolling_text/index.html', {'form': form})

    def post(self, request):
        form = TextForm(request.POST)
        if form.is_valid():
            text_instance = form.save()

            # Параметры видео
            width, height = 100, 100
            duration = 3  # Продолжительность в секундах
            text = text_instance.text

            text_clip = TextClip(text, fontsize=24, color='white', size=(width * 2, height)).set_duration(duration)

            def scroll_text(t):
                return (-width + width * 2 * t / duration, 'center')

            video = CompositeVideoClip([text_clip.set_position(scroll_text)]).set_duration(duration)
            output_path = os.path.join(os.getcwd(), 'scrolling_text.mp4')
            video.write_videofile(output_path, fps=24)

            response = FileResponse(open(output_path, 'rb'), as_attachment=True, filename='scrolling_text.mp4')
            return response
        return render(request, 'scrolling_text/index.html', {'form': form})
