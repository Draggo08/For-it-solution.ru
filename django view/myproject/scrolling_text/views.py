import os
from django.http import FileResponse
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

            width, height = 100, 100
            duration = 3
            text = text_instance.text

            font_path = os.path.join(os.path.dirname(__file__), 'static/fonts/DejaVuSans-Bold.ttf')

            fontsize = 24
            text_clip = TextClip(text, fontsize=fontsize, color='white', bg_color='black', font=font_path)
            text_width = text_clip.size[0]

            scroll_speed = (width + text_width) / duration

            def scroll_text(t):
                return (width - t * scroll_speed, 'center')

            text_clip = text_clip.set_position(scroll_text).set_duration(duration)
            video = CompositeVideoClip([text_clip], size=(width, height)).set_duration(duration)

            output_path = os.path.join(os.getcwd(), 'scrolling_text.mp4')
            video.write_videofile(output_path, fps=24)

            response = FileResponse(open(output_path, 'rb'), as_attachment=True, filename='scrolling_text.mp4')
            return response
        return render(request, 'scrolling_text/index.html', {'form': form})
