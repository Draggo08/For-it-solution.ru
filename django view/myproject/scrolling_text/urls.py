from django.urls import path
from .views import CreateScrollingTextView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_video/', CreateScrollingTextView.as_view(), name='create_scrolling_text'),
]
